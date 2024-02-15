h = 0.00000000000001
laufvariable = 2.0

alte_laufvariable = laufvariable

def rechnung ():
    result = (((alte_laufvariable.__pow__(h))-1) / h)
    return result

for i in range (1, 5):
    alte_laufvariable = laufvariable
    laufvariable = rechnung()
    if (float(laufvariable) > 0.0):
        laufvariable = laufvariable - 1.0.__pow__(-i)
    else:
        laufvariable = laufvariable -1.0.__pow__(-i)
    print(f"{rechnung()} - {alte_laufvariable}")
    