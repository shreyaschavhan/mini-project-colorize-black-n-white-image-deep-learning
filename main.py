from flask import Flask
from flask import render_template, request
import os
import colorize

app = Flask(__name__)
UPLOAD_FOLDER = "A:\in-tray\mini project\DL\static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/result', methods=('GET', 'POST'))
def result():
    if request.method == 'POST':
        image = request.files['image']
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'original.jpg'))
        colorize.colorize(os.path.join(app.config['UPLOAD_FOLDER'], 'original.jpg'))
    return render_template("results.html")

if __name__ == "__main__":
    app.run()
