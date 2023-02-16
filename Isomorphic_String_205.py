# s = "egg"
# t = "add"

# s = "foo"
# t = "bar"

# s = "paper"
# t = "title"

s = "badc"
t = "baba"

countS1 = 0
countT1 = 0

# for i in s:
#     for j in t:
#         if s.count() == j.count():
#             print("true")
#         else:
#             print("false")

for i in s:
    countS1 = s.count(i)
    
for j in t:
    countT1 = t.count(j)
    
if countS1 == countT1:
    print("true")
else:
    print("false")

# # count S
# countS = 0;
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         countS += 1        
# print(countS)


# # count T
# countT = 0;
# for i in range(len(t)-1):
#     if t[i] == t[i+1]:
#         countT += 1
# print(countT)


# if countS == countT:
#     print("true")
# else:
#     print("false")
