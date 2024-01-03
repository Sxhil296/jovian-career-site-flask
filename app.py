from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def hello_world():
    # return "Hello, World!"
    return render_template('home.html')

if __name__== "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    # serve(app, host="0.0.0.0", port=8000)
