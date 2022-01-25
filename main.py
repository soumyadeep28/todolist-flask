from flask import Flask
app = Flask(__name__)


@app.route('/')
def index(request):
    return 


#-----------------run-------------
app.run(Debug =True)