import pandas
# commit: add spa hotel shild class Sec42

df=pandas.read_csv('hotels.csv',dtype={'id':str}) # load all values as str
df_cards=pandas.read_csv('cards.csv',dtype=str).to_dict(orient='records') # load all as string
df_cards_security=pandas.read_csv('card_security.csv',dtype=str)



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



class SpaHotel(Hotel):
    def book_spa_package(self):
        pass



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



class SpaTicket:
    def __init__(self,cust_name,hotel_object) -> None:
        self.cust_name=cust_name
        self.hotel=hotel_object

    def generate(self):
        content=f"""
        Thank you for your SPA reservation!
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
        
    def hello(self):
        print('This is CC obj')



class SecureCreditCard(CreditCard): # child of CreditCard class inherits from
    def authenticate(self,given_password):
        password=df_cards_security.loc[df_cards_security['number']==self.number,
                                       'password'].squeeze()
        if password==given_password:
            return(True)
        else:
            return(False)
    
    def hello(self): # overriding parent class method, so not modifying parent class!!!
        # return super().hello()
        print('This is SecureCC obj!!!')



print(df)
hotel_ID=input('Enter id of the hotel: ')
# hotel=Hotel(hotel_ID)
hotel=SpaHotel(hotel_ID) # this is a spahotel obj which is also a hotel obj!!!

if hotel.available():
    # card_number=input('Enter cc number')
    # credit_card=CreditCard(number='1234567890123456')
    credit_card=SecureCreditCard(number='1234567890123456')
    if credit_card.validate(expiration='12/26',holder='JOHN SMITH',cvc='123'):
        if credit_card.authenticate(given_password='mypass'):
            hotel.book()
            name=input('Enter your name: ')
            reservation_ticket=ReservationTicket(cust_name=name,hotel_object=hotel)
            print(reservation_ticket.generate())

            spa_res=input('Do you want to book a spa package? (yes/no)')
            if spa_res=='yes':
                hotel.book_spa_package()
                spa_tkt=SpaTicket(cust_name=name,hotel_object=hotel)
                print(spa_tkt.generate())
        else:
            print('CC authentication failed.')
    else:
        print('There was a problem with your payment. Invalid Credit Card.')
else:
    print('Hotel is not free.')