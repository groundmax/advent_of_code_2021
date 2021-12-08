def main():
    with open("input.txt") as f:
        text = f.read()
        array = [int(digit) for digit in text.splitlines()]
        size = len(array)
        i = 0
        counter = 0
        window_size = 3

        while i < size - window_size:
            idx_low_1, idx_high1 = i, i + window_size
            idx_low_2, idx_high_2 = idx_low_1 + 1, idx_high1 + 1

            previous_sum, next_sum = sum(array[idx_low_1:idx_high1]), sum(
                array[idx_low_2:idx_high_2]
            )

            if previous_sum < next_sum:
                counter += 1

            i += 1

    print(counter)


if __name__ == "__main__":
    main()
