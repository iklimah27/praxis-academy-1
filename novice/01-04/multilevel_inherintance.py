# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)" 

class Orang(): # Base Class
	def __init__(self, nama): 
		self.nama = nama 
	 
	def getName(self): #untuk mendapatkan nama
		return self.nama 
 

class Usia(Orang): #Sub class
	def __init__(self, name, usia): 
		Orang.__init__(self, name) 
		self.usia = usia 

	def getAge(self): # Untuk mendapatkan usia
		return self.usia 


class Lengkap(Usia): #Turunan dari subclass
	def __init__(self, nama, usia, alamat): 
		Usia.__init__(self, nama, usia) 
		self.alamat = alamat 

	def getAddress(self): #Untuk mendapatkan alamat
		return self.alamat	 

Identitas = Lengkap("Lorem", 23, "Ipsum") #menambahkan value
print(Identitas.getName(), Identitas.getAge(), Identitas.getAddress()) #print semua data yang telah ditentukan 


