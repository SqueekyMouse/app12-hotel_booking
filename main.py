import pandas
# commit: add credit card class and functions Sec42

df=pandas.read_csv('hotels.csv',dtype={'id':str}) # load all values as str
df_cards=pandas.read_csv('cards.csv',dtype=str).to_dict(orient='records') # load all as string

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
        


class CreditCard:
    def __init__(self,number) -> None:
        self.number=number

    def validate(self,expiration,holder,cvc):
        card_data={'number':self.number,'expiration':expiration,
                   'cvc':cvc,'holder':holder}
        if card_data in df_cards:
            return(True)
        else: # not necessary as it will return None by default
            return(False)



print(df)
hotel_ID=input('Enter id of the hotel: ')
hotel=Hotel(hotel_ID)

if hotel.available():
    # card_number=input('Enter cc number')
    credit_card=CreditCard(number='1234567890123456')
    if credit_card.validate(expiration='12/26',holder='JOHN SMITH',cvc='123'):
        hotel.book()
        name=input('Enter your name: ')
        reservation_ticket=ReservationTicket(cust_name=name,hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print('There was a problem with your payment. Invalid Credit Card.')
else:
    print('Hotel is not free.')