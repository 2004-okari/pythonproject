import math

def calculate_e():
    e_approx = 1.0  # first term
    term = 1         # counter
    previous = 0.0   # store previous value
    
    while True:
        term_value = 1 / math.factorial(term)
        e_approx += term_value
        
        # if the difference is less than 1e-8
        if abs(e_approx - previous) < 1e-8:
            break
            
        previous = e_approx
        term += 1
    
    return term, e_approx

terms_needed, e_value = calculate_e()

print(f"Number of terms needed: {terms_needed}")
print(f"Approximation of e: {e_value:.8f}")
print("Actual value of e: ~2.718281828")