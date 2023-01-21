# wap to check the string is palindrome or not

# word = "malayalam"
word = input("enter string ")
word = list(word)
length = 0
count = 0

# to find the length of word
for i in word:
    length += 1

n=int(length/2)
m = int(length-1)

for i, j in zip(range(0, n, 1), range(m, n, -1)):
    if word[i] == word[j]:
        count += 1

word = "".join(word)

if count == n:
    print(word + " is palindrome")
else:
    print(word +" is not palindrome")
