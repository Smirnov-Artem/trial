from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Simple Calculator"

@app.route('/calc', methods=['GET'])
def calc():
    try:
        operation = request.args.get('operation')
        x = float(request.args.get('x'))
        y = float(request.args.get('y'))

        if operation == 'add':
            result = x + y
        elif operation == 'subtract':
            result = x - y
        elif operation == 'multiply':
            result = x * y
        elif operation == 'divide':
            result = x / y
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
