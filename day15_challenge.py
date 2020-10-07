fo = open('file.txt','r')

str1=fo.read(1000)

print(str1)

fo.close()

count=0
st = str1.split()

for i in st:
    if i=='the':
        count=count+1

print('Number of the found = ',count)