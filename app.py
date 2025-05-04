# Importar las funciones necesarias de la librería Flask
from flask import Flask, render_template_string, request

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Plantilla HTML como cadena (usamos render_template_string para no crear un archivo HTML separado)
TEMPLATE_HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora Flask</title>
    <style>
        /* Estilos generales */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            transition: background-color 0.5s, color 0.5s;
        }

        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #fff;
        }

        h1 {
            margin-top: 20px;
        }

        .calc-container {
            display: grid;
            grid-template-columns: repeat(4, 100px);
            gap: 10px;
            margin: 20px;
        }

        button {
            padding: 20px;
            font-size: 20px;
            cursor: pointer;
            border-radius: 8px;
            border: none;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #ddd;
        }

        input[type="text"] {
            width: 260px;
            height: 50px;
            font-size: 24px;
            text-align: right;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            margin-bottom: 20px;
        }

        .switch-mode-btn {
            padding: 10px 20px;
            font-size: 18px;
            cursor: pointer;
            background-color: #2c3e50;
            color: white;
            border: none;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        /* Modo Oscuro */
        body.dark-mode {
            background-color: #2c3e50;
            color: white;
        }

        .dark-mode button {
            background-color: #34495e;
            color: white;
        }

        .dark-mode button:hover {
            background-color: #1abc9c;
        }

        .dark-mode input[type="text"] {
            background-color: #34495e;
            color: white;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <button class="switch-mode-btn" onclick="toggleDarkMode()">Cambiar Modo</button>
        <h1>Calculadora Web</h1>
        <form method="POST">
            <input type="text" name="resultado" id="resultado" value="{{ resultado }}" disabled>
        </form>

        <div class="calc-container">
            <button onclick="insertar('7')">7</button>
            <button onclick="insertar('8')">8</button>
            <button onclick="insertar('9')">9</button>
            <button onclick="operacion('sumar')">+</button>
            <button onclick="insertar('4')">4</button>
            <button onclick="insertar('5')">5</button>
            <button onclick="insertar('6')">6</button>
            <button onclick="operacion('restar')">-</button>
            <button onclick="insertar('1')">1</button>
            <button onclick="insertar('2')">2</button>
            <button onclick="insertar('3')">3</button>
            <button onclick="operacion('multiplicar')">*</button>
            <button onclick="insertar('0')">0</button>
            <button onclick="insertar('.')">.</button>
            <button onclick="limpiar()">C</button>
            <button onclick="operacion('dividir')">/</button>
        </div>
        <button onclick="calcular()">Calcular</button>
    </div>

    <script>
        let operacionActual = '';
        let numeroActual = '';
        let resultado = '';

        function insertar(valor) {
            numeroActual += valor;
            document.getElementById('resultado').value = numeroActual;
        }

        function operacion(op) {
            if (numeroActual !== '') {
                operacionActual = op;
                resultado = numeroActual;
                numeroActual = '';
            }
        }

        function calcular() {
            if (numeroActual !== '') {
                resultado = realizarOperacion(resultado, numeroActual, operacionActual);
                document.getElementById('resultado').value = resultado;
                numeroActual = resultado;
                operacionActual = '';
            }
        }

        function limpiar() {
            numeroActual = '';
            operacionActual = '';
            resultado = '';
            document.getElementById('resultado').value = '';
        }

        function realizarOperacion(num1, num2, operacion) {
            num1 = parseFloat(num1);
            num2 = parseFloat(num2);
            switch (operacion) {
                case 'sumar':
                    return num1 + num2;
                case 'restar':
                    return num1 - num2;
                case 'multiplicar':
                    return num1 * num2;
                case 'dividir':
                    return num2 === 0 ? 'Error: Div. por cero' : num1 / num2;
                default:
                    return 'Operación no válida';
            }
        }

        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
        }
    </script>
</body>
</html>
'''
@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = ''
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        operacion = request.form['operacion']
        resultado = realizar_operacion(numero1, numero2, operacion)

    return render_template_string(TEMPLATE_HTML, resultado=resultado)

def realizar_operacion(numero1, numero2, operacion):
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

if __name__ == '__main__':
    app.run(debug=True)
