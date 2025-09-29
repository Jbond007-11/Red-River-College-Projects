from flask import Flask, render_template, request, redirect, url_for
import math

class MyMath:
    """ Math operations class that manages a list of numbers and provides methods to calculate avg and StdDev """
    """ attribute num_list (list) a list of numbers for math operations """

    def __init__(self):
        """ Initializes the MyMath class with an empty list of numbers. """
        self.num_list = []

    def add_number(self, number):
        """Adds a number to the internal num_list.
        Args: number (float): The number to add to the list."""
        self.num_list.append(number)
    
    def average(self):
        """ Calculates the mean of all numbers in the list. """
        if not self.num_list:
            return 0
        return sum(self.num_list) / len(self.num_list)
    
    def stddev(self):
        """ Calculates the sample standard deviation (uses n-1 in the denominator)"""
        if len(self.num_list) <= 1:
            return 0
        
        mean = self.average()
        squared_diffs = [(x - mean) ** 2 for x in self.num_list]
        variance = sum(squared_diffs) / (len(self.num_list) - 1)
        return math.sqrt(variance)

    def max_value(self):
        """ Returns the largest number in the list. """
        if not self.num_list:
            return 0
        return max(self.num_list)

    def get_numbers(self):
        """ Returns a copy of the current list of numbers. """
        return self.num_list.copy()
    
    def clear_numbers(self):
        """ Empties the list of numbers. """
        self.num_list = []

# Initialize Flask app
app = Flask(__name__)

# Create a global MyMath instance
calculator = MyMath()

# Define the route for the home page (calculator)
@app.route('/')
def home():
    """Renders the calculator home page."""
    return render_template('index.html', numbers=calculator.get_numbers())

# Route to handle number input
@app.route('/add_numbers', methods=['POST'])
def add_numbers():
    """Process user input of numbers."""
    numbers_input = request.form['numbers']
    
    # Clear previous numbers
    calculator.clear_numbers()
    
    # Parse the input aka comma-separated numbers
    try:
        numbers = [float(x.strip()) for x in numbers_input.split(',') if x.strip()]
        for num in numbers:
            calculator.add_number(num)
    except ValueError:
        return render_template('index.html', 
                             numbers=calculator.get_numbers(), 
                             error="Please enter valid numbers separated by commas")
    
    return redirect(url_for('home'))

# Route to calculate and display results
@app.route('/calculate')
def calculate():
    """Calculate and display results."""
    if len(calculator.get_numbers()) == 0:
        return render_template('index.html', 
                             numbers=calculator.get_numbers(), 
                             error="Please enter some numbers first")
    
    results = {
        'numbers': calculator.get_numbers(),
        'max': calculator.max_value(),
        'average': calculator.average(),
        'stddev': calculator.stddev()
    }
    
    return render_template('results.html', results=results)

# Route to clear numbers
@app.route('/clear')
def clear():
    """Clear all numbers and return to home."""
    calculator.clear_numbers()
    return redirect(url_for('home'))

# Runs the app
if __name__ == '__main__':
    # The debug=True argument allows to see changes without restarting the server
    app.run(debug=True, host='0.0.0.0', port=5000)