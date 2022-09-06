#import flask
from flask import Flask

app = Flask(__name__)

#Created main index and two additional pages
@app.route('/')
def home_page():
    return 'Hello world!'

@app.route('/dashboard')
def dashboard():
    return 'This is the dashboard page'

@app.route('/settings')
def settings():
    return 'This is the settings page'

#To run app using 'python app.py' command 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
