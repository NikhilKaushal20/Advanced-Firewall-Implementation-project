from flask import Flask, render_template, request, redirect, url_for, session
from Firewall.strategy_factory import StrategyFactory
from Config.settings import Settings

app = Flask(__name__)
app.secret_key = 'your_secret_key'

settings = Settings()

# Dummy admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"
    return render_template('index.html')

@app.route('/home')
def home():
    if 'admin' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/set_rules', methods=['GET', 'POST'])
def set_rules():
    if 'admin' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        ip = request.form.get('ip')
        port = request.form.get('port')
        protocol = request.form.get('protocol')
        list_type = request.form.get('list_type')
        entry = f"{ip},{port},{protocol}"
        if list_type == 'whitelist':
            settings.add_to_whitelist(entry)
        elif list_type == 'blacklist':
            settings.add_to_blacklist(entry)
    return render_template('set_rules.html')

@app.route('/display_lists', methods=['GET', 'POST'])
def display_lists():
    if 'admin' not in session:
        return redirect(url_for('login'))
    message = None
    if request.method == 'POST':
        ip = request.form.get('ip')
        port = request.form.get('port')
        protocol = request.form.get('protocol')
        list_type = request.form.get('list_type')
        entry = f"{ip},{port},{protocol}"
        if list_type == 'move_to_whitelist':
            if entry in settings.get_blacklist():
                settings.remove_from_blacklist(entry)
                settings.add_to_whitelist(entry)
                message = "Entry moved to whitelist."
            else:
                message = "Entry not found in blacklist."
        elif list_type == 'move_to_blacklist':
            if entry in settings.get_whitelist():
                settings.remove_from_whitelist(entry)
                settings.add_to_blacklist(entry)
                message = "Entry moved to blacklist."
            else:
                message = "Entry not found in whitelist."
    whitelist = settings.get_whitelist()
    blacklist = settings.get_blacklist()
    return render_template('display_lists.html', whitelist=whitelist, blacklist=blacklist, message=message)

@app.route('/check_packet', methods=['GET', 'POST'])
def check_packet():
    if 'admin' not in session:
        return redirect(url_for('login'))
    result = None
    if request.method == 'POST':
        ip = request.form.get('ip')
        port = request.form.get('port')
        protocol = request.form.get('protocol')
        packet = {"ip": ip, "port": port, "protocol": protocol}
        try:
            if settings.is_allowed(packet):
                result = "Packet allowed"
            else:
                result = "Packet denied"
        except Exception as e:
            result = f"Invalid packet format: {e}"
    return render_template('packet_check.html', result=result)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
