s = input("sentence: ")
v = ['a', 'i', 'u', 'e', 'o']
s1 = ""
for i in s:
    if i.lower() not in v:
        s1 += i

print(s1)