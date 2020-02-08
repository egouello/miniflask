from flask import Flask, render_template,json,jsonify, request,make_response

app = Flask(__name__)

#on ouvre le fichier json contenant les donnees sauvegardees
with open('data.json') as json_file:
    data = json.load(json_file)

#la page qui affiche les donnees
@app.route('/')
def index():
    return render_template('index.html',data=data) #on affiche la page index en passant en parametre le dictionnaire json

#quand le bouton ajout est presse, cette route est declenchee
@app.route('/ajouter',methods=['POST'])
def ajouter():
    data["person"].append({"firstName":request.form['prenom'],"lastName":request.form['nom']})
    with open('data.json', 'w') as jsonfile: #on sauvegarde le dictionnaire json
        json.dump(data, jsonfile)
    return render_template('index.html',data=data) #on affiche la page index en passant en parametre le dictionnaire json

#quand le bouton supprimer est presse, cette route est declenchee
@app.route('/supprimer',methods=['POST'])
def supprimer():
    data["person"].pop(int(request.form['index'])) #on supprime l<element du  dictionnaire json
    with open('data.json', 'w') as jsonfile: #on sauvegarde le dictionnaire json
        json.dump(data, jsonfile)
    return render_template('index.html',data=data) #on affiche la page index en passant en parametre le dictionnaire json

#@app.route('/summary')
#def summary2():
#    return jsonify(data)


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

