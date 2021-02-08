Scope of work:

    -   To develop a flask based socket server which allows to 
        
        - connect 
        - disconnect
        - send event periodically. Example ebike speed.
        
    -   To have effective, scalable and maintainable code structure.
    

Assumption

    -   No user authentication
    -   Periodic speed is being by virtual device.


Key Feature

    -   Flask based Socket Server
    -   Virtual device contnuously broadcasting speed.
    -   Configuration driven via environment based config files
    -   Functional/Pythonic approach
    -   Separation of concern via proper directory structure
    -   Dependency management via requirements.txt
    -   Code Reusability via decorator
    -   Centralised error handling.
    -   File and console based logging
    -   Stubbed Authentication middleware
    -   Support for CORS feature for separate React hosting
    -   Virtual environment
    -   Setup
    

Possible enhancement

    -   Deployment using docker.
    -   Deployment using gunicorn.
    -   Unit test
    -   Cluster based socket server using Queues and sticky sessions.
    
    
How to Run

    -   git clone https://github.com/gauravguptabits/imp_flask_ws.git
    
    -   Create Virtual environment
        
        -   pip install virtualenv
        -   virtualenv venv
        -   source venv/bin/activate
        
    -   Install dependencies
        
        -   pip install -r requirements.txt
    
    -   Start Server
    
        -   python app.py
        
    
    -   Open the url in browser ( http://localhost:5000/ )
    

How app works

    -   Server reads the configuration based on the environment mentioned in the .env file.
    -   Server spawns the thread which continously generate the speed (a random number). This is called virtual device 
    and is mimicing the ebike which will send events to the server continuously.
    -   With the link open in browser, user will be able to
        
        -   establish the connection with server using "Connect Button" which will fire "connect" event.
        -   subscribe to "speed_change" event.
        -   disconnect the connection via "disconnect Button" which will fire "disconnect" event.
    
           
    
    