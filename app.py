from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    