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
2.	Network Traffic Filtering
•	IP Addresses, Ports, and Protocols: 
Implements strategies for filtering traffic based on these parameters.
3.	User Interface
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
2.	Use the home page to manage rules, display lists, and check packets.
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
