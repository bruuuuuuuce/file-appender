# file-appender
Append data to file with data from an html form. App will be hosted on a url that you can visit, enter data into the input field, and when you click submit, data will be appended to the `data.txt` file

### Pre-requisites
1. [Python 3.7](https://www.python.org/downloads/)
1. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### How to run
1. `git clone https://github.com/dodger012/file-appender.git`
1. `cd file-appender`
1. `python3 -m venv venv`
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `export FLASK_APP=main.py`
1. `flask run`
