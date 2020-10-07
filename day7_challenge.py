import json
n= int(input("Enter a number: "))

s={"1":"1"}

if(n== 1):
    print(json.dumps(s))
    exit(0)

for i in range(2,n+1):
    s.update({i:i*i})

print(json.dumps(s))