class User:
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id

    def display_user(self):
        print(f"{self.name} : {self.user_id}")


class Ticket:
    def __init__(self,ticket_id,event_name,price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.price = price

        self.is_booked = False
        

    def display_ticket(self):
        print(f"{self.ticket_id} {self.event_name} {self.price} {'booked' if self.is_booked else 'not booked'}")

    

class BookingSystem:
    def __init__(self):
        self.users = []
        self.tickets = []

    def add_user(self,name,user_id):
        self.users.append(User(name,user_id))

    def add_ticket(self,ticket_id,event_name,price):
        self.tickets.append(Ticket(ticket_id,event_name,price))

    def show_available_tickets(self):
        for ticket in self.tickets:
           ticket.display_ticket()

    def book_ticket(self,user_id,ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                if not ticket.is_booked == True:
                    print(f'{ticket.ticket_id} is booked')
                else:
                    print("Not available")

            else:
                print("Not found")


            

if __name__ == '__main__':
    system = BookingSystem()
    system.add_user('45','aman')
    system.add_ticket('123','plane',2300)
    system.show_available_tickets()
    system.book_ticket('45','123')