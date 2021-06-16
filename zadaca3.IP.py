import re

unos = input("Unesi string: ")     

regex1 = "^i.*[0-5].*\s.*ć$"

regex2 = "\s"

podudaranje = re.search(regex1, unos)

podudaranje2 = re.search(regex2, unos)

if podudaranje and podudaranje2:
           print("podudaranje!")

else:
           print("nije pronađeno podudaranje")
