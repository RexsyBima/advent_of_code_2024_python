import unittest


def subs_2num(x: int, y: int) -> int:
    out = x - y
    if out < 0:
        out = y - x
        return out
    return out


def sort_list_from_small(input_list: list) -> list:
    n = len(input_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

    return input_list

    # x = input_list[0]
    # for i in input_list:
    #     if i < x:
    #         output.append(i)
    #         x = i
    # return output
    # # return sorted(input_list)


class Test(unittest.TestCase):
    def test_sort_list_from_small(self):
        x = sort_list_from_small([4, 5, 4, 6, 6, 8])
        self.assertEqual(x, [4, 4, 5, 6, 6, 8])


def read_input(file_name: str) -> tuple[list, list]:
    list_left = []
    list_right = []
    with open(file_name, "r") as f:
        datas = f.readlines()
        for d in datas:
            input_list = [int(x.strip()) for x in d.split(" ") if x != ""]
            list_left.append(input_list[0])
            list_right.append(input_list[1])
    return (list_left, list_right)


class Solutions:
    @staticmethod
    def solution1():
        list_left, list_right = read_input("input.txt")
        list_left, list_right = (
            sort_list_from_small(list_left),
            sort_list_from_small(list_right),
        )
        output = 0
        for x, y in zip(list_left, list_right):
            out = subs_2num(x, y)
            print(out)
            output += out

        print(output)

    @staticmethod
    def solution2():
        list_left, list_right = read_input("input.txt")
        output = 0
        for i in list_left:
            x = list_right.count(i)
            i = i * x
            output += i

        print(output)

    # print([int(x.strip()) for x in data[0].split(" ") if x != ""])


if __name__ == "__main__":
    Solutions.solution1()
    Solutions.solution2()
