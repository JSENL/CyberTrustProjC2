from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/payloads')
def payloads():
    return render_template('payloads.html')

@app.route('/listeners')
def listeners():
    return render_template('listeners.html')

@app.route('/connections')
def connections():
    return render_template('connection.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

