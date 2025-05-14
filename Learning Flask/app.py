from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Jss@1313'
app.config['MYSQL_DB'] = 'job_form'

UPLOAD_FOLDER = 'static/resumes'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mysql = MySQL(app)

@app.route("/",methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        college_name = request.form['college_name']
        graduation_year = request.form['graduation_year']
        stream = request.form['stream']
        position = request.form['position']
        resume = request.files['resume']

        filename = secure_filename(resume.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(filepath)

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO job_application 
            (name, email, phone, address, college_name, graduation_year, stream, position, resume_path)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, email, phone, address, college_name, graduation_year, stream, position, filepath))
        mysql.connection.commit()
        cur.close()

        return "Form submitted successfully!"
    return render_template('form.html')

@app.route("/applications")
def applications():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM job_application")
    data = cur.fetchall()
    cur.close()
    return render_template('applications.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)