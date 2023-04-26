def test():
    assert (add("") == 0), "'' doesn't return 0"
    assert (add("1") == 1), "'1' doesn't return 1"
    assert (add("1,2") == 3), "'1,2' doesn't return 3"
    print("Yes Passed!!!")


def add(string):
    if len(string) == 0:
        return 0
    elif len(string) == 1:
        return int(string)
    else:
        numList = string.split(",")
        result = 0
        for strnum in numList:
            result += int(strnum)
        return result


test()
