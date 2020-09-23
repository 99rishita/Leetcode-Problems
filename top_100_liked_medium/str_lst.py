s = "hello word"
str1 = ''
count = 0
'''for i in range(len(s)):
    if s[i]!=' ' :
        str1 += s[i]
    else:
        str1 = ''
print(len(str1))'''

for i in range(len(s)):
    if s[i]==' ' :
        count = 0
    else:
        count += 1
print(count)
