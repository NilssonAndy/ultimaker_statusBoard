# ultimaker_statusBoard

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
