import pandas

# commit: create classes n basic flow Sec41

df=pandas.read_csv('hotels.csv')

class Hotel:
    def __init__(self) -> None:
        pass
        
    def book(self): # book what? a hotel not user!!!
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self,cust_name,hotel_object) -> None:
        pass

    def generate(self):
        # content=f'Name of the customer hotel'
        # return(content)
        pass


print(df)
id=input('Enter id of the hotel: ')
hotel=Hotel(id)
if hotel.available():
    hotel.book()
    name=input('Enter your name: ')
    reservation_ticket=ReservationTicket(name,hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is not free.')