import random as r
def otsort(х):
    n = len(х)
    for j in range(0, n - 1):
        if х[j] > х[j + 1]:
            return False
    return True

def peremesh(х):
    n = len(х)
    for j in range(0, n):
        ra = r.randint(0, n - 1)
        х[j], х[ra] = х[ra], х[j]

def bogo_sort(х):
    n = len(х)
    while not otsort(х):
        peremesh(х)

def prov(x):
    try:
        s = int(x)
    except:
        return()

            

kol = 10

max_n = input("Максимальное число = ")
prov(max_n)

max_n = int(max_n)

a = [r.randint(0, max_n) for _ in range(kol)]

print(a)
bogo_sort(a)
print(a)


