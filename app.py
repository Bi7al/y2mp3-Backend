from flask import Flask
app = Flask(__name__)



@app.route('/')
def default_function():
    return  "This is the Default Route for Youtube to Mp3 Site"



if __name__ == '__main__':
    app.run();
