def calculate_sum_of_multiples(max_num: int, *multiples) -> int:
    s = 0
    for x in range(max_num):
        if not all((x % multiple for multiple in multiples)):
            s += x
    return s

def main():
    print(calculate_sum_of_multiples(1000, 3, 5))

if __name__ == '__main__':
    main()