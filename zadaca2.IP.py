#Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
#Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena.
#Nedovoljan 0-49%
#Dovoljan 50-65%
#Dobar 65-80%
#Vrlodobar 80-90%
#Izvrstan 90-100%

from csv import reader
with open('rezultati.csv','r') as read_obj:
    csv_reader=reader(read_obj)
    rezultati=list(map(tuple,csv_reader))
    #print(rezultati)
    
novirezultati=[]
for ime,prezime,bodovi in rezultati:
    novirezultati.append((prezime,ime,bodovi))
novirezultati.sort()
print(novirezultati)

ocjena={'Nedovoljan':0,
        'Dovoljan':0,
        'Dobar':0,
        'Vrlo dobar':0,
        'Odlican':0
        }
for prezime,ime,bodovi in rezultati:
    if int(bodovi) < 49:
        ocjena['Nedovoljan']+= 1
    elif int(bodovi) > 50 and int(bodovi)<65:
        ocjena['Dovoljan']+= 1
    elif int(bodovi)>65 and int(bodovi)<80:
        ocjena['Dobar']+= 1
    elif int(bodovi)>80 and int(bodovi)<90:
        ocjena['Vrlo dobar']+= 1
    elif int(bodovi)>90:
        ocjena['Odlican']+= 1
    print(prezime,ime,bodovi)
    
print(ocjena)
