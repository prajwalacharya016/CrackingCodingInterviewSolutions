def merge(lista, listb, lasta, lastb):
    mergedindex=lasta+lastb+1
    while lasta>=0 and lastb>=0:
        if lista[lasta] > listb[lastb]:
            lista[mergedindex]=lista[lasta]
            mergedindex-=1
            lasta-=1

        else:
            lista[mergedindex]=listb[lastb]
            lastb-=1
            mergedindex -= 1


    while(lastb>=0):
        lista[mergedindex]=listb[lastb]
        lastb -= 1
        mergedindex -= 1

lista=[None]*8
listb=[None]*4

lista[0]=2
lista[1]=3
lista[2]=7
lista[3]=9
listb[0]=1
listb[1]=2
listb[2]=4
listb[3]=8
merge(lista,listb,3,3)
print lista