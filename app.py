from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calc():
    try:
        operation = request.form['operation']
        x = float(request.form['x'])
        y = float(request.form['y'])

        if operation == 'add':
            result = x + y
        elif operation == 'subtract':
            result = x - y
        elif operation == 'multiply':
            result = x * y
        elif operation == 'divide':
            result = x / y
        else:
            return render_template('index.html', result="Invalid operation")

        return render_template('index.html', result=f"Result: {result}")
    except (TypeError, ValueError):
        return render_template('index.html', result="Invalid input")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
