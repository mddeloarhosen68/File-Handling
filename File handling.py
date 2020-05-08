
f = open('IMG_1010.JPG.jpg', 'rb')

f1 = open('MyPic', 'wb')

for i in f:
    f1.write(i)


"""
file = open('MyData','r')
file1 = open('abc','w')


for data in file:
    print(data,end="")

for data in file:
    file1.write(data)
file1.write("Computer")
print(file.readline(),end="")
print(file.readline())"""