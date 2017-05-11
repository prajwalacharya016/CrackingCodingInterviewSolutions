#join O(n) compared to String concatenation O(n^2)

def countcompression(mystr):
    last=mystr[0]
    size=0
    count=1

    for char in mystr:
        if char==last:
            count+=1
        else:
            last =char
            size = size+1+len(str(count))
            count = 1

    size=size+1+len(str(count))
    return size

def compression(mystr):
    size=countcompression(mystr)
    if size >= len(mystr):
        return mystr

    last = mystr[0]
    count = 1
    retstr=""
    for char in mystr[1:]:
        if char==last:
            count+=1
        else:
            retstr = ''.join([retstr,last])
            retstr = ''.join([retstr,str(count)])
            last=char
            count=1

    retstr = ''.join([retstr, last])
    retstr = ''.join([retstr, str(count)])
    return retstr

print compression("aabcccccaaa")