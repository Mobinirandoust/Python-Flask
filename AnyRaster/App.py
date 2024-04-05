from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from packagee import unic

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DAtabase.sqlite"

db = SQLAlchemy()
db.init_app(app)

class Landsat7(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column()
    tel:Mapped[int] = mapped_column()
    band1:Mapped[str] = mapped_column()
    band2:Mapped[str] = mapped_column()
    band3:Mapped[str] = mapped_column()
    band4:Mapped[str] = mapped_column()
    band5:Mapped[str] = mapped_column()
    band6:Mapped[str] = mapped_column()
    band7:Mapped[str] = mapped_column()
    city:Mapped[str] = mapped_column()
    history:Mapped[str] = mapped_column()
    date:Mapped[str] = mapped_column()
    takmili:Mapped[str] = mapped_column()

class Landsat8(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column()
    tel:Mapped[int] = mapped_column()
    band1:Mapped[str] = mapped_column()
    band2:Mapped[str] = mapped_column()
    band3:Mapped[str] = mapped_column()
    band4:Mapped[str] = mapped_column()
    band5:Mapped[str] = mapped_column()
    band6:Mapped[str] = mapped_column()
    band7:Mapped[str] = mapped_column()
    city:Mapped[str] = mapped_column()
    history:Mapped[str] = mapped_column()
    date:Mapped[str] = mapped_column()
    takmili:Mapped[str] = mapped_column()

class Landsat9(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column()
    tel:Mapped[int] = mapped_column()
    band1:Mapped[str] = mapped_column()
    band2:Mapped[str] = mapped_column()
    band3:Mapped[str] = mapped_column()
    band4:Mapped[str] = mapped_column()
    band5:Mapped[str] = mapped_column()
    band6:Mapped[str] = mapped_column()
    band7:Mapped[str] = mapped_column()
    city:Mapped[str] = mapped_column()
    history:Mapped[str] = mapped_column()
    date:Mapped[str] = mapped_column()
    takmili:Mapped[str] = mapped_column()

with app.app_context():
    db.create_all()

@app.route('/',methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/landsat7',methods=["GET","POST"])
def index7():
    if request.method == "POST":
        try:
            requestuser = Landsat7(
            code = unic(),
            name = request.form['name'],
            tel = request.form['tel'],
            band1 = request.form['L7band1'],
            band2 = request.form['L7band2'],
            band3 = request.form['L7band3'], 
            band4 = request.form['L7band4'],
            band5 = request.form['L7band5'],
            band6 = request.form['L7band6'],
            band7 = request.form['L7band7'], 
            history = request.form['history'],
            city = request.form['city'],
            date = datetime.now(),
            takmili = request.form['text'],
            )
            db.session.add(requestuser)
            db.session.commit()
            return render_template('index7.html',report=f"اطلاعات با موفقیت ارسال شد منتظر تماس ما باشید \t کد پیگیری شما {requestuser.code}")
        except:
            return render_template('index7.html',report="لطفا باند هایی که مورد نظرتان نیست را روی آف قرار دهید")
    return render_template('index7.html')

@app.route('/landsat8',methods=["GET","POST"])
def index8():
    if request.method == "POST":
        try:
            requestuser = Landsat8(
            code = unic(),
            name = request.form['name'],
            tel = request.form['tel'],
            band1 = request.form['L8band1'],
            band2 = request.form['L8band2'],
            band3 = request.form['L8band3'],
            band4 = request.form['L8band4'],
            band5 = request.form['L8band5'],
            band6 = request.form['L8band6'],
            band7 = request.form['L8band7'],
            history = request.form['history'],
            city = request.form['city'],
            date = datetime.now(),
            takmili = request.form['text'],
            )
            db.session.add(requestuser)
            db.session.commit()
            return render_template('index8.html',report=f"اطلاعات با موفقیت ارسال شد منتظر تماس ما باشید \t کد پیگیری شما {requestuser.code}")
        except:
            return render_template('index8.html',report="لطفا باند هایی که مورد نظرتان نیست را روی آف قرار دهید")
    return render_template('index8.html')

@app.route('/landsat9',methods=["GET","POST"])
def index9():
    if request.method == "POST":
        try:
            requestuser = Landsat9(
            code = unic(),
            name = request.form['name'],
            tel = request.form['tel'],
            band1 = request.form['L9band1'],
            band2 = request.form['L9band2'],
            band3 = request.form['L9band3'],
            band4 = request.form['L9band4'],
            band5 = request.form['L9band5'],
            band6 = request.form['L9band6'],
            band7 = request.form['L9band7'],
            history = request.form['history'],
            city = request.form['city'],
            date = datetime.now(),
            takmili = request.form['text'],
            )
            db.session.add(requestuser)
            db.session.commit()
            return render_template('index9.html',report=f"اطلاعات با موفقیت ارسال شد منتظر تماس ما باشید \t کد پیگیری شما {requestuser.code}")
        except:
            return render_template('index9.html',report="لطفا باند هایی که مورد نظرتان نیست را روی آف قرار دهید")
    return render_template('index9.html')


@app.route("/admin",methods=["GET","POST"])
def admin():
    if request.method == "POST":
        admin = str(request.form["Admin"])
        pasw = str(request.form["Password"])
        if admin == "SuperAdmin":
            if pasw == "Raster4$":
                user_7 = db.session.execute(db.select(Landsat7).order_by(Landsat7.id)).scalars().all()
                user_8 = db.session.execute(db.select(Landsat8).order_by(Landsat8.id)).scalars().all()
                user_9 = db.session.execute(db.select(Landsat9).order_by(Landsat9.id)).scalars().all()
                return render_template('AdminActivate.html',user7=user_7,user8=user_8,user9=user_9)
    return render_template('Admin.html')



# حذف کاربر از طریق آیدی امکان پذیر شد
@app.route("/admin/delete7/",methods=["GET","POST"])
def del_user_by_id7():
    select = request.args.get('id1')
    request_user = db.get_or_404(Landsat7,select)
    db.session.delete(request_user)
    db.session.commit()
    return redirect('/admin')

@app.route("/admin/delete8/",methods=["GET","POST"])
def del_user_by_id8():
    select = request.args.get('id1')
    request_user = db.get_or_404(Landsat8,select)
    db.session.delete(request_user)
    db.session.commit()
    return redirect('/admin')

@app.route("/admin/delete9/",methods=["GET","POST"])
def del_user_by_id9():
    select = request.args.get('id1')
    request_user = db.get_or_404(Landsat9,select)
    db.session.delete(request_user)
    db.session.commit()
    return redirect('/admin')

@app.route("/store/images/")
def store_images():
    return render_template('image.html')

@app.route("/<name>")
def index_Error_404(name):
    return render_template("Error404.html")

if __name__=='__main__':
    app.run(host='127.0.0.1',debug=True)
