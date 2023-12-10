from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

def conectar_bd():
    client = MongoClient('localhost', 27017)
    db = client['slang_panameno']
    collection = db['palabras']
    return client, collection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_palabra():
    if request.method == 'POST':
        palabra = request.form['palabra']
        significado = request.form['significado']

        client, collection = conectar_bd()
        nueva_palabra = {
            'palabra': palabra,
            'significado': significado
        }
        collection.insert_one(nueva_palabra)
        return redirect(url_for('lista_palabras'))

    return render_template('agregar.html')

@app.route('/editar/<palabra_a_editar>', methods=['GET', 'POST'])
def editar_palabra(palabra_a_editar):
    client, collection = conectar_bd()
    palabra = collection.find_one({'palabra': palabra_a_editar})

    if request.method == 'POST':
        nueva_palabra = request.form['nueva_palabra']
        nuevo_significado = request.form['nuevo_significado']

        query = {'palabra': palabra_a_editar}
        new_values = {'$set': {'palabra': nueva_palabra, 'significado': nuevo_significado}}
        collection.update_one(query, new_values)
        return redirect(url_for('lista_palabras'))

    return render_template('editar.html', palabra=palabra)

@app.route('/eliminar/<palabra_a_eliminar>')
def eliminar_palabra(palabra_a_eliminar):
    client, collection = conectar_bd()
    collection.delete_one({'palabra': palabra_a_eliminar})
    return redirect(url_for('lista_palabras'))

@app.route('/lista')
def lista_palabras():
    client, collection = conectar_bd()
    palabras = collection.find()

    return render_template('lista.html', palabras=palabras)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_palabra():
    if request.method == 'POST':
        palabra_a_buscar = request.form['palabra_a_buscar']
        return redirect(url_for('mostrar_significado', palabra_a_buscar=palabra_a_buscar))

    return render_template('buscar.html')

@app.route('/mostrar/<palabra_a_buscar>')
def mostrar_significado(palabra_a_buscar):
    client, collection = conectar_bd()
    palabra = collection.find_one({'palabra': palabra_a_buscar})

    if palabra:
        significado = palabra['significado']
        return render_template('mostrar.html', palabra_a_buscar=palabra_a_buscar, significado=significado)
    else:
        return render_template('palabra_no_encontrada.html', palabra_a_buscar=palabra_a_buscar)

if __name__ == '__main__':
    app.run(debug=True)
