from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculadora.html', resultado=None)

@app.route('/calcular', methods=['POST'])
def calcular():
    valor1 = float(request.form['valor1'])
    valor2 = float(request.form['valor2'])
    operacao = request.form['operacao']

    if operacao == 'soma':
        resultado = valor1 + valor2

    elif operacao == 'subtracao':
        resultado = valor1 - valor2

    elif operacao == 'multiplicacao':
        resultado = valor1 * valor2

    elif operacao == 'divisao':
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            resultado = "Erro: divisão por zero."

    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)