# 12)WAP to find the sum of all items in a dictionary
# Input: {'a': 100, 'b':200, 'c':300}
# Output: 600
# Input: {'x': 25, 'y':18, 'z':45}
# Output: 88

def sum(dict):
    total = 0
    for key in dict:
        total += dict[key]
    return total

def main():
    dict = {'a': 100, 'b':200, 'c':300}
    print(sum(dict))
    dict = {'x': 25, 'y':18, 'z':45}
    print(sum(dict))

if __name__ == '__main__':
    main()