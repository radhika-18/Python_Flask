from flask import Flask


app=Flask(__name__)

@app.route('/local')
def HelloWorld():
    return "Hello World"

if __name__=='__main__':
    app.run()