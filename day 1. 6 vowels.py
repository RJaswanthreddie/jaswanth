def countstrings(n, start):
    if n == 0:
        return 1
    c = 0
    for i in range(start, 5):
        c += countstrings(n - 1, i)
    return c 
def countVowelStrings(n):
    return countstrings(n, 0)
n =int(input("enter the value of n:"))
print(countVowelStrings(n))
