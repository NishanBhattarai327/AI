# You are given a string and your task is to swap cases. In other words, convert all lowercase letters
# to uppercase letters and vice versa.

def swap_case(sen):
    swaped = ''
    for char in sen:
        ascii = ord(char)
        if ascii >= ord('a') and ascii <= ord('z'):   # lower case
            ascii -= 32
        elif ascii >= ord('A') and ascii <= ord('Z'):  # upper case
            ascii += 32
        swaped += chr(ascii)
    return swaped

def main():
    sen = input('Enter your sentence: \n')
    print(swap_case(sen))

if __name__ == '__main__':
    main()