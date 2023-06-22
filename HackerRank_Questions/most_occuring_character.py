#Print the three most common characters along with their occurrence count.

def findOccurance(string):
    for i in range(len(string)):
        count = 0
        for j in range(len(string)):
            if string[i]==string[j]:
                count += 1
        print("{},{}".format(string[j],count),end=" ")

string = "aabbbccde"
findOccurance(string)