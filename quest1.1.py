def isuniquechar(str):
    charset=[]
    if len(str)>256:
        return False
    for i in range(0,256):
        charset.append(False)
    for char in str:
        if charset[ord(char)]:
            return False

        charset[ord(char)]=True
    return True

print isuniquechar("ABCDEFGHIJKLM")