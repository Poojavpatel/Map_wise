import flask, request
app=flask.Flask("__main__")

@app.route("/" , methods = ['GET'])
def my_index():
    return flask.render_template("index.html",token="Hello world")

@app.route("/uploadfile" , methods = ['POST'])
def myfile():
    data=request.form['upload']

app.run(debug=True)