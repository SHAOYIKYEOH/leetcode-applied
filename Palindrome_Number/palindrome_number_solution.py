#solution
def palindrome(x:int):
    s=str(x)
    if s==s[::-1]:
        return True
    else:
        return False