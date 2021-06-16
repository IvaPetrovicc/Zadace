#Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.

def parni(n):
    for i in range(n):
        if i % 2==0:
            yield i

def  neparni(n):
    for i in range(n):
        if i %2 !=0:
            yield i

broj=int(input("Unesite parametar:"))

print("Parni:")
for i in parni(broj):
    print(i)
print("Neparni:")
for i in neparni(broj):
    print(i)




