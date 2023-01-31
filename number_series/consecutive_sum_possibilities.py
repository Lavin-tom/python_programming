#! /usr/bin/python3

# consecutive sum check
# return no of possibilities

def consecutiveSum(a):
    count = 0
    for i in range(1, a):
        sum = 0
        for j in range(i, a):
            sum = sum + j
            if sum == a:
                count += 1
                for k in range(i, j+1):
                    print(k, end="")
                    if k != j:
                        print(' + ', end='')
                print()
    return count


a = int(input("enter no : "))
print(f'Total possibilities: {consecutiveSum(a)}')
