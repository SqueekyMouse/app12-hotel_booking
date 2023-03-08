from abc import ABC,abstractmethod

class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class PdfTicket(Ticket):
    #will err out as its not implementing the abstract method
    def generate_pdf(self):
        pass

# ticket=Ticket() #TypeError: Can't instantiate abstract class Ticket with abstract method generate
# ticket=PdfTicket() #TypeError: Can't instantiate abstract class PdfTicket with abstract method generate