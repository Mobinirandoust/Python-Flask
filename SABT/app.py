from flask import Flask,redirect,render_template,request
from typing import Optional
from random import choice
from string import ascii_letters
from sys import getsizeof
import validators
app = Flask(__name__)
collec = {} # memory

# Function is make ShortName for web
def create_shortname():
    base = ""
    for i in range(choice(range(3,7))):
        i = choice(ascii_letters)
        base = base+i
    return base

# Function is create dict of collec
def creat_link(k:Optional[str] | None , v:Optional[str] | None):
    collec[k] = v
    return collec

# Route's:

# Route 1
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        key = create_shortname()
        val = request.form["val"]
        if validators.url(val):
            creat_link(key,val)
            return render_template('index.html',key=key,val=val)
        else:
            msg = "لطفا آدرس وبسایت را درست وارد کنید http://mihan.ir"
            return render_template('index.html',key='Error',val='Error',msg=msg)
    return render_template('index.html')

# Route 2
@app.route("/<username>")
def box(username):
    try:
        if username == "Admin0.0&%":
            return collec
        else:
            return redirect(collec[username]) # This is *: این خط همون لینک کوتاه شده است که کاربر به وبسایت هدایت میکند
    except:
        return '<h2>The shortened link is wrong: <a href="/">Create a short link</a></h2>'

# Route 3
@app.route("/<x>/<y>")
def handle(x,y):
    if x == '1400' and y == '1500':
        return f'Collec = {getsizeof(collec)}'
    return '<h2>The shortened link is wrong: <a href="/">Create a short link</a></h2>'

# Route 4
@app.route("/adminator/<object>")
def clear(object):
    if object == 'all-memory-collec':
        collec.clear()
        return "Clear of memmory!"
    elif type(object) == type(""):
        collec.pop(object)
        return "key seleced is dalate!"

app.run(debug=True)
