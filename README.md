![bc83903dece2c55ed2dd2eb44f3d0caa](https://user-images.githubusercontent.com/57374106/125447413-d4e4d16e-67b9-415e-b602-7132ec4a48aa.png)
# ultimaker_statusBoard

Note that this is a work in progress, it is usable but it is not completely done.


Tested on raspberry Pi


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
