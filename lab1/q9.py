# WAP program to sum all the items in a list.

# the list = {5, 4, 11, 13, 51}

def add(list):
    if len(list) <= 1:
        return list[0]
    return list[0] + add(list[1:])

def main():
    list = [5, 4, 11, 13, 51]
    sum = add(list)
    print(sum)

if __name__ == '__main__':
    main()