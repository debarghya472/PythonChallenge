val = input("Enter anything: ")
print(val)

if type(input("Enter anything: ")) is int:
    print("datatype is int")

# elif type(val) is str:
#     print("datatype is String")

elif type(val) is float:
    print("datatype is float")

elif type(val) is list:
    print("datatype is List")

elif type(val) is set:
    print("datatype is set")

elif type(val) is dict:
    print("datatype is dict")

elif type(val) is bool:
    print("datatype is boolean")

elif type(val) is bytes:
    print("datatype is bytes")

elif type(val) is bytearray:
    print("datatype is bytesarray")
