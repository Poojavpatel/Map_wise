import flask

app=flask.Flask("__main__")
upload_folder = "/data"
app.config['UPLOAD_FOLDER'] =upload_folder

@app.route("/" , methods = ['GET'])
def my_index():
    return flask.render_template("index.html",token="Hello world")

@app.route("/uploadfile" , methods = ['POST'])
def myfile():
    f=request.files['file']
    f.save(f.filename)
    return 'file uploaded successfully'
#     data=request.form['upload']

app.run(debug=True)