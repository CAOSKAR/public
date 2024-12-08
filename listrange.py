import copy
print(list(range (5)))
print(range (5))
for i in [0, 1, 2]:
    print(i)
    print("TEST")
print("TESTENDE")
aufzaehlung = ["h","a","l","l","o"]

for i in range(len(aufzaehlung)):
    print(i,"ist", aufzaehlung[i])
print("###################################")
for i, element in enumerate(aufzaehlung):
    print(i,"ist", element)

print("###################################")
print(1==1,2==1)
print("###################################")
ls1 =[1]
ls2 = ls1
ls3 =[2]
tp1 = (1,2,3)
ls4 = copy.deepcopy(ls1)
print(ls1 is ls2)
print(ls3 is ls2)
print(type([]) is list)
print(type(ls1) is list)
print(type(tp1))
print(type(ls1))
print("Deepcopy", ls4 is ls1)
print("Deepcopy", ls4 == ls1)
for i in range(6):
    if i < 4 or i >5:
        pass
    else:
        print(i)
ls = ["a","b","c"]
print("###################################")

for i in range(len(ls)):
    print("len ist" ,len(ls))
    print(ls[i])
    

