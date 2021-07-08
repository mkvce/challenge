def calculate_sum_of_multiples_old(max_num: int, *multiples)->int:
    s = 0
    for x in range(max_num):
        if not all((x % multiple for multiple in multiples)):
            s += x
    return s

def get_sum_of_multiples(max_num: int, mult: int)->int:
    if mult > max_num:
        return 0
    first_multiple = mult
    last_multiple = max_num - (max_num%mult)
    num_of_multiples = (last_multiple-first_multiple) // mult + 1
    return (first_multiple+last_multiple) * num_of_multiples // 2
    

def calculate_sum_of_multiples(max_num: int, mult1: int, mult2: int)->int:
    sum_of_mult1_multiples = get_sum_of_multiples(max_num, mult1)
    sum_of_mult2_multiples = get_sum_of_multiples(max_num, mult2)
    sum_of_common_multiples = get_sum_of_multiples(max_num, mult1 * mult2)
    return sum_of_mult1_multiples + sum_of_mult2_multiples - sum_of_common_multiples

def main():
    max_num = 999
    mult1 = 3
    mult2 = 5
    print(calculate_sum_of_multiples(max_num, mult1, mult2))

if __name__ == '__main__':
    main()