#Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.

def reverse(string):
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])+string[0]
                       
unos= input("Unesite string:")
print(reverse(unos))
                       
