def recursion(s, l, r):
    if l >= r: 
        return 1, l+1
    elif s[l] != s[r]: 
        return 0, l+1
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

l = int(input())
input_str = []
for i in range(l):
    s = input()
    input_str.append(s)

for s in input_str:
    result = isPalindrome(s)
    print(result[0], result[1])