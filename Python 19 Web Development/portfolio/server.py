from flask import Flask, render_template

# instantiating the flask application
app = Flask(__name__)
print(__name__)

# decorator - this allows us to do more with a simple function
# here app.route gives it web server festures, such as security, authentication etc...

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)




# add a favicon
