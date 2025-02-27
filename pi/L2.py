mylist=['a','b','c','d','e']
listsegment=mylist[2:4]
print(mylist)
print(len(mylist))
print(type(mylist))
mylist.insert(0,'o')
print(mylist)
mylist.append('i')
print(mylist)
mylist.extend(listsegment)
print(mylist)
listadd=mylist+listsegment
print(listadd)
listbool=mylist==listsegment
print(listbool)
listbool=mylist is listsegment
print(listbool)


mytuple=(1,2,3,4,5,6)
tulpesrgment=mytuple[2:4]
print(mytuple)
print(mytuple[-1],mytuple[0])
print(len(mytuple))
print(type(mytuple))

print(mytuple+tulpesrgment)
for x in mytuple:
  mylist.append(x)
print(mylist)

print(mytuple.count(2))
print(mytuple.index(3))



thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))
print(len(thisset))
print("banana" in thisset)
thisset.add("orange")
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
thisset.update(mylist)
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("mango")
print(thisset)
thisset.clear()
print(thisset)
