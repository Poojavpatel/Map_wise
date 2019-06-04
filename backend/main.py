import flask
app=flask.Flask("__main__")

@app.route("/" , methods = ['GET'])
def my_index():
    return flask.render_template("index.html",token="Hello world")

app.run(debug=True)