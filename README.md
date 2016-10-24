# Simple Ocr Implementation


## Installation

### 1. Install dependencies
```sh
sudo apt-get install tesseract-ocr
```

### 2. Setup Virtual Environment
For [virtualenv](http://pypi.python.org/pypi/virtualenv) follow instructions at: *http://pypi.python.org/pypi/virtualenv*
```sh
sudo pip install -U pip
sudo pip install virtualenv
```

### 3. Get the latest source code
```sh
git clone *******
```

### 4. Create and Activate Virtual Environment
```sh
virtualenv -p python3 myenv
source myenv/bin/activate
```

### 5. Get libraries
```sh
pip install -r requirements.txt
```

### 6. Initialise the database
```sh
python manage.py migrate
```

### 9. Run local server
```sh
python manage.py runserver
```

### 10. Visit the following url to get started
```sh
http://localhost:8000/index/
```