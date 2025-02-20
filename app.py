from flask import Flask, jsonify
from flask_cors import CORS
from urllib.parse import unquote
app = Flask(__name__)





CORS(app,resources={r"/*": {"origins": ["http://127.0.0.1:5500", "https://y2mp3-front-end.vercel.app"]}})

@app.route('/')
def default_function():
    try:
        return jsonify({"message":"This is the Default Route for Youtube to Mp3 Site"})
    except Exception as e:
        app.logger.error(f"Error in default_function: {str(e)}")
        raise
@app.route('/download/<path:url>',methods=['POST'])
def download_function(url):
    decoded_url = unquote(url)
    try:
        return jsonify({"recievedUrl":decoded_url});
    except Exception as e:
        app.logger.error(f"Error in default_function: {str(e)}")
        raise





# Vercel requires the application to be exported as 'app'
app = app
