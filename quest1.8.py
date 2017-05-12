def isrotation(str1, str2):
    str3 = ''.join([str1,str1])

    if str2 in str3:
        return True
    else:
        return False


print isrotation("myname", "myr")