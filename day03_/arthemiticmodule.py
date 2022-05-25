
# print("------- welcome to arithmetic module---------------")

def addnums(num1, num2):
    print(f"num1= {num1}, num2={num2}")

    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 + num2
    else:
        res =None

    return res


# res = addnums("10",20)
# print(res)


def mulnums(num1, num2):
    print(f"num1= {num1}, num2={num2}")

    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 * num2
        return res

    return None