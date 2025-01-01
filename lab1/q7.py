# WAP to ask for a sentence and count the number of words.
import string

def main():
    sen = input('Enter your sentence: \n')
    words = [word for word in sen.split() if bool(word.strip(string.punctuation))]
    print(len(words))

if __name__ == '__main__':
    main()