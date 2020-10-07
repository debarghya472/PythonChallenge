fo = open('file.txt','w')
str="Python has the least code complexity"
fo.write(str)
fo.seek(len(str))
fo.close()

fo = open('file.txt','r')

str =fo.read(100)
fo.seek(0)
print ("Reading :",str)

fo.close()