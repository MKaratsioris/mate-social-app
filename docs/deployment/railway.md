# Railway Platform setup

## Setup App
#### Repository setup
- Make sure there is a file `requirements.txt`.
- Create the file `runtime.txt` and place it in the same folder as `manage.py`. Inside this file, write `python-3.10.2`.
- Create the file `Procfile` and place it in the same folder as `manage.py`. Inside this file, write `web: python3 manage.py makemigrations && python3 manage.py migrate && gunicorn mate.wsgi`

#### Railway setup

## Setup DB
