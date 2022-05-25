
def askfornum(messge):
    num= input(f"please enter {messge}")
    if num.isdigit():
        num = int(num)
        return num
    return askfornum(messge)


