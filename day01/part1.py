def main():
    with open("input.txt", "r") as f:
        text = f.read()
        strings = [string for string in text.splitlines()]

        commands = {}

        for string in strings:
            command, digit = string.split()
            commands[command] = commands.get(command, 0) + int(digit)

        print(max(commands["down"] - commands["up"], 0) * commands["forward"])


if __name__ == "__main__":
    main()
