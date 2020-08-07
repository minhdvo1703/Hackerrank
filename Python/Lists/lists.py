if __name__ == '__main__':
    N = int(raw_input())
    L = []
    for i in range(N):
        arg = raw_input()
        arg = arg.split(" ")
        if arg[0] == "insert":
            L.insert(int(arg[1]),int(arg[2]))
        elif arg[0] == "remove":
            L.remove(int(arg[1]))
        elif arg[0] == "append":
            L.append(int(arg[1]))
        elif arg[0] == "sort":
            L.sort()
        elif arg[0] == "pop":
            L.pop()
        elif arg[0] == "reverse":
            L.reverse()
        elif arg[0] == "print":
            print(L)
