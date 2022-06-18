from flask import Flask
from dalle import 

app = Flask(__name__)

"""app routes"""
@app.route('/')
def get_song():
    return 

if __name__ == '__main__':
    app.run()
