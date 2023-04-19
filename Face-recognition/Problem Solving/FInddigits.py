var = 0
s = str(124)
for i in range(len(s)):
    try:
        if int(s) % int(s[i]) == 0:
            var += 1
    except:
        var += 0
print(var)