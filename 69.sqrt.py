def mySqrt(x: int) -> int:
    for i in range(x):
        print(i)
        if (i*i) > x:
            print(i * i)
            return i-1

    return None

print(mySqrt(8))
