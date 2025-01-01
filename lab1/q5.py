# WAP to enter the marks of 10 students and display it.

def get_mark(i):
    flag = True
    while flag:
        try:
            mark = float(input(f'Enter student no. {i} mark: '))
            if mark < 0 or mark > 100:
                raise Exception("mark is outside of range (0-100)")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        return mark

def main():
    marks = []
    for i in range(1, 11):
        mark = get_mark(i)
        marks.append(mark)
    
    print('\n\n----------------- Marks -----------------')
    for i in range(0, 10):
        print(f'student no. {i+1} obtained mark: {marks[i]}')

if __name__ == '__main__':
    main()