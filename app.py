from flask import Flask, render_template 
app = Flask(__name__)


########################################################################
########################################################################
########################################################################
#code

database1 = ["john","doe","goe","doey"]


########################################################################
########################################################################
########################################################################
#VIEW
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",database1 = file_list1)  

@app.route('/about')
def about():
    return 'about'  

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')