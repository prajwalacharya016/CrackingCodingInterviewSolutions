def stacksort(stack):
    dummystack=[]

    while stack:
        tmp=stack.pop()
        while dummystack and dummystack[-1]>tmp:
            stack.append(dummystack.pop())
        dummystack.append(tmp)

    return dummystack

stack=[1,2,8,4,3,7]
print stacksort(stack)