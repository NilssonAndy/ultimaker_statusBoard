
# ultimaker_statusBoard

Note that this is a work in progress, it is usable but it is not completely done.


Tested on raspberry Pi

![b0eba29b8430e8cff28e7459c436c2dd](https://user-images.githubusercontent.com/57374106/125447598-9cd7a7cc-c186-4f22-8e98-e5241b73c3ce.png)



INSTRUCTIONS



Open Terminal / BASH



Create a folder for your project (mkdir folder_name)



Navigate to the project folder (cd folder_name)



Create the virtual environment (python3 -m venv ./venv)



Activate the virtual environment (source ./venv/bin/activate)




inside folder_name



pip install Flask



pip install Flask-SocketIO



pip install requests



then still in folder_name type:



git clone https://github.com/NilssonAndy/ultimaker_statusBoard.git



cd ultimaker_statusBoard/service



python3 app.py



navigate to http://127.0.0.1:5000/ in your browser on the local machine
