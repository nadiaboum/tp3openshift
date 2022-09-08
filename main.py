import sys
import os


@app.route('/', methods=['GET', 'POST'])

        
def home():
    if request.form:
        compteurkill = 0
        listeVaincus = []
        pseudo = request.form['pseudo']

        monpersonnage = personnage(pseudo, 20,6,3)
        
        while monpersonnage[1] > 0:
            monstreennemi = createmob()
            gestioncombat(monpersonnage, monstreennemi)

            if monpersonnage[1] > 0:
                compteurkill = compteurennemistues(compteurkill)
                listeVaincus.append(monstreennemi[0])
        return render_template("home.html" , pseudo=pseudo, compteurkill=compteurkill , listeVaincus=list)

if __name__== "__main__":
     app.run(debug=True, host='0.0.0.0', port=8001)       
