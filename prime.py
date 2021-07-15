from math import sqrt, floor


def get_prime_numbers(first: int, last: int)->list:
    if first == 1:
        first = 2
    seq = []
    for num in range(first, last):
        for divisor in range(2, floor(sqrt(num)) + 1):
            if num % divisor == 0:
                break
        else:
            seq.append(num)
    return seq

def write_prime_numbers_in_file(first: int, last: int, file: str):
    prime_numbers = get_prime_numbers(first, last)
    with open(file, 'w') as output:
        output.write('primes:\n')
        for prime_number in prime_numbers:
            output.write(f'{prime_number}\n')

def main():
    write_prime_numbers_in_file(1, 10**6, 'out.txt')

if __name__ == '__main__':
    main()
