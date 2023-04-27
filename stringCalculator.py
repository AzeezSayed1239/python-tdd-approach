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
        lis = []
        j = 0
        while j < (len(string)):
            if string[j].isdigit() == True:
                pos = j
                l = 0
                while string[j].isdigit() == True and j < len(string):
                    j += 1
                    l += 1
                num = int(string[pos:pos+l])
                print(num)
                lis.append(num)
            j += 1
        return sum(lis)


test()
