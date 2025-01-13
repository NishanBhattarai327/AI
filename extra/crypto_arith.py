# solve the following crypto arithmetic
# problems by showing all the steps.
# BASE + BALL = GAMES

from itertools import permutations
import sys

# Function to convert a word into its numeric representation
def word_to_number(word, letter_to_digit):
    return sum(letter_to_digit[letter] * (10 ** i) for i, letter in enumerate(reversed(word)))

# Function to check if a given letter-to-digit mapping satisfies the equation
def check_solution(words, letter_to_digit):
    # Convert each word to its numeric equivalent and sum them
    total = 0
    for word in words[:-1]:  # All words except the last one (the result word)
        total += word_to_number(word, letter_to_digit)
    
    # The last word is the result
    result_word = words[-1]
    result = word_to_number(result_word, letter_to_digit)
    
    return total == result

# Generalized solution function
def solve_crypto_arithmetic(words):
    # Get all distinct letters from the words
    distinct_letters = set(''.join(words))
    
    if len(distinct_letters) > 10:
        raise ValueError("Too many distinct letters for the available digits")
    
    # Try all possible permutations of digits for the distinct letters
    for perm in permutations(range(10), len(distinct_letters)):
        letter_to_digit = dict(zip(distinct_letters, perm))
        
        # Check if the current letter-to-digit mapping satisfies the equation
        if check_solution(words, letter_to_digit):
            return letter_to_digit  # Return the valid mapping
    
    return None  # No solution found

# Example usage for BASE + BALL = GAMES
if len(sys.argv) > 2:
    words = [sys.argv[1], sys.argv[2], sys.argv[3]]
    solution = solve_crypto_arithmetic(words)

    if solution:
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
        for word in words:
            dig = ''
            for ch in word:
                dig += str(solution[ch])
            print(word + " : " + dig)
    else:
        print("No solution found")
else:
    print("Invalid input")
