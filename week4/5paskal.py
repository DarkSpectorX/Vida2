def factorial(n):
    #Base case
    if n == 0 or n == 1:
        return 1
    #Recursion case
    return n * factorial(n - 1)

# Function to calculate binomial coefficient C(n, k)
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Function to print Pascal's Triangle using recursion
def pascal_triangle(n, current=0):
    if current == n:
        return
    
    # Print spaces for alignment
    print(" " * (n - current), end="")
    
    # Print values in the current row
    for k in range(current + 1):
        print(binomial_coefficient(current, k), end=" ")
    print()
    
    # Recursive call for the next row
    pascal_triangle(n, current + 1)

# Ask user for number of rows
rows = int(input("Enter number of rows for Pascal's Triangle: "))
pascal_triangle(rows)
