from flask import Flask, render_template, redirect, session, request
import random     #importanto el módulo random

app = Flask(__name__)
app.secret_key = 'KeeptheSecret' # establece una clave secreta

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formularios', methods=['POST'])
def formulario():
    print(request.form)

    session['name'] = request.form['nombre']
    session['local'] = request.form['localidad']
    session['fav'] = request.form['lenguaje']
    session['comments'] = request.form['comentario']

    return redirect('/resultados')

@app.route('/resultados')
def resultados():
    #print(request.form)
    return render_template('resultados.html')



if __name__=="__main__":    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración