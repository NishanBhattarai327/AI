# WAP to ask for a sentence and calculate the frequency of characters in the sentences.

def freq_dict(sen):
    freq = {}
    for char in sen:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def main():
    sen = input('Enter your sentence: \n')
    print(freq_dict(sen))

if __name__ == '__main__':
    main()