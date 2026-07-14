class student:
    
    def __init__(self , Name_f , Name_l , RollNo , RegNo , CGPA ):
        self.Name_f   = Name_f
        self.Name_l   = Name_l
        self.RollNo = RollNo
        self.RegNo  = RegNo
        self.CGPA   = CGPA
        
    def fullname(self):
        return '{} {}'.format(self.Name_f , self.Name_l)
    
person_1 = student('Parth' , 'Sonkusale' , 31 , 37 , 9)    
person_2 = student('Sagar' , 'Bhore' , 41 , 35 , 8)           
        
        
print(person_1.Name_f)