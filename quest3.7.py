from linkedlist import LinkedList, Node


class Animal:
    def __init__(self):
        self.any=LinkedList()
        self.cat=LinkedList()
        self.dog=LinkedList()

    def enqueue(self, element):
        if element.__class__.__name__ == "Cat":
            self.any.insert(element)
            self.cat.insert(element)


        if element.__class__.__name__ == "Dog":
            self.any.insert(element)
            self.dog.insert(element)

    def dequeueAny(self):
        if self.any.first is None:
            return

        anyhead = self.any.first
        returnnode = anyhead

        if self.any.first is self.any.head:
            self.any.head = None
            self.cat.head = None
            self.dog.head = None

        self.any.first=self.any.first.get_next()

        if returnnode.get_data().__class__.__name__=="Cat":
            if self.cat.first is self.cat.head:
                self.cat.head = None
            self.cat.first = self.cat.first.get_next()

        if returnnode.get_data().__class__.__name__=="Dog":
            if self.dog.first is self.dog.head:
                self.dog.head = None
            self.dog.first = self.dog.first.get_next()

        return returnnode.data

    def dequeuecat(self):
        if self.cat.first is None:
            return
        anyhead = self.any.first
        returnnode = self.cat.first
        if self.cat.first is self.cat.head:
            self.cat.head = None

        self.cat.first= self.cat.first.get_next()
        while True:
            if anyhead.get_next() is None:
                break

            if anyhead.get_next().get_data().__class__.__name__=="Cat":
                if anyhead.get_next() is self.any.head:
                    self.any.head = anyhead.get_next().get_next()
                anyhead.set_next(anyhead.get_next().get_next())
                break

            if self.any.first.get_data().__class__.__name__=="Cat":
                if self.any.first is self.any.head:
                    self.any.head = None
                self.any.first = self.any.first.get_next()
                break

            anyhead = anyhead.get_next()

        return returnnode.data

    def dequeueDog(self):
        if self.dog.first is None:
            return
        anyhead = self.any.first
        returnnode = self.dog.first
        if self.dog.first is self.dog.head:
            self.dog.head = None
        self.dog.first = self.dog.first.get_next()
        while True:
            if anyhead.get_next() is None:
                break

            if anyhead.get_next().get_data().__class__.__name__ == "Dog":
                if anyhead.get_next() is self.any.head:
                    self.any.head = anyhead
                anyhead.set_next(anyhead.get_next().get_next())
                break

            if self.any.first.get_data().__class__.__name__ == "Dog":
                if self.any.first is self.any.head:
                    self.any.head = None
                self.any.first = self.any.first.get_next()
                break

            anyhead = anyhead.get_next()

        return returnnode.data

class Cat:
    def __init__(self,cstr):
        self.data=cstr


class Dog:
    def __init__(self, dstr):
        self.data = dstr

cat1=Cat("C1")
cat2=Cat("C2")
cat3=Cat("C3")
cat4=Cat("C4")
cat5=Cat("C5")
cat6=Cat("C6")
cat7=Cat("C7")
cat8=Cat("C8")

dog1=Dog("D1")
dog2=Dog("D2")
dog3=Dog("D3")
dog4=Dog("D4")
dog5=Dog("D5")
dog6=Dog("D6")

a=Animal()
a.enqueue(cat1)
a.enqueue(cat2)
a.enqueue(dog1)
a.enqueue(cat3)
a.enqueue(cat4)
a.enqueue(dog2)

a.dequeueAny()
a.dequeuecat()
a.dequeuecat()
a.dequeueAny()
a.dequeueDog()
a.dequeueDog()
a.dequeueDog()
a.dequeueDog()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.enqueue(cat3)
a.enqueue(cat1)
a.enqueue(cat2)
a.enqueue(dog1)
a.enqueue(cat3)
a.enqueue(cat4)
a.enqueue(dog2)
a.dequeueAny()
a.any.printlist()