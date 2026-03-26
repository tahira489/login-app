from flask import Flask, render_template, request
import pymysql

app= Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            mydb = pymysql.connect(
                host="centerbeam.proxy.rlwy.net",
                port=48772,
                user="root",
                password="pfsJpyfpriJkdQNvrOScKPLNZMudxVZp",
                database="railway",
                ssl={"ssl": {}}
            )
        except Exception as e:
            return f"Database connection failed: {str(0)}"
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM userdata WHERE username = %s AND password = %s',(username,password))
        account = mycursor.fetchone()
        if account:
            print('login succesful')
            name = account[1]
            msg = 'login succesful'
            return render_template('welcome.html', name=name, msg=msg)
        else:
            msg = 'Incorrect Credentials / kindly check'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = "Logged out succesfully"
    return render_template('login.html', msg=msg, name = name, id=id)

if __name__ == '__main__':
    app.run(debug=True)