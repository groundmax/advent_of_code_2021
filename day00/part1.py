def main():
    with open("input.txt") as f:
        previous = int(f.readline())
        counter = 0

        for digit in f:

            digit = int(digit)

            if digit > previous:
                counter += 1

            previous = digit

        print(counter)


if __name__ == "__main__":
    main()
