if __name__ == "__m5_main__":
    with open("example.txt", "w") as output_file:
        for i in range(10):
            output_file.write(f"{i}\n")
    with open("example.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.strip()
            print(line)
    with open("example.txt", "a") as output_file:
        for i in range(10, 16):
            output_file.write(f"{i}\n")