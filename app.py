from flask import Flask, render_template_string, request

app = Flask(__name__)

# Plantilla HTML como cadena (usamos render_template_string para no crear un archivo HTML separado)
TEMPLATE_HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora Flask</title>
</head>
<body>
    <h1>Calculadora Web</h1>
    <form method="POST">
        <input type="text" name="numero1" placeholder="Primer número" required>
        <input type="text" name="numero2" placeholder="Segundo número" required>

        <select name="operacion">
            <option value="sumar">Sumar</option>
            <option value="restar">Restar</option>
            <option value="multiplicar">Multiplicar</option>
            <option value="dividir">Dividir</option>
        </select>

        <button type="submit">Calcular</button>
    </form>

    {% if resultado %}
        <h2>Resultado: {{ resultado }}</h2>
    {% endif %}
</body>
</html>
'''

def realizar_operacion(numero1, numero2, operacion):
    """
    Realiza la operación matemática seleccionada.

    Args:
        numero1 (str): Primer número como texto.
        numero2 (str): Segundo número como texto.
        operacion (str): Operación a realizar ('sumar', 'restar', 'multiplicar', 'dividir').

    Returns:
        str: Resultado de la operación o mensaje de error.
    """
    try:
        n1 = float(numero1)
        n2 = float(numero2)

        if operacion == 'sumar':
            return str(n1 + n2)
        elif operacion == 'restar':
            return str(n1 - n2)
        elif operacion == 'multiplicar':
            return str(n1 * n2)
        elif operacion == 'dividir':
            if n2 == 0:
                return "Error: No se puede dividir por cero"
            return str(n1 / n2)
        else:
            return "Error: Operación no válida"
    except ValueError:
        return "Error: Ingresa solo números válidos"

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    """
    Ruta principal que muestra la calculadora y procesa los datos del formulario.
    """
    resultado = ''
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        operacion = request.form['operacion']
        resultado = realizar_operacion(numero1, numero2, operacion)
    return render_template_string(TEMPLATE_HTML, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
