from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Helper functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum([d ** length for d in digits]) == n


def digit_sum(n):
    return sum(int(d) for d in str(n))


def get_fun_fact(n):
    if is_armstrong(n):
        return f"{n} is an Armstrong number because {' + '.join([f'{d}^{len(str(n))}' for d in str(n)])} = {n}"
    return f"{n} is a fascinating number!"


# API route
@app.route('/api/funnnumber', methods=['GET'])
def funnumber():
    number = request.args.get('number')

    # Validate input
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []

    # Classify number properties
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Prepare response data
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
