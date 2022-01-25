from http.client import HTTPResponse

from flask import Flask ,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Base.html" )

#-----------------run-------------
if __name__ == "__main__":
    app.run(debug =True)

'''
You can also set params
FLASK_ENV=development
FLASK_APP=main.py
and do flask run commanmd to run the flask app
'''