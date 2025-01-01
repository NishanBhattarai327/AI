# WAP to calculate sum, diff, product and quotient between two input numbers using a single function.

def calculate(x, y):
    return x+y, x-y, x*y, x/y

def main():
    try:
        x = float(input("Enter value of x: "))
        y = float(input("Enter value of y: "))

        if y == 0:
            raise Exception("y cannot be zero (ZeroDivisionError)")
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    sum, diff, prod, quot = calculate(x, y)
    print(f'sum = {sum}, diff = {diff}, product = {prod}, and quotient = {quot}')

if __name__ == '__main__':
    main()