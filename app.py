from flask import Flask, request, jsonify, render_template, redirect, url_for
from functions.get_contacts import get_contacts
from functions.post_contact import post_contact


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return 'Hubspot Implementation In flask <br/><br/> <a href="/contacts">Contacts List</a><br/><br/><a href="/create-contact">Create Contact</a>'

@app.route("/create-contact", methods=["GET"])
def create_contact():
    return render_template("contact_form.html")

@app.route("/contacts", methods=["GET","POST"])
def operate_contacts():
    if request.method == "GET":
        result = get_contacts()
        return render_template("contacts.html", contacts = result["contacts"])

    if request.method == "POST":
        req = request.form
        result = post_contact(req)
        return redirect(url_for('operate_contacts'))
    else:
        return "Method not allowed"



if __name__ == "__main__":
    app.run(debug=True)
