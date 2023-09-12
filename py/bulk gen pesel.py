



import random
def generate_ssns_unique_alt2(x):
	data=[]; csum="0"
	yymm="9001"
	w="1379137913"
	for dd in range(1,20):
		for zzz in range(0,1000):
			for gend in range(0,10,2):
				# generate pesel
				pesel=f'{yymm}{dd:02d}{zzz:03d}{gend:01d}'
				sum=0
				for i in range (0,10):
					sum+=int(pesel[i])*int(w[i])
				csum=(10 - sum) % 10
				pesel+=str(csum)
				# print(f'{pesel}')
				data.append(pesel)
	dataext=(random.sample(data,x))
	return dataext

print (generate_ssns_unique_alt2(3))