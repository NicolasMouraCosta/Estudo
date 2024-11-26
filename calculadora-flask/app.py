from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            numero1 = float(request.form.get("numero1"))
            numero2 = float(request.form.get("numero2"))
            operacao = request.form.get("operacao")
            
            if operacao == "adicao":
                resultado = numero1 + numero2
            elif operacao == "subtracao":
                resultado = numero1 - numero2
            elif operacao == "multiplicacao":
                resultado = numero1 * numero2
            elif operacao == "divisao":
                if numero2 != 0:
                    resultado = numero1 / numero2
                else:
                    resultado = "Erro: Divisão por zero!"
        except ValueError:
            resultado = "Erro: Entrada inválida!"
    
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
