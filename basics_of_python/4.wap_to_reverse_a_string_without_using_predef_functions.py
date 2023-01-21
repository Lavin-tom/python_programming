# wap to reverse a string without predef function

word = input("enter string: ")
word = list(word)
length = 0

# to find the length of word
for i in word:
    length += 1

n=int(length/2)
m = int(length-1)

# reverse using a temp variable
for i, j in zip(range(0, n, 1), range(m, n, -1)):
    temp = word[j]
    word[j] = word[i]
    word[i] = temp

word = "".join(word)
print(word)
