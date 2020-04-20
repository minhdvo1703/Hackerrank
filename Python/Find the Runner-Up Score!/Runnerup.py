if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # use "Set" to remove the same value and sort acsending
    # then transform back to list
    arr = list(set(arr))
    
    # sort acsending values in arr
    arr = sorted(arr)
    
    #print the 2nd largest value in arr
    print(arr[len(arr)-2])
