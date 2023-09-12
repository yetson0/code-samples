# -*- coding: utf-8 -*-

# Zadanie # 1

### 1. Bazując na bibliotekach pandas (https://github.com/pandas-dev/pandas) i faker (https://github.com/joke2k/faker), a konkretnie metodzie ssn z klasy Provider dla lokalizacji pl_PL (https://github.com/joke2k/faker/blob/master/faker/providers/ssn/pl_PL/__init__.py#L33)

zaimplementuj funkcję o nazwie generate_ssns, która zwraca obiekt typu Series z liczbą rekordów określoną parametrem wejściowym funkcji oraz wartościami reprezentującymi wygenerowane losowe numery PESEL.
"""

#import bibliotek
import pandas as pd
!pip install Faker
from faker import Faker
fake = Faker('pl_PL') #preconfig to PL

def generate_ssns(x):
  data=[]
  serie=[]
  for _ in range(x):
    data.append(fake.ssn())
  serie = pd.Series(data) # create series form a list
  return serie

# check/test generate_ssns(x)
print(generate_ssns(5)) # test #1pt1

"""### 2. Zaimplementuj funkcję **generate_unique_ssns** 
(w dowolny sposób), która zwraca obiekt typu Series z *liczbą rekordów* określoną parametrem wejściowym funkcji oraz wartościami reprezentującymi wygenerowane losowe i unikalne (tylko w ramach zwracanej kolekcji) *numery PESEL właściwe dla osób o płci* (żeńska/męska) oraz *urodzonych w przedziale dat (od-do)* określonymi również parametrami wejściowymi tej funkcji. 
"""

## ATTEMPT 1:
# sposob z wykorzystaniem generatora faker: 
# generuj fake.uniqe.ssn()
# sprawdzaj czy plec odpowiednia
# sprawdzaj czy data w wskazanym zakresie
# wykonuj az do osiagniecia ilosci x

def generate_unique_ssns(x,gender,startdate,enddate):
  data=[]
  i=0
  index=0
  # for _ in range(5000): #for is alternatively faster?
  while i < x:
    ssn=fake.unique.ssn() #unique might be slower?
    ssndate=ssn[:6]
    index+=1
    # print(f'ssn: {ssn}, date: {ssndate}, {startdate} - {enddate}, {index}, collected: {i}')
 #   if int(ssndate) in range(startdate,enddate+1):
    # print ('in range') #check collection 
    if int(ssn[9])%2 == 0: # 0 - female, 1 - male
      ssngender='female'
    else:
      ssngender='male'
    a=int(ssndate) in range(startdate,enddate+1) #a condition - born in range
    b=ssngender==gender #b condition - check gender
    # c=ssn not in data #c condition - check unique, not necessasry if fake.unique method
    if a and b: # and c: # all conditions fixed
      data.append(ssn) #add to data
      i+=1 #next until x ssn's
    
  ser = pd.Series(data)
  return ser

# check/test
print(generate_unique_ssns(5,'male',900101,900119))

"""### 3. Następnie zaimplementuj wywołania funkcji generate_ssns oraz generate_unique_ssns dla 1 000, 10 000 i 100 000 rekordów, 
wskazując wybraną płeć oraz przedział dat urodzenia od 1990-01-01 do 1990-01-19. Dokonaj pomiaru i wyświetl czas trwania ich wykonania (osobno dla każdego wywołania każdej z tych dwóch funkcji). 
"""

import time
start = time.process_time()

generate_ssns(1000) # runtime sec: 0.047870907000000074 
# generate_ssns(10000) # runtime sec: 0.4046137279999975
# generate_ssns(100000) # runtime sec: 3.9226966170000033

print(time.process_time() - start)

start = time.process_time()

# skipping - too long
# generate_unique_ssns(1000,'female',900101,900119) # runtime sec: 106.73s
# generate_unique_ssns(10000,'female',900101,900119) # runtime min: 18m
# generate_unique_ssns(100000,'female',900101,900119) # runtime unknown/infinity

print(time.process_time() - start)

"""!!! generate_unique_ssns - przy duzej ilosci rekordow (>10000) algorytm zastosowany w definicji funkcji okazal sie zbyt wolny -> **potrzeba zbudowac wlasny generator**

