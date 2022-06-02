## Quick Flask setup
Use this quick guide to be up and running with Flask
1. Install flask using [this guide](https://flask.palletsprojects.com/en/1.0.x/installation/#installation)
2. After you have created your venv from previous step. Create a project folder and copy [hello.py](hello.py) there
3. Follow the below lines to setup the flask and run the server\
    - Linux/MacOS\
    `export FLASK_APP=hello.py`\
    `flask run`
    - Windows PowerShell\
    `$env:FLASK_APP = "hello.py"`\
    `flask run`
4. Go to this url http://127.0.0.1:5000/
If everything was setup correctly you should see a "Hello World!" in the page
5. Read the quickstart guide for more information - [Link](https://flask.palletsprojects.com/en/1.0.x/quickstart/#quickstart)