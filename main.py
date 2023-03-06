import pandas
# commit: impl Res class functions Sec41

df=pandas.read_csv('hotels.csv',dtype={'id':str}) # load all values as str


class Hotel:
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
        else:
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
        


print(df)
hotel_ID=input('Enter id of the hotel: ')
hotel=Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name=input('Enter your name: ')
    reservation_ticket=ReservationTicket(cust_name=name,hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is not free.')