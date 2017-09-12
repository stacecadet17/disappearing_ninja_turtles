from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    return render_template('allninjas.html')

@app.route('/ninja/<color>')
# color tag acts as a placeholder for value we want to pass through
def color(color):
    # define the argument that we are going to be dealing with
    if color == "red":
        image = "/static/Ninjas/raphael.jpg"
        # set image value to the file path that corresponds to input color
    elif color == "blue":
        image = "/static/ninjas/leonardo.jpg"
    elif color == "orange":
        image = "/static/ninjas/michelangelo.jpg"
    elif color == "purple":
        image = "/static/ninjas/donatello.jpg"
    else:
        image = "/static/ninjas/notapril.jpg"




    return render_template('ninja.html', image = image)
    # define the variables that we want to pass through (image) when rendering the template.
    # in the html file, the image is denoted with the {{color}} as the id, and the source is the variable {{image}}

app.run(debug=True)
