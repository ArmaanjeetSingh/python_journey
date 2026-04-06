class Movie:
    def __init__(self):
        self.movie_list = {
            "Avengers":{"10:00 AM":["A1","A2","A3"]},
            "Fast & Furious":{"10:30 AM":["B1","B2"],"12:30":["A1","B1"]},
            "Spiderman":{"8:30 AM":["B1","A2"]}
        }
       

    def show_movies(self):
        print("*"*40)
        for index,movie in enumerate(self.movie_list,start=1):
            print(index," : ",movie)
        

    def view_available_seats(self):
        for movie,detail in self.movie_list.items():
            print(movie,": ",end='')
            for index,detail in enumerate(detail.items(),start=1):
                show,seats = detail
                print(show,end=' = ')
                for seat in seats:
                    print(seat,end=', ')
            print()

    def select_seats(self):
        self.show_movies()
        current_choice = input("Enter your movie choice ")
        if  current_choice not in self.movie_list:
            print("Wrong movie name")
            return 
        for index,val in enumerate(self.movie_list[current_choice].items(),start=1):
            show,seats = val
            print(f"{index} : {show} has {len(seats)} seats")
        show_choice = input("Enter your show choice ")
        if show_choice not in self.movie_list[current_choice]:
            print("Wrong show time")
        seats_list = self.movie_list[current_choice][show_choice]
        for index,seat in enumerate(seats_list,start=1):
            print(index," : ",seat)
        input_choice = int(input("Enter number of seats "))
        if 0 <= input_choice <= len(seats_list):
            booked = seats_list[:input_choice]
            
        return booked,show_choice,current_choice

            

class BookingSystem(Movie):
    def __init__(self):
        super().__init__()
        self.booked_shows = {}

    def select_seats(self):
        seats_list,show_choice,current_choice = super().select_seats()
        self.booked_shows[current_choice]=[show_choice,seats_list]

    def booked_shows_display(self):
        print(booked_shows)
        
        

        




if __name__ == "__main__":
    bs = BookingSystem()
    # bs.show_movies()
    bs.select_seats()
    bs.booked_shows_display()
