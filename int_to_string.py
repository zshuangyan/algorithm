import string
char_space = string.ascii_letters
decimal = len(char_space)

def int_to_char(n):
    return chr(n + ord("A"))

def char_to_int(c):
    return ord(c) - ord("A")

def num_to_string(num: int) -> string:
    result = []
    while num:
        value, num = num % decimal, num // decimal
        char = int_to_char(value)
        result.append(char)
    return "".join(result[::-1])


def string_to_num(s: string) -> int:
    result = 0
    total_len = len(s)
    for index, c in enumerate(s):
        result += char_to_int(c) * pow(decimal, total_len - 1 - index)
    return result


if __name__ == "__main__":
    assert num_to_string(521) == "KB"
    assert string_to_num("CD") == 107
