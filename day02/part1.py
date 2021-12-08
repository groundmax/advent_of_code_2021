def main():
    with open("input.txt", "r") as f:
        text = f.read()
        binaries = [string for string in text.splitlines()]

        hash_map = {i: {} for i in range(len(binaries[0]))}

        for binary in binaries:
            for i, bit in enumerate(binary):
                hash_map[i][bit] = hash_map[i].get(bit, 0) + 1

        gamma_rate, epsilon_rate = "", ""

        for position, counter in hash_map.items():
            gamma_rate += max(counter, key=counter.get)
            epsilon_rate += min(counter, key=counter.get)

        print(int(gamma_rate, base=2) * int(epsilon_rate, base=2))


if __name__ == "__main__":
    main()
