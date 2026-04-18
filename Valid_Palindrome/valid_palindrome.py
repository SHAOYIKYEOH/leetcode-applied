#solution
def valid_palindrome(s:str):
    cleaned=[]
    for x in s:
        if x.isalnumber():
            cleaned.append(x.lower())
    return cleaned == cleaned[::-1]        