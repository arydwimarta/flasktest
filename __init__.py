from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from babel import dates
#from datetime import date, datetime, time, timedelta
import datetime
import pytz

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'flask'
app.config['MYSQL_DB'] = 'flaskemail'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM email")
    data = cur.fetchall()
    cur.close()




    return render_template('index2.html', email=data )



@app.route('/save_mails', methods = ['POST'])
def insert():

    #d = date(2007, 4, 1)

    if request.method == "POST":
        flash("Data Inserted Successfully")
        email = request.form['email']
        email_subject = request.form['email_subject']
        email_content = request.form['email_content']
        #time_stamp = dates.format_date(d, locale='en_US')
        #time_stamp = request.form['time_stamp']
        #time_stamp = datetime.datetime.utcnow().replace(microsecond=0)
        dt_mtn = datetime.datetime.now(tz=pytz.timezone('Asia/Singapore'))
        time_stamp = dt_mtn.strftime('%d %b %Y %H:%M')
        #newdate = newline.strip()
        #time_stamp = datetime.datetime.strptime(newdate,'%d/%b/%Y:%H:%M:%S')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO email (email, email_subject, email_content, time_stamp) VALUES (%s, %s, %s, %s)", (email, email_subject, email_content, time_stamp))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM email WHERE event_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['event_id']
        email = request.form['email']
        email_subject = request.form['email_subject']
        email_content = request.form['email_content']
        time_stamp = request.form['time_stamp']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE email
               SET email=%s, email_subject=%s, email_content=%s, time_stamp=%s
               WHERE id=%s
            """, (email, email_subject, email_content, time_stamp))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(debug=True)
