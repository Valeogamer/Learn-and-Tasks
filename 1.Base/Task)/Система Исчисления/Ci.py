def print_formatted(n: int) -> print:
    result: str = ''
    for i in range(1, n + 1):
        print("{0:d}\t{0:o}\t{0:X}\t{0:b}".format(i))


if __name__ == '__main__':
    n: int = int(input())
    print_formatted(n)

# def print_formatted(number):
#     # your code goes here
#     width = len(bin(number)[2:])
#     for i in range(1, number+1):
#         deci = str(i)
#         octa = oct(i)[2:]
#         hexa = hex(i)[2:].upper()
#         bina = bin(i)[2:]
#         print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)
