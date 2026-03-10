from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/atividades")
def atividades():
    return render_template("atividades.html")

@app.route("/equipe")
def equipe():
    return render_template("equipe.html")

@app.route("/parceiros")
def parceiros():
    return render_template("parceiros.html")

@app.route("/participe")
def participe():
    return render_template("participe.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)