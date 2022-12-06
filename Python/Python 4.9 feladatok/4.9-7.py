def osszeg(n):
    osszeg = 0
    for i in range(1, n+1):
        osszeg = osszeg + i

    return osszeg

szam = osszeg(10)
print(szam)