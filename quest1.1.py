def isuniquechar(mystr):
    charset=[]
    if len(mystr)>256:
        return False
    for i in range(0,256):
        charset.append(False)
    for char in mystr:
        if charset[ord(char)]:
            return False

        charset[ord(char)]=True
    return True

print isuniquechar("ABCDEFGAHIJKLM")