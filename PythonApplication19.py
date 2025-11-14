


#class Company:
  # def __init__(self,name,base_id,):
   # self.name=name                                #CompanID company deki þirketlerin temel baþlangýç ID deðeri 
    #self.base_id= base_id
                                                   #15,18,19


 


class ID:
    def __init__(self):
        self.next_ID = {}  # her base_id için NextID sayacý
        self.last_ID = {}  # her base_id için son oluþturulan ID
        self.free_ids = {}   #removed ID's storing
   
    def create_id(self, base_id):

        if base_id not in self.free_ids:
            self.free_ids[base_id]= []
        # Eðer base_id yoksa sayaç baþlat
        if base_id not in self.next_ID:
            self.next_ID[base_id] = 0
           
        

        # ID oluþtur
        if self.free_ids[base_id]:
            new_id=self.free_ids[base_id].pop(0)
        else:
            new_id = base_id + self.next_ID[base_id]
             # Sayaç artýr
        self.next_ID[base_id] += 1
        

        # Last_CompanID güncelle
        self.last_ID[base_id] = new_id

        return new_id


    def remove_id(self, base_id, Move_ID):
        if base_id not in self.free_ids:
            self.free_ids[base_id] = []

        # Silinen ID'yi free_ids'e ekle
        self.free_ids[base_id].append(Move_ID)

#class fire(Company,Employee):

#class hire(Company,Employee):


ID_system = ID()  # sýnýftan bir obje oluþturduk

class Employee:
    def __init__(self,ID_system,base_id,name,age,position,Company):
         self.name = name
         self.age = age 
         self.position = position
         self.ID_Emp = ID_system.create_id(3000)

E1 = Employee(ID_system,2000,"Ahmet",30,"Manager",[None])

#Apple = Company("Apple",2000)
#Samsung = Company("Samsung",4000)
#Valve = Company("Valve",6000)
#print(Apple)
#print(Samsung
print(E1.ID_Emp)
print(ID_system.create_id(3000))   
print(ID_system.create_id(3000))   
ID_system.remove_id(3000,3001)
print(ID_system.last_ID) 
print(ID_system.free_ids)

