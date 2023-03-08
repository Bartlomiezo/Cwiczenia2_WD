# a="5,3"
# b=5
# print(a+" "+str(b))
# print(b+2)
# b+=2
# print(b)
# lista=[1 , "2", 3.5,4+5j,[2,3,4]]
# numery=[5,1,3,8,9,4,2,3,6,5]
# numery2=[5,1,3,8,9,4,2,3,6,5]
# lista.append(8) #dodaj element do listy
# lista.pop(3) #usun element z listy na danej pozycji
# lista.remove("2") #usun element z listy o danej wartosci
# lista.insert(5,[1,2,3]) #dodaj do listy element na danej pozycji
# numery.extend((6,7,8)) #dodaj sekwencje elementow do listy
# numery.sort() #sortowanie listy
# numery2.reverse() #odwracanie listy
# print(lista)
# print(numery)
# print(numery2)
# slownik = {1:"a", 2:2,3:"klucz",4:3}
# print(slownik)
# slownik["nowy"]="wartosc"
# print(slownik)
# slownik.pop(2)
# del slownik[3]
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# print("a = %(zm)d" %{"zm":12}) #formatowanie
# print("a = {}".format(12)) #formatowanie
# napis=input("wprowadz liczbe: ")
# print(type(napis))
# napis = int(napis)
# print(type(napis))

# instrukcja warunkowa
# if warunek:
# instrukcja
# elif warunek:
# instrukcja
# else:
# warunek
# a=input("podaj a: ")
# b=input("podaj b: ")
# c=input("podaj c: ")
# d=input("podaj d: ")
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if a>b:
#     print("a wieksze od b")
# elif a<b:
#     print("a jest mniejsze od b")
# else:
#     print("obie liczby sa rowne")
# if (a>b) and (c>d):
#     print("a wieksze od b i c wieksze od d")
# else:
#     print("a nie jest wieksze od b lub c nie jest wieksze od d")

# for element in sekwencja:
# instrukcje
# else:
# instrukcje po petli
# for x in range(1,6,1):
#     print(x)
# else:
#     print("koniec petli for")
# lista=[2,6,7,3,79,31,5,8]
# for i in lista:
#     print(i)
# else:
#     print("koniec pierwszsego for")
# for i in range(0, len(lista), 1):
#     print(lista[i])
# else:
#     print("koniec drugiego for")
# while warunek:
# instrukcja
# else:
# instrukcja
# licznik = 0
# while licznik != len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print("koniec petli while")
# lista2=[2,4,634,5,67,4,25,6,3]
# a=input("podaj a = ")
# a = int(a)
# licznik=0
# while licznik != len(lista2):
#     if lista2[licznik] - a == 0:
#         print(str(a)+" - "+str(lista2[licznik])+" = 0")
#     licznik+=1
lista = [1, 4, 6, 2, 2, 5, 5, 2, 56, 7, 4]
licznik = 0
while licznik != len(lista):
    if lista[licznik] == 2:
        lista.pop(licznik)
    licznik += 1
print(lista)
