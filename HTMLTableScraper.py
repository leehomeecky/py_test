import requests
from bs4 import BeautifulSoup
from statistics import median, mode, variance
import random

class HTMLTableScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape_table(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        if table is not None:
            rows = table.find_all('tr')
        else:
            rows = []
        data = []
        for row in rows:
            cells = row.find_all('td')
            row_data = []
            for cell in cells:
                row_data.append(cell.text.strip())
            if row_data:
                data.append(row_data)
        return data
    
    def calculate_mean(self):
        data = self.scrape_table()
        values = [int(val) for val in data]
        mean = sum(values) / len(values)
        return mean
    
    def calculate_median(self):
        data = self.scrape_table()
        values = [int(val) for val in data]
        median_val = median(values)
        return median_val
    
    def calculate_mode(self):
        data = self.scrape_table()
        values = [int(val) for val in data]
        mode_val = mode(values)
        return mode_val
    def get_variance(self) -> float:
        color_values = [int(color.replace('#', ''), 16) for row in self.color_table for color in row]
        return variance(color_values)
    
    
def recursive_search(numbers, target):
    # Base case: if the list is empty, return False
    if not numbers:
        return False
    
    # Recursive case: check if the first element of the list is equal to the target
    # If it is, return True; otherwise, recursively search the rest of the list
    if numbers[0] == target:
        return True
    else:
        return recursive_search(numbers[1:], target)
    

def generate_binary_to_decimal():
    # Generate a random 4-digit binary number
    binary_str = "".join([random.choice("01") for _ in range(4)])

    # Convert the binary number to base 10
    decimal = int(binary_str, 2)

    # Return the results
    return (binary_str, decimal)


def fibonacci_sum(n):
    # Initialize the first two Fibonacci numbers
    fib_prev, fib_curr = 0, 1

    # Compute the sum of the first n Fibonacci numbers
    fib_sum = 0
    for i in range(n):
        fib_sum += fib_curr

        # Compute the next Fibonacci number
        fib_next = fib_prev + fib_curr

        # Update the previous two Fibonacci numbers
        fib_prev, fib_curr = fib_curr, fib_next

    return fib_sum




