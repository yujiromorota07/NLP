from grammer_network import check
from dictionary import dic
f = open('test.txt', 'r')
data = f.read()
list=data.split(' ')
list2=[]
for e in list:
    if e in dic:
        list2.append([e,dic[e]])
list2.insert(0,['','START'])
list2.append(['.','END'])

result=check(0,list2)
print("result :"+result)