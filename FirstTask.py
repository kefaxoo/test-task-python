# Дано положительное целочисленное 2-х байтное число. Нужно найти значение, которое будет, если поменять байты местами.

from InputLibrary import int_input

def main():
    value = 0
    while not 8 < len(bin(value)[2:]) <= 16:
        value = int_input("Enter a 2-byte integer: ")

    first_byte = (value >> 8) & 0xff
    second_byte = value & 0xff
    print("Integer before swapping bytes:", value)
    print("Integer after swapping bytes:", ((second_byte << 8) | first_byte))

if __name__ == "__main__":
    main()