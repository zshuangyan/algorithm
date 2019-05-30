from hashlib import sha256


class SimHash:
    def __init__(self, length=256, hash_func=sha256):
        self.len = length
        self.hash = hash_func

    def simhash(self, word_counter):
        """
        Turn word:count dict into a vector
        """

        vector = [0 for i in range(self.len)]
        for word, count in word_counter.items():
            hex_str = self.hash(word.encode("utf-8")).hexdigest()
            binary_vec = []
            for h in hex_str:
                binary_vec.extend(hex2binary(h))

            for i in range(self.len):
                vector[i] += binary_vec[i]*count
        return [1 if i > 0 else 0 for i in vector]

    def hamming_distance(self, vec1, vec2):
        total = 0
        for i in range(self.len):
            if vec1[i] != vec2[i]:
                total += 1
        return total


def num_to_binary(num):
    """
    Turn numbers from 0 to 15 into binary vector

    >>> num_to_binary(0)
    [0, 0, 0, 0]
    >>> num_to_binary(6)
    [0, 1, 1, 0]
    >>> num_to_binary(15)
    [1, 1, 1, 1]
    """

    if type(num) != int or num > 15 or num < 0:
        raise ValueError("num: %s should less than 16 and larger than 0" % num)

    result = []
    for i in range(4):
        num, reminder = num >> 1, num % 2
        result.append(reminder)
    return result[::-1]


def hex2binary(hex):
    """
    Turn hex char to binary vector
    
    >>> hex2binary('0')
    [0, 0, 0, 0]
    >>> hex2binary('a')
    [1, 0, 1, 0]
    """

    if type(hex) != str and len(hex) != 1 or hex.lower() not in "0123456789abcdef":
        raise ValueError("hex: %s should be char" % hex)

    if hex.lower() in "abcdefg":
        return num_to_binary(10+ord(hex.lower())-ord("a"))
    else:
        return num_to_binary(int(hex))


sm = SimHash()
word_counter1 = {"我们": 1, "一家人":2}
word_counter2 = {"我们": 1, "一家人": 2}
result1 = sm.simhash(word_counter1)
result2 = sm.simhash(word_counter2)
diff = sm.hamming_distance(result1, result2)
similarity = 1 - diff/256
print(similarity)

word_counter1 = {"我们": 5, "相爱": 4, "结婚": 2, "父母": 2, "操办": 1}
word_counter2 = {"我们": 4, "在一起": 2, "结婚": 1, "父母": 2, "主持": 1}
result1 = sm.simhash(word_counter1)
result2 = sm.simhash(word_counter2)
diff = sm.hamming_distance(result1, result2)
similarity = 1 - diff/256
print(similarity)


word_counter1 = {"我": 1, "广场": 1, "放松": 1}
word_counter2 = {"我": 1, "焦虑": 1, "怀疑": 1}
result1 = sm.simhash(word_counter1)
result2 = sm.simhash(word_counter2)
diff = sm.hamming_distance(result1, result2)
similarity = 1 - diff/256
print(similarity)

word_counter1 = {"广场": 1, "放松": 1}
word_counter2 = {"焦虑": 1, "工作": 1}
result1 = sm.simhash(word_counter1)
result2 = sm.simhash(word_counter2)
diff = sm.hamming_distance(result1, result2)
similarity = 1 - diff/256
print(similarity)
