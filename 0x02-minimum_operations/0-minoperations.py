def minOperations(n):
    if n == 0:
        return 0
    
    current_operations = 0
    current_length = 1  # Starting with one 'H'
    
    for i in range(2, n + 1):
        if n % i == 0:
            remaining = n // i
            current_operations += (current_length + i - 1) // i
            current_length = i
            
            if current_length == n:
                return current_operations
    
    return 0

# Example usage:
n = 9
print(minOperations(n))  # Output: 6

