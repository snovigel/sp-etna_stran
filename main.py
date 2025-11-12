from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home_page.html")

@app.route('/test/<username>')
def test(username):
    return render_template("test.html", username=username) 

@app.route('/form_test/')
def form_test():
    return render_template("form_test.html")

@app.route('/form-submit/')
def form_submit():
    uporabnisko_ime = request.args.get("username")
    geslo = request.args.get("geslo")
    print(uporabnisko_ime,geslo)
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    insert_command = 'SELECT * FROM contacts WHERE first_name="' + uporabnisko_ime + '" AND last_name="' + geslo + '"'
    print(insert_command)
    cursor.execute(insert_command)
    rezultati = list(cursor)
    conn.close()
    if rezultati:
        return "Prijava je uspešna"
    else:
        return render_template("form_test.html", info_text = "Ni uspela")

    
@app.route('/regi/')
def regi():
    return render_template("regi.html")

@app.route('/registracija_submit/')
def registracija_submit():
    uporabnisko_ime = request.args.get("username")
    geslo = request.args.get("geslo")
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    insert_command ='INSERT INTO contacts(first_name, last_name) VALUES("'+uporabnisko_ime+'", "'+geslo+'")'
    print(insert_command)
    cursor.execute(insert_command)
    conn.commit()
    return "V izvedbi"



@app.route('/view_db/')
def view_db():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("select * from contacts;")
    return cursor.fetchall()

app.run(debug=True)
