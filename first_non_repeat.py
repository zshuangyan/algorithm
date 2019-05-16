def first_non_repeat(l):
    repeat = set()
    non_repeat = dict()
    first = None
    for index, item in enumerate(l):
        if item not in repeat:
            if item in non_repeat:
                del non_repeat[item]
                repeat.add(item)
            else:
                non_repeat[item]=index

    #print("non_repeat: %s" % non_repeat)
    pos = len(l)
    result = None
    for item, index in non_repeat.items():
        if index < pos:
            result = item
            pos = index

    return result


assert first_non_repeat([3, 5, 4, 3]) == 5
assert first_non_repeat([4, 4, 5, 3]) == 5
