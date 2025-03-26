def ekub(a, b):
    if b == 0:
        return a
    else:
        return ekub(b, a % b)


print(ekub(18, 6))