from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/<URL>', methods=['POST'])
def convert_video(URL):
    try:
        # Add your video conversion logic here
        return jsonify({"message": f"Processing video from URL: {URL}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['POST', 'GET'])
def default_function():
    return jsonify({"message": "This is the Default Route for Youtube to Mp3 Site"})

# Vercel-specific WSGI handler
def handler(event, context):
    from vercel import wsgi
    return wsgi(app)(event, context)

# WSGI application for general deployment
application = app

if __name__ == '__main__':
    app.run(debug=True)
