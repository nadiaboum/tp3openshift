from flask import Flask, render_template, request , send_file, redirect, url_for, Response, redirect

app = Flask(__name__)
import sys
import os

@app.route('/', methods=['GET' , 'POST'])


def home():
    if request.form:
        compteurtues = 0
        listevaincus = []
        pseudo = request.form['pseudo']

        monpersonnage = personnage(pseudo, 20,6,3)
        
        while monpersonnage[1] > 0:
            monstreennemi = createMob()
            fight(monpersonnage, monstreennemi)

            if monpersonnage[1] > 0:
                compteurtues = compteurennemistues(compteurtues)
                listevaincus.append(monstreennemi[0])
        return render_template("home.html" , pseudo=pseudo, compteurtues=compteurtues , listevaincus=listevaincus)

if __name__== "__main__":
     app.run(debug=True, host='0.0.0.0', port=8001)       