-> generate_ssns_unique_alt(x,gender,startdate,enddate)
"""

## ATTEMPT 2:
# alternatywny generator aby przyspieszyc ->
# generate_ssns_unique_alt(x,gender,startdate,enddate)

import datetime
import random
def generate_ssns_unique_alt(x,gender,startdate,enddate):
  data=[]
  date1=datetime.date(1990,1,1)
  date2=datetime.date(1990,1,19)
  ii=0
  w="1379137913"
  # for i in range(x*3): # for is faster than while?
  while ii < x:
    if gender==1: gendernum=random.randrange(1,10,2) #odd male
    elif gender==0: gendernum=random.randrange(0,10,2) #even female
    dtime=date2-date1
    ddays=dtime.days
    randdays=random.randrange(ddays)
    randdate=date1+datetime.timedelta(days=randdays)
    # make date as peseldate
    date=str(randdate).strip()
    date=''.join(date.split('-'))
    year=int(date[:4])
    month=int(date[5:6])
    peseldate=date[2:]
    peselmonthadd=((year//100-4)%5*2)*10
    peseldate=str(int(peseldate)+(peselmonthadd)*100)
    # add numbers to pesel, add gender
    pesel=peseldate+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(gendernum)
    # make checksum, add checksum to pesel
    sum=0
    for i in range (0,10):
      sum+=int(pesel[i])*int(w[i])
    csum=(10 - sum) % 10
    pesel+=str(csum)
    # print(f'{randdate} -> {peselmonthadd}, {peseldate}, {pesel}')
    if pesel not in data: # if unique add to data
      data.append(pesel)
      ii+=1
      # if ii==x:
        # break
  ser = pd.Series(data)
  return ser

# testujemy nowy generator generate_ssns_unique_alt(x,gender,startdate,enddate)
# gender: 0 - female, 1 - male

import time
start = time.process_time()

print (generate_ssns_unique_alt(1000,0,(1990,1,1),(1990,1,19))) # runtime sec: 0.034789508999978125
# print (generate_ssns_unique_alt(10000,0,(1990,1,1),(1990,1,19))) # runtime sec: 1.3865384519999964
# print (generate_ssns_unique_alt(95000,0,(1990,1,1),(1990,1,19))) # runtime unknown/infinity

print(time.process_time() - start)

"""ponad 1000 krotne przyspieszenie !"""

# UWAGA - PESEL ::
# 19days x 1000 possible digits (ZZZ) x 5 possible digits (one gender) = 95 000 records !

# maksymalna mozliwosc to wygenerowanie 95 000 rekordow w przedziale 19 dni dla jednej płci.

"""dla ostatniego podpunktu tj. 100 000 rekordow -> /95 000 (maks) rekordow/

najlepiej zbudowac inny algorytm generatora -- **generator wszystkich mozliwych rekordow**, ktory buduje pelna baze numerow pesel a nastepnie losuje sposrod nich wskazana ilosc x - (1000,10000,95000)
"""

## ATTEMPT 3
# budujemy dedykowany *bulk generator* wszystkich rekordow dla 19 dni, wskazanej plci
import random
def generate_ssns_unique_alt2(x,gender):
  data=[]
  csum="0"
  yymm="9001" # prefix styczen 1990
  w="1379137913"
  for dd in range(1,20): # 1 do 19
    for zzz in range(0,1000):
      for gend in range(0,10,2-gender):
        # generate pesel
        pesel=f'{yymm}{dd:02d}{zzz:03d}{gend:01d}'
        sum=0
        for i in range (0,10):
          sum+=int(pesel[i])*int(w[i])
        csum=(10 - sum) % 10
        pesel+=str(csum)
        # print(f'{pesel}')
        data.append(pesel)
  ser = pd.Series(random.sample(data,x))
  return ser

import time
start = time.process_time()

print (generate_ssns_unique_alt2(1000,0)) # runtime sec: 0.6381695619998027
# print (generate_ssns_unique_alt2(10000)) # runtime sec: 0.664998622999974
# print (generate_ssns_unique_alt2(95000)) # runtime sec: 0.8160389960003158

print(time.process_time() - start)

"""**BINGO!** wystarczajaco szybko

---
Wnioski:
1. Maksymalna ilosc PESELi dla wskazanej plci pomiedzy dniami 1 a 19 stycznia 1990 wynosi 95000; (*19 dni x 1000 mozliwych liczb z 3 cyfr (ZZZ) x 5 mozliwych cyfr dla jednej plci = 95 000*)
2. Najbardziej efektywny przy duzych ilosciach okazal sie generator: **generate_ssns_unique_alt2(x)**;
3. kod generatora moznaby optymalizowac;
4. w zaleznosci od scenatiusza warto rozwazyc rozne podejscia algorytmiczne do generatora -> przy malych zapytaniach okazal sie sprawniejszy **generate_ssns_unique_alt**;

