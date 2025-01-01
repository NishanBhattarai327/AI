# WAP to sort the list {5, 4, 11, 13, 51}

def insertion_sort(list):
    i = 1
    while i < len(list):
        j = i
        while j > 0 and list[j-1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]   # Swap
            j -= 1
        i += 1

def main():
    list = [5, 4, 11, 13, 51]
    insertion_sort(list)
    print(list)

if __name__ == '__main__':
    main()