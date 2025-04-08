def mean(arr):
    """Calculate the mean of a list of numbers."""
    return sum(arr) / len(arr)

def sumOfSquare(arr):
    """Calculate the sum of squares of a list of numbers."""
    return sum(pow(x, 2) for x in arr)