**porownianie czasow** 

[sekundy]

| #records | generate_ssns | generate_unique_ssns | generate_ssns_unique_alt | generate_ssns_unique_alt2 |
| --- | --- | --- | --- | --- |
| 1 000 | 0.047870907000000074 | 106.73 | 0.034789508999978125 | 0.6381695619998027 |
| 10 000 | 0.4046137279999975 | 1080 | 1.3865384519999964 | 0.664998622999974 |
| 95 000 | - | too long | too long | 0.8160389960003158 |
| 100 000 | 3.9226966170000033 | n/a | n/a | n/a |

---

### 4. Zaimplementuj funkcję o nazwie validate_ssn, która na wejściu przyjmuje numer PESEL wraz z określeniem oczekiwanej płci (żeńska/męska/dowolna) i daty urodzenia (konkretna/określona lub dowolna), a na wyjściu zwraca informację o poprawności numeru PESEL. Wewnątrz funkcji zawrzyj logikę weryfikującą poprawność syntaktyczną numeru PESEL z uwzględnieniem informacji o oczekiwanej płci oraz dacie urodzenia. Następnie przetestuj działanie funkcji validate_ssn na przykładowych danych.


# wikipedia PESEL:
# Checksum calculation
# Having a PESEL in the form of ABCDEFGHIJK, one can check the validity of the number by computing the following expression:
# A×1 + B×3 + C×7 + D×9 + E×1 + F×3 + G×7 + H×9 + I×1 + J×3
# The checksum is the last digit of result of the above expression subtracted from 10. If this last digit is 0 then the checksum is 0.
# If the result of the last operation is not equal to the last digit (K) of a given PESEL, the PESEL is incorrect. This system works reliably well for catching one-digit mistakes and digit swaps

# PESEL number has the form of YYMMDDZZZXQ, where YYMMDD is the date of birth (with century encoded in month field), ZZZX is the personal identification number, where X codes sex (even number for females, odd number for males) and Q is a check digit, which is used to verify whether a given PESEL is correct or not.

#The PESEL system has been designed to **cover five centuries**. To distinguish people born in different centuries, numbers are added to the MM field:
# for birthdates between 1900 and 1999 – no change to MM field is made (see below)
# for other birthdates:
# 2000–2099 – month field number is increased by 20
# 2100–2199 – month + 40
# 2200–2299 – month + 60
# 1800–1899 – month + 80

# -----------------

def checksum(pesel): #check proper checksum for pesel numbers
	if pesel.isnumeric() and len(pesel)==11: # 11 & numbers check
	    sum=0
	    w="1379137913"
	    for i in range (0,10):
	      sum+=int(pesel[i])*int(w[i])
	    csum=(10 - sum) % 10
	    if csum==int(pesel[10]):
	        return True
	    else:
        	return False
	else:
		return False

def checkgender(gender): #check gender coded into pesel
	if gender==9: # check for any
		return True
	else:
		return int(pesel[9]) % 2 == gender # 0 - female, 1 - male

def checkdate(date): #check date given with pesel numbers, correct until 22xx 23rd century
	if date=='*': # check for any
		return True
	else:
		data=date.strip()
		date=''.join(date.split('-'))
		year=int(date[:4])
		month=int(date[5:6])
		peseldate=date[2:]
		peselmonthadd=((year//100-4)%5*2)*10
		peseldate=str(int(peseldate)+(peselmonthadd)*100)
		if peseldate == pesel[:6]:
			return True
		else:
			return False

def validate_ssn(pesel,gender,date): # main task function, gender as [0,1]
    return checksum(pesel) and checkgender(gender) and checkdate(date)

#  tests for validate_ssn(pesel,gender,date)

# [0,1,9] for gender -- 0 - female, 1 - male, 9 - any
# ["YYYY-MM-DD", "*"] for date -- * - any date

datasets=[
("93021629642",0,"1993-02-16"),
("97111435821",9,"1997-11-14"),
("97111435821",1,"1997-11-14"),
("97111435821",0,"*"),
("75050705427",1,"1975-05-07"),
("81201478022",0,"1981-10-14"),
("8a101478022",0,"*"),
] 
for dataset in datasets:
	pesel, gender, date = dataset
	print (f'Pesel:{pesel}, checksum: {checksum(pesel)}, gendercheck: {checkgender(gender)}, datecheck: {(checkdate(date))} -> SSN validation: {validate_ssn(pesel,gender,date)}')