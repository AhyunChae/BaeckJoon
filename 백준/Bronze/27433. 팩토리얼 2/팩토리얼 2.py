def fac(n, s):
    if n > 0:
        s *= n;
        return fac(n-1, s)
    else:
        return s;


input_n = int(input())
print(fac(input_n, 1))