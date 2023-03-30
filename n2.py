string0 = input()
string = ""
for x in range(0, len(string0) - 1):
    if x != 2:
        string = string + string0[x]
print(string)
print(len(string0))
if string.find("с") >= 0:
    print("+С")
