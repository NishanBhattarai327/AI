# WAP to check if an input number is odd or even

def main():
    try:
        num = int(input("Enter a number: "))
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    if num % 2 == 0:
        print("Even")
    else: 
        print("Odd")

if __name__ == '__main__':
    main()