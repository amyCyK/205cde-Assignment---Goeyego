from flask import Flask, request
from flask import render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = 'root'
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_DB'] = 'goeyego'

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def register():
	if request.method == 'POST':
		name = request.form['name']
		password = request.form['password']
		phonenumber = request.form["phonenumber"]
		email = request.form['email']
		gender = request.form['gender']
		region = request.form['region']

		cur = mysql.connection.cursor()

		# execute SQL query using execute() method.
		cur.execute("INSERT INTO login (name,password,phonenumber,email,gender,region)VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,password,phonenumber,email,gender,region,))

		mysql.connection.commit()

		cur.close()

		return 'success'

	return render_template("register.html")	

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/news.html')
def news():
    return render_template('news.html')

@app.route('/flight.html')
def flight():
    return render_template('flight.html')

@app.route('/hotel.html')
def hotel():
    return render_template('hotel.html')


headings = ('Name','password','phonenumber','email','gender','region')

data = (('123','123','12345678','123@1234.com','Male','Hong Kong'))

@app.route('/table.html')
def table():
    return render_template('table.html', headings=headings, data=data)

@app.route('/booking.html', methods=['GET','POST'])
def booking():
#	if request.method == 'POST':
#		name = request.form['name']
#		email = request.form['email']
#		phonenumber = request.form["phonenumber"]
#		companyname = request.form['companyname']
#		totalprice = request.form['totalprice']
#		product = request.form['product']
#		region = request.form['region']
#
#		cur = mysql.connection.cursor()
#
#		execute SQL query using execute() method.
#		cur.execute("INSERT INTO booking (name,email,phonenumber,companyname,totalprice,product,region)VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,email,phonenumber,companyname,totalprice,product,region,))
#
#		mysql.connection.commit()
#
#		cur.close()

#		return 'success'
	
    return render_template('booking.html')

@app.route('/currency.html')
def currency():
	return render_template('currency.html')

@app.route('/currencytool.html')
def currencytool():
	return render_template('currencytool.html')

@app.route('/contactus.html')
def contactus():
	return render_template('contactus.html')

if __name__=="__main__":
	app.run(debug=True)