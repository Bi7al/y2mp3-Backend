from flask import Flask, jsonify
app = Flask(__name__)







@app.route('/')
def default_function():
    try:
        return "This is the Default Route for Youtube to Mp3 Site"
    except Exception as e:
        app.logger.error(f"Error in default_function: {str(e)}")
        raise





# Vercel requires the application to be exported as 'app'
app = app
