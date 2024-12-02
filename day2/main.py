def check_if_list_increasing(input_list: list) -> bool:
    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i + 1]:
            return False
    return True


def check_if_list_decreasing(input_list: list) -> bool:
    for i in range(len(input_list) - 1):
        if input_list[i] < input_list[i + 1]:
            return False
    return True


def read_file(filename: str) -> list[list]:
    output = []
    with open(filename, "r") as file:
        for line in file:
            output.append([int(x) for x in line.split(" ")])
    return output


def test_list(x: list) -> bool:
    x_len = len(x)
    for i in range(x_len - 1):
        if x[i] == x[i + 1]:
            return False
        out = x[i] - x[i + 1]
        if out < 0:
            out = -out
        if out not in [1, 2, 3]:
            return False
    return True


def main():
    output = 0
    datas = read_file("input.txt")
    print(len(datas))
    for data in datas:
        if check_if_list_increasing(data) or check_if_list_decreasing(data):
            if test_list(data):
                output += 1
    print(output)


if __name__ == "__main__":
    main()

