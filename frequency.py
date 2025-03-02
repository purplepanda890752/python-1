dictnry = {'Codingal': 2, 'is':2, 'best':2, 'for':2, 'coding':1}

print("The original dict" + str (dictnry))

k = 2
res = 0
for key in dictnry:
    if dictnry[key]==k:
        res = res + 1
print("Frequency of K is" + str(res))