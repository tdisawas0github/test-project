from flask import Flask, request, render_template, jsonify
import main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        result = {
            'sum': a + b,
            'difference': a - b,
            'product': a * b,
            'quotient': a / b if b != 0 else 'undefined'
        }
        return jsonify(result)
    return render_template('calculator.html')

@app.route('/pyramid', methods=['GET', 'POST'])
def pyramid():
    if request.method == 'POST':
        n = int(request.form['n'])
        result = []
        for i in range(1, n + 1):
            result.append(" " * (n - i) + "*" * (2 * i - 1))
        return jsonify(result)
    return render_template('pyramid.html')

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        n = int(request.form['n'])
        result = [0, 1]
        for _ in range(2, n):
            result.append(result[-1] + result[-2])
        return jsonify(result)
    return render_template('fibonacci.html')

@app.route('/factorial', methods=['GET', 'POST'])
def factorial():
    if request.method == 'POST':
        n = int(request.form['n'])
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return jsonify({'factorial': fact})
    return render_template('factorial.html')

@app.route('/prime', methods=['GET', 'POST'])
def prime():
    if request.method == 'POST':
        n = int(request.form['n'])
        is_prime = True
        if n <= 1:
            is_prime = False
        else:
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    is_prime = False
                    break
        return jsonify({'number': n, 'is_prime': is_prime})
    return render_template('prime.html')

@app.route('/palindrome', methods=['GET', 'POST'])
def palindrome():
    if request.method == 'POST':
        n = int(request.form['n'])
        original = n
        reversed_num = 0
        while n > 0:
            digit = n % 10
            reversed_num = reversed_num * 10 + digit
            n //= 10
        return jsonify({'number': original, 'is_palindrome': original == reversed_num})
    return render_template('palindrome.html')

@app.route('/armstrong', methods=['GET', 'POST'])
def armstrong():
    if request.method == 'POST':
        n = int(request.form['n'])
        original = n
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 3
            n //= 10
        return jsonify({'number': original, 'is_armstrong': original == total})
    return render_template('armstrong.html')

@app.route('/reverse', methods=['GET', 'POST'])
def reverse():
    if request.method == 'POST':
        n = int(request.form['n'])
        original = n
        reversed_num = 0
        while n > 0:
            digit = n % 10
            reversed_num = reversed_num * 10 + digit
            n //= 10
        return jsonify({'original': original, 'reversed': reversed_num})
    return render_template('reverse.html')

@app.route('/sort', methods=['GET', 'POST'])
def sort():
    if request.method == 'POST':
        numbers = [int(x) for x in request.form['numbers'].split(',')]
        sorted_numbers = sorted(numbers)
        return jsonify({'original': numbers, 'sorted': sorted_numbers})
    return render_template('sort.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        numbers = [int(x) for x in request.form['numbers'].split(',')]
        key = int(request.form['key'])
        search_type = request.form['search_type']
        
        if search_type == 'binary':
            numbers.sort()  # Binary search requires sorted array
            left, right = 0, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == key:
                    return jsonify({'found': True, 'index': mid, 'array': numbers})
                if numbers[mid] < key:
                    left = mid + 1
                else:
                    right = mid - 1
        else:  # linear search
            for i, val in enumerate(numbers):
                if val == key:
                    return jsonify({'found': True, 'index': i, 'array': numbers})
        
        return jsonify({'found': False, 'array': numbers})
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
