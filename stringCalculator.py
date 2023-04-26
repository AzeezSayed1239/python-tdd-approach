def test():
    assert (add("") == 0), "'' doesn't return 0"
    assert (add("1") == 1), "'1' doesn't return 1"
    assert (add("1,2") == 3), "'1,2' doesn't return 3"
    assert (add("1,2,3,4") == 10), "'1,2,3,4' doesn't return 10"

    # test for different delimiters in string
    assert (add("1\n2,3") == 6), "'1\n2,3' doesn't return 6"
    assert (add("//;\n1;21") == 22), "'//;\n1;2' doesn't return 22"

    assert (add("1-1/;\n1;2") ==
            "negatives not allowed"), "'//;\n1;2' doesn't return 'negatives not allowed'"
    print("Yes Passed!!!")


def add(string):
    if len(string) == 0:
        return 0
    elif len(string) == 1:
        return int(string)
    else:
        result = 0
        num = ""
        for i in range(0, len(string)):
            if string[i].isdigit() and string[i-1] == "-":
                return "negatives not allowed"
            elif string[i].isdigit():
                num += string[i]
            elif string[i].isdigit() == False:
                num = "0"

            result += int(num)
        print(result)
        return result


test()
