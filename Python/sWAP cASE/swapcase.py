def swap_case(s):
    new = ""
    for i in s:
        if i == i.lower():
            new += i.upper()
        else:
            new += i.lower()
    return new

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
