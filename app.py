from flask import Flask, request, jsonify
import math
import os


app = Flask(__name__)

# Enable CORS
from flask import Flask, request, jsonify
import math
import os

app = Flask(__name__)

# Enable CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Helper functions
def is_prime(n):
    if n <= 1:  # Prime numbers are only positive integers greater than 1
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:  # Perfect numbers are only positive integers
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    if n < 0:  # Armstrong numbers should be treated as non-negative
        return False
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum([d ** length for d in digits]) == n

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))  # Consider absolute value for digit sum

def get_fun_fact(n):
    if is_armstrong(n):
        return f"{n} is an Armstrong number because {' + '.join([f'{d}^{len(str(n))}' for d in str(n)])} = {n}"
    return f"{n} is a fascinating number!"

# API endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get the 'number' from query parameters
    number = request.args.get('number')

    # Check if the 'number' parameter is missing
    if not number:
        return jsonify({"error": True, "message": "Missing 'number' parameter"}), 400

    # Try to handle both integer and floating-point numbers
    try:
        # Check if the number can be converted to a float
        number = float(number)
    except ValueError:
        # If conversion fails, it's an invalid number
        return jsonify({"number": number, "error": True, "message": "Invalid input"}), 400

    # Initialize the list to store the properties
    properties = []

    # Check if the number is Armstrong, prime, even, or odd
    if number.is_integer():
        number = int(number)  # Convert to integer for further checks

        # Check Armstrong, prime, even, or odd for integers
        if is_armstrong(number):
            properties.append("armstrong")
        if is_prime(number):
            properties.append("prime")
        if is_perfect(number):
            properties.append("perfect")
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        # Prepare the response
        response = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": get_fun_fact(number)
        }
    else:
        # For non-integer numbers (float), only the digit sum and fun fact can be returned
        response = {
            "number": number,
            "properties": ["not_integer"],
            "digit_sum": digit_sum(int(abs(number))),  # Consider absolute value of float for digit sum
            "fun_fact": "No Armstrong or prime check for floats."
        }

    # Return the JSON response
    return jsonify(response), 200

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Number Classification API!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
