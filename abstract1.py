from abc import ABC, abstractmethod
from datetime import datetime
from random import choice

class School_admission(ABC):

    @abstractmethod
    def got_admission(self):
        pass

class student(School_admission):

    def __init__(self,name,id):
        self.name = name
        self.id =id

class school_alumni(student):
    
    def got_admission(self):
        flag = choice([True, False])
        print(f'flag is {flag}')
        return flag

    def join_school_alumni(self):
        if self.got_admission() is True:
            self.school_alumni_id = str(self.id) + '-'+ str(datetime.now().year)
            return f'Your School Alumni Id is {self.school_alumni_id}'
            
        else:
            return ("Sorry, You could not get admission in this school")
    
school_alumni_obj = school_alumni('Prerna', 123)
print(school_alumni_obj.join_school_alumni())

