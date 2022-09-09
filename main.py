
import sys
import os

from flask import Flask, render_template, request , send_file, redirect, url_for, Response, redirect
from personnage import *
from createmob import *
from fight import *
from compteurennemistues import *

app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])


def menu():
    if request.form:
        compteurtues = 0
        listevaincus = []
        pseudo = request.form['pseudo']

        monperso = personnage(pseudo, 20,6,3)
        
        while monperso[1] > 0:
            monstreennemi = createMob()
            fight(monperso, monstreennemi)

            if monperso[1] > 0:
                compteurtues = compteurennemistues(compteurtues)
                listevaincus.append(monstreennemi[0])
        return render_template("home.html" , pseudo=pseudo, compteurtues=compteurtues , listevaincus=listevaincus)

if __name__== "__main__":
     app.run(debug=True, host='0.0.0.0', port=8001)       
