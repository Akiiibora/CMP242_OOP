


class Company:
   def __init__ (self,name,base_id,employees):
       self.name=name                               
       self.base_id= base_id
       self.employees =employees if employees is not None else[]                                            

Apple = Company("Apple",2000,[])
Samsung = Company("Samsung",4000,[])
Valve = Company("Valve",6000,[])
companies ={"Apple":Apple,"Samsung":Samsung,"Valve": Valve}


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
ID_system = ID()  # sýnýftan bir obje oluþturduk
#class fire(Company,Employee):

    

class Employee:
    def __init__(self):
         self.name = None
         self.age = None 
         self.position = None
         self.company =None

    def hire(self,companies,ID_system):
        
         company_choice = input("which company do you want add employee? (Apple/Samsung/Valve): ")

         if company_choice not in companies:
            print("You have to choose one of this three!")
            return self.hire(companies,ID_system) 
        
            
            
         selected_company = companies[company_choice]
         self.company= selected_company
         selected_company.employees.append(self)

         self.name= input("Enter employee's name: ")
         self.age =input("Enter employee's age: ")
         self.position = input("Enter employee's position: ")
         
         self.ID_Emp =ID_system.create_id(selected_company.base_id)
         print(f"Hired as a {self.position} which is name of {self.name} hired at {selected_company.name} with ID {self.ID_Emp}")
E1= Employee()
E1.hire(companies,ID_system)

print(E1.ID_Emp)


