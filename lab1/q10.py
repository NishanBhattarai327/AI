# WAP program to get the largest number from a list.

# the list {5, 4, 11, 13, 51}

def largest(list):
    max = list[0]
    for elem in list:
        if elem > max:
            max = elem
    return max

def main():
    list = [5, 4, 11, 13, 51]
    max = largest(list)
    print(max)

if __name__ == '__main__':
    main()