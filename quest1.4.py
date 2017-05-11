#This is also kinda easy in python


def replacefunction(str):
    str = str.rstrip(" ")
    str = str.replace(" ", "%20")
    return str

print replacefunction("Mr John Smith     ")
