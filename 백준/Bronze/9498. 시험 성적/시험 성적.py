num =  int(input())
if num < 60:
    result = "F"
elif num < 70:
    result = "D"
elif num < 80:
    result = "C"
elif num < 90:
    result = "B"
else:
    result = "A"
    
print(result)