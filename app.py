from flask import Flask, render_template, request
from predict import *

# Creating flask app
app = Flask(__name__, template_folder='./public')

# Initialize the model
model = init_model()


# Home endpoint, render html file
@app.route('/')
def render():
    return render_template('index.html')


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    file = request.files['file1']
    file.save('./static/file.jpg')


# Run app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port=port)
