import pandas
from abc import ABC,abstractmethod # Abstract Base Class and decorator!!!
# commit: demo: abstract classe and method Sec43

df=pandas.read_csv('hotels.csv',dtype={'id':str}) # load all values as str

# Instance attributes - inst var and inst method
# Class attributes - class var and class method
# instance propeties - is amethod which behaves like a var
# static methods - static method and class method disctiction is blurred, usually used for stuff like conversion etc.

# magic methods - 
# python is always interaction between things like functions an dinstances and meyhods
# 'hello'=='hi' # syntactic sugar ie, simplified syntax, readable
# 'hello'.__eq__('hi') # actual stuff happening
# 1 + 2
#  1 .__add__(2)
# dir(str) see magic methods

# abstract classes and abstract methods - 
# Abstract Base Class and decorator imported from abc package!!!
# cannot instantiate abstract class
#  its role is to define a structure basically

class Hotel:
    watermark='The Real Estate Company' # class variable
    def __init__(self,hotel_id) -> None:
        self.hotel_id=hotel_id # instance variables
        self.name=df.loc[df['id']==hotel_id,'name'].squeeze()
        pass

    def book(self): # book what? a hotel not user!!!
        """Books a hotel by changing availability to no"""
        df.loc[df['id']==self.hotel_id,'available']='no'
        df.to_csv('hotels.csv',index=False) # no need to add another column index

    def available(self): # instance method
        """Checks if the hotel is available"""
        availability=df.loc[df['id']==self.hotel_id,'available'].squeeze()
        if availability=='yes':
            return True 
        else: # not necessary as it will return None by default
            return False
    
    @classmethod   # decorator to change the method to class method
    def get_hotel_count(cls,data): # cls var that holds the class obj!!!
        return(len(data))
    
    # overriding magic methods!!!
    def __eq__(self,other): # false normally, will be true once we override it to comapre just the id of the two hotel objects
        if self.hotel_id==other.hotel_id:
            return(True)
        else:
            return(False)
    
    def __add__(self,other): # hotel1+hotel2 will return sum of prices !!!!
        total=self.price+other.price
        return(total)


# Abstract class
class Ticket(ABC): # ABC - Abstract Base Class imported from abc package!!!

    @abstractmethod # imported from abc package!!!
    def generate(self): # all inheriting classes should implement this method
        pass


class ReservationTicket(Ticket): # would inherit from teh ticket class
    def __init__(self,cust_name,hotel_object) -> None:
        self.cust_name=cust_name
        self.hotel=hotel_object

    def generate(self): # using a property in here!!!
        content=f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel: {self.hotel.name}
        """
        return(content)
    
    @property # property decorator
    def the_customer_name(self): # use when it reutrns a variable but needs some processing!!
        name=self.cust_name.strip()
        name=name.title()
        return(name)
    
    @staticmethod
    def convert(amount): # no self or cls arguments, its a function so done have any reference to teh obj or class
        return(amount*1.2) # its like a utility func but related to the class purpose like usd to euro conversion
    # static method and class method disctiction is blurred, usually used for stuff like conversion etc.


class DigitalTicket(Ticket): # would inherit from the abstract class
    # since its inheriting from teh abstract class it need to implement the abstract class
    def generate(self):
        return('Hello thi sis yoyr digital ticket')
    
    def download(self):
        pass

class DigitalTicket1(ReservationTicket):
    # overriding parent class methods
    # this s not the best way, better way will be to use abstract class
    # both the parent and child class would be inheriting from teh abstract class???
    def generate(self):
        return('Hello thi sis yoyr digital ticket')
    
    def download(self):
        pass


def demo3():
    # abstract class
    # cannot instantiate abstract class
    ticket=Ticket() #TypeError: Can't instantiate abstract class Ticket with abstract method generate

def demo1():
    hotel1=Hotel(hotel_id='188')
    hotel2=Hotel(hotel_id='134')

    # instance var
    print(hotel1.name)
    print(hotel2.name)

    # class var
    print(hotel1.watermark) 
    print(hotel2.watermark)
    print(Hotel.watermark)
    # print(Hotel.name) # Err: AttributeError: type object 'Hotel' has no attribute 'name'

    # instance method
    print(hotel1.available())

    # class method
    print(Hotel.get_hotel_count(df))
    print(hotel1.get_hotel_count(df)) # this will also work, still class method

    # property
    ticket=ReservationTicket(cust_name='john smith ',hotel_object=hotel1)
    print(ticket.the_customer_name) # it behaves like a variable!!!!
    print(ticket.generate())

    # static method
    converted=ReservationTicket.convert(10)
    print(converted)


def demo2():
    # magic methods
    # from main2 import Hotel
    print(Hotel)
    print(dir(Hotel)) # has magic methods '__eq__' , '__ge__' etc

    hotel1=Hotel('188')
    hotel2=Hotel('188')
    print(hotel1==hotel2) # false normally, will be true once we override it to comapre just tahe id of the two hotel objects
    # TypeError: Hotel.__eq__() takes 1 positional argument but 2 were given