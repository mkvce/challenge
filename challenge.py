def calculate_sum_of_multiples(max_num: int, *args):
    s = 0
    for x in range(max_num):
        reminders = [x % arg for arg in args]
        if not all(reminders):
            s += x
    return s

def main():
    print(calculate_sum_of_multiples(1000, 3, 5))

if __name__ == '__main__':
    main()