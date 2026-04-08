class User:
    def __init__(self,name):
        self.name = name


class Movie:
    def __init__(self,name,available_seats):
        self.name = name
        self.available_seats = available_seats


# class Booking:
#     def __init__(self):
#         self.seats_booked = []

#     def book_ticket(self,user,movie,seats):
#         if seats <= movie.available_seats:
#             movie.available_seats -= seats
#             self.seats_booked.append({user.name:[movie.name,seats]})
#             print("Booked movie successfully")
        
#         else:
#             print("Not enough seats available")

#     def print_booked(self):
#         data = self.seats_booked
#         for booked in data:
#             for k,v in booked.items():
#                 print(f"{k} has booked {v[0]} with {v[1]} seats")
class Booking:
    def __init__(self,user,movie,seats):
        self.user = user
        self.movie = movie
        self.seats =seats

    def get_details(self):
        return {
            "user": self.user.name,
            "movie": self.movie.name,
            "seats": self.seats
        }
        
def book_ticket(user,movie, seats):
    if seats <= movie.available_seats:
        movie.available_seats -= seats
        booking = Booking(user,movie,seats)
        return {
            "status": "success",
            "data": booking.get_details()
        }
    else:
        return {
            "status": "error",
            "message": "Not enough seats available"
        }


if __name__ == '__main__':
    user1 = User("Armaan")
    mv1 = Movie("Avengers",20)
    # bk = Booking()
    response = book_ticket(user1,mv1,5)

    print(response)
