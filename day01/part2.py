def main():
    with open('input.txt', 'r') as f:
        text = f.read()
        strings = [string for string in text.splitlines()]


        aim, depth, horizontal = 0, 0, 0

        for string in strings:
            command, digit = string.split()
            digit = int(digit)
            if command == 'forward':
                horizontal += digit
                depth += aim * digit
            elif command == 'down':
                aim += digit
            else:
                aim -= digit

        print(horizontal * depth)


if __name__ == '__main__':
    main()
