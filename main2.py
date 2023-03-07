import pandas
# commit: demo: class var vs instance var Sec43

df=pandas.read_csv('hotels.csv',dtype={'id':str}) # load all values as str


class Hotel:
    watermark='The Real Estate Company' # class variable
    def __init__(self,hotel_id) -> None:
        self.hotel_id=hotel_id
        self.name=df.loc[df['id']==hotel_id,'name'].squeeze()
        pass

    def book(self): # book what? a hotel not user!!!
        """Books a hotel by changing availability to no"""
        df.loc[df['id']==self.hotel_id,'available']='no'
        df.to_csv('hotels.csv',index=False) # no need to add another column index

    def available(self):
        """Checks if the hotel is available"""
        availability=df.loc[df['id']==self.hotel_id,'available'].squeeze()
        if availability=='yes':
            return True 
        else: # not necessary as it will return None by default
            return False



class ReservationTicket:
    def __init__(self,cust_name,hotel_object) -> None:
        self.cust_name=cust_name
        self.hotel=hotel_object

    def generate(self):
        content=f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.cust_name}
        Hotel: {self.hotel.name}
        """
        return(content)


hotel1=Hotel(hotel_id='188')
hotel2=Hotel(hotel_id='134')

print(hotel1.name) # instance var
print(hotel2.name)

print(hotel1.watermark) # class var
print(hotel2.watermark)
print(Hotel.watermark)
# print(Hotel.name) # Err: AttributeError: type object 'Hotel' has no attribute 'name'