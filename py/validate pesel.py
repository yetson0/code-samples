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

def checksum(pesel):
	if pesel.isnumeric() and len(pesel)==11: # 11 numbers check
	    sum=0
	    w="1379137913"
	    for i in range (0,10):
	      sum+=int(pesel[i])*int(w[i])
	    csum=(10 - sum) % 10
	    # print('checksum: '+str(csum))
	    if csum==int(pesel[10]):
	        return True
	    else:
        	return False
	else:
		return False

def checkgender(gender):
	# if int(pesel[9]) % 2 == gender:
		# print('male') 
	return int(pesel[9]) % 2 == gender # 0 - female, 1 - male

def checkdate(date): #correct until 22xx 23rd century
	data=date.strip()
	date=''.join(date.split('-'))
	year=int(date[:4])
	month=int(date[5:6])
	peseldate=date[2:]
	peselmonthadd=((year//100-4)%5*2)*10
	peseldate=str(int(peseldate)+(peselmonthadd)*100)
	# print(f'{date} -> {peseldate}, {peselmonthadd}')
	# print(peseldate, pesel[:6])
	if peseldate == pesel[:6]:
		return True
	else:
		return False

def validate_ssn(pesel,gender,date): # 0 - female, 1 - male
    return checksum(pesel) and checkgender(gender) and checkdate(date)

datasets=[
("93021629642",0,"1993-02-16"),
("97111435821",0,"1997-11-14"),
("75050705427",1,"1975-05-07"),
("81101478022",0,"1981-10-14"),
("8a101478022",0,"1981-10-14"),
] # 0 - female, 1 - male
for dataset in datasets:
	pesel, gender, date = dataset
	print (f'Pesel:{pesel}, checksum:{checksum(pesel)}, gendercheck:{checkgender(gender)}, datecheck:{bool(checkdate(date))} -> SSN validation: {validate_ssn(pesel,gender,date)}')
