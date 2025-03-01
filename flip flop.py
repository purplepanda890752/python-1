def palindrome(r):
    e = len(r) - 1
    s = 0
    while(s < e):
        if (r[s] != r[e]):
            return False
        s += 1
        e -= 1
    return True

r = (3,7,6,4,2,8)
if(palindrome(r)):
    print("The Tuple is Flip Flop")
else:
    print("The Tuple is not Flip-Flop")