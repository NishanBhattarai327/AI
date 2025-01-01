# WAP to calculate the factorial of an input number.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def main():
    try:
        n = int(input('Enter an interger number: '))
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    print(factorial(n))

if __name__ == '__main__':
    main()