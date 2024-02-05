lista={"CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
        "LOL": "Częsta reakcja na coś zabawnego",
        "REL": "Wypowiada to osoba, która się z czymś zgadza"}
slowo=input ("Jakie słowo chcesz sprawdzić?")
if slowo in lista.keys():
    print (lista[slowo])
else:
    print ("Niestey nie posiadamy takiej informacji")
