from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Thiago Valadão Coelho Aula 1 - Com Action + Heroku - https://devopslabthiago.herokuapp.com/"

if __name__ == '__main__':
    app.run()