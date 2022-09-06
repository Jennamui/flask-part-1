from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello world!'

@app.route('/dashboard')
def dashboard():
    return 'This is the dashboard page'

@app.route('/settings')
def settings():
    return 'This is the settings page'
  
if __name__ == '__main__':
app.run(debug=True, host='0.0.0.0', port=80)
