ADVANCED FIREWALL PROJECT
This is a web application designed to manage incoming and outgoing network traffic using predefined rules.
FUNCTIONALITY:
1.	Login Authentication:
Provides secure access to the application.
2.	Whitelists and Blacklists Management:
Allows users to manage lists of allowed and blocked entities.
3.	Rule Management:
Facilitates adding, moving, and removing rules between whitelists and blacklists.
4.	Packet Validation:
Checks the validity of network packets based on configured rules.

OBJECTIVES:

1.	Design Patterns
•	Strategy, Factory, and Singleton Patterns: 
Implemented for efficient rule handling and scalability.

3.	Network Traffic Filtering
•	IP Addresses, Ports, and Protocols: 
Implements strategies for filtering traffic based on these parameters.

5.	User Interface
•	Rule Management Interface:
Provides a user-friendly web interface for setting rules and monitoring network traffic.

SOFTWARE REQUIREMENTS:
•	Python 3.12 or later: Core programming language.
•	Flask: Web framework for building the application.

INSTALLATION:
Step 1: First, we must install the dependencies:
 
Step 2: we must run the application:
 
Step 3: Usage, we must access this on 
 

Logging In:
1.	Use the default admin credentials:
o	Username: admin
o	Password: password

Navigating the Application:
3.	Use the home page to manage rules, display lists, and check packets.

•	Firewall/: Contains core application files.
o	__init__.py: Initialization file.
o	strategy_factory.py: Implements strategy and factory patterns.
o	ip_filter.py: Handles IP filtering logic.
o	settings.py: Configuration settings.
•	templates/: HTML templates for the web interface.
o	index.html: Main page template.
o	home.html, set_rules.html, display_lists.html, check_packet.html: Specific page templates.
•	static/: Static files like CSS for styling.
o	style.css: CSS stylesheets.
•	app.py: Entry point for running the Flask application.
•	requirements.txt: Lists all dependencies required for the project.

STEPS TO COMPLETE PROJECT:

Step 1: Set Up Configuration Settings (Singleton Pattern)
•	Purpose: Ensure only one instance of the settings exists.
•	File: config/settings.py

Step 2: Define the Base Strategy (Strategy Pattern)
•	Purpose: Create an abstract base class for filtering network traffic.
•	File: firewall/base_strategy.py

Step 3: Implement IP Filter Strategy
•	Purpose: Filter network traffic based on IP addresses.
•	File: firewall/ip_filter.py

Step 4: Implement Port Filter Strategy
•	Purpose: Filter network traffic based on ports.
•	File: firewall/port_filter.py

Step 5: Implement Protocol Filter Strategy
•	Purpose: Filter network traffic based on protocols.
•	File: firewall/protocol_filter.py

Step 6: Create the Strategy Factory (Factory Pattern)
•	Purpose: Create instances of different firewall strategies.
•	File: firewall/strategy_factory.py

Step 7: Combine Everything in the Main File
•	Purpose: Use the strategies for filtering network traffic.
•	File: main.py

![image](https://github.com/user-attachments/assets/59cebe14-f472-43ec-95b6-c0bd3269491e)

WORKING:
1.	Firstly run the app.py file
![image](https://github.com/user-attachments/assets/4e3a397e-ce74-4060-90b0-d3353bef4d00)

Step 2 click on Running on http://127.0.0.1:5000
![image](https://github.com/user-attachments/assets/16ba8ed4-3fe2-4039-ae08-31ac2f9d20ed)

Step 3 Login: username – admin password- password (you can do following things mentioned there)
![image](https://github.com/user-attachments/assets/54a5c275-70f9-4e30-8a81-0b20d921c970)

Step 4: after setting rules and IP’s we will check for the packets:
![image](https://github.com/user-attachments/assets/26af786c-32f3-4ddb-a5ce-28743d5a743c)




