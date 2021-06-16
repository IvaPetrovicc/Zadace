import re

regexmail = "(^[a-z]+)[.]([a-z]+)([@]fpmoz[.]sum[.]ba$)"

while 1:
           unos = input("Unesi mail: ")
           podudaranje = re.match(regexmail,unos)
           if podudaranje:
                      print("Uspješno ste unijeli vašu e-mail adresu!")
                      grupe = podudaranje.groups()
                      break
           else:
                      print("Format se ne podudara, unesite ponovo!")

prvoslimena = grupe[0][0]
pr = grupe[1]

regexeduid = "^"+prvoslimena+pr+"(\d*@sum.ba$)"

while 1:
           unos2 = input("Unesi eduid: ")
           match = re.match(regexeduid, unos2)
           if match:
                      print("Uspješno ste unijeli vaš eduid!")
                      break
           else:
                      print("Format se ne podudara, unesite ponovo!")
