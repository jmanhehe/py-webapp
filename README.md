# Setup

## Enter venv (Virtual environment)

### Windows  

python -m venv venv  
venv\Scripts\activate

### Mac/Linux

python3 -m venv venv  
source venv/bin/activate

## Install dependency inside the environment

pip install flask  
pip install requests

## Check that flask is installed correctly (Optional)

```py
python -c "import flask; print(flask.__version__)"
```

## Start script (Start the application)

python main.py

## Check url

[http://127.0.0.1:5000/todos](http://127.0.0.1:5000/todos)

## Deactivate venv (Close virtual environment)

deactivate  
