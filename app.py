from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            operation_symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            operation_symbol = '-'
        elif operation == 'multiply':
            result = num1 * num2
            operation_symbol = 'x'
        elif operation == 'divide':
            if num2 == 0:
                return "Cannot divide by zero!"
            result = num1 / num2
            operation_symbol = '/'

        return render_template('result.html', num1=num1, num2=num2, operation_symbol=operation_symbol, result=result)

if __name__ == '__main__':
    app.run(debug=True)