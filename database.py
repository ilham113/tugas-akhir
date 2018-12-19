def option():
	print ("1. masukkan data baru ")
	print ("2. melihat data ")
	print ("3. exit ")
	pilihan=int(input("masukkan pilihan anda: "))
	print ("\n")
	return pilihan

pilihan=0
while (pilihan<3):
	pilihan=option()
	if (pilihan==3 | pilihan==0):
		break
	elif(pilihan==1):
		print ("Selamat datang di Program Biodata")
		print ("=================================")
		nama = input("Nama: ")
		tanggal_lahir= input("tanggal lahir: ")
		asal_daerah = input("asal daerah: ")
		teks = ("{}\nnama: {}\ntanggal_lahir: {}\nAlamat: {}\n---".format(nama, tanggal_lahir, asal_daerah))
		file_bio = open("database.txt", "a")
		file_bio.write(teks)
		file_bio.close()
		print ("\n")
	elif(pilihan==2):
		database=open("database.txt", "r")
		data=database.read()
		print (data)
		database.close()
		print ("\n")
