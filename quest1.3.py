def permutation(str1, str2):
    if len(str1)!=len(str2):
        return False
    else:
        count1=[0]*256
        count2=[0]*256

        for c in str1:
            count1[ord(c)] = count1[ord(c)]+1

        for c in str2:
            count2[ord(c)] = count2[ord(c)]+1

        for i in range(0,256):
            if count1[i] != count2[i]:
                return False

        return True

print permutation("prajwal","lawajrp")