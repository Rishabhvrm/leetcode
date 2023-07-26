def addBinary(a, b):
    a, b = int(a, 2), int(b, 2)
    print(a, b)

    sum = a + b
    
    print(sum)
    print(bin(sum)[2:])

addBinary('101', '110')