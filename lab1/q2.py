# WAP to input the percentage and display the division
# >=80 → Distinction
# >=65 → First Division
# >=55 → Second Division
# >=40 → Third Division
# <40 → Fail

def main():
    try:
        percentage = float(input('Enter your percentage: '))

        if percentage < 0 or percentage > 100:
            raise Exception("percentage is outside of range (0-100)")
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    if percentage >= 80:    print('Distinction')
    elif percentage >= 65:  print('First Division')
    elif percentage >= 55:  print('Second Division')
    elif percentage >= 40:  print('Third Division')
    else:                   print('Fail')

if __name__ == '__main__':
    main()