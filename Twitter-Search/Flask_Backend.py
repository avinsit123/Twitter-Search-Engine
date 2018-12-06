from flask import Flask,request,render_template
from Mine_Data import find_friends
#ML Packages

app = Flask(__name__)
#Bootstrap(app)


@app.route('/')
def index():
    return render_template("Main_Page.html")


@app.route('/check_followers', methods=['POST','GET'])
def check_followers():
    if request.method=='POST':
        friends=find_friends()
        return friends


@app.route('/User',methods=['POST','GET'])
def User():
    return "aHello"

@app.route('/Search',methods=['POST','GET'])
def Search():
    return "bHello"





if __name__ == '__main__':
    app.run(debug=True)