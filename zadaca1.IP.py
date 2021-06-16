#Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
#Prebrojati u rječnik koliko ima kojih ocjena.
#Izračunati postotak prolaznosti. (sve ocjene veće od 1)

import random

imena=['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

ocjene={}
for ime in imena:
    ocjene[ime]= random.randint(1,5)

brojacOcj={}
brpoz= 0

for student in ocjene:
    ocjena=ocjene[student]
    if ocjena>1:
        brpoz+=1
    if ocjena in brojacOcj:
        brojacOcj[ocjena]+=1
    else:
        brojacOcj[ocjena]=1

for ocjena in brojacOcj:
    print('ocjena %d se pojavljuje %d puta' % (ocjena,brojacOcj[ocjena]))

prolaznost=(brpoz /len(ocjene))*100
print('prolaznost',prolaznost)
