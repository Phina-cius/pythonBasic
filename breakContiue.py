#the break statement

num=0

while num < 20:
    print(num)
    if num==15:
        break
    num+=1

#continue statement

#list
device=['laptop','phone','cell-phone']
for n in device:
    if n=='laptop':
        continue
    print(n)
