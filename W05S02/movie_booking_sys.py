"""
Movie Booking System

Features:
1.	User Registration and Login:
    o	Users can register and log in to book tickets.
    o	Credentials are stored securely in memory.
2.	Movie and Show Management:
    o	Admin can add movies and show timings.
    o	Users can view available movies and their timings.
3.	Seat Booking:
    o	Users can select a movie, showtime, and book seats.
    o	Seats are dynamically updated based on availability.
4.	Booking History:
    o	Users can view their past bookings.
"""
class User:
    """
    User: 
        Handles user details, login, and registration.
    """
    user = dict()  # {username: <object of user>, username2: <obj of user 2>}
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = hash(password) # Assignment: make password a private variable and have a getter method for it
        self.booking = []

    @classmethod
    def register(cls):
        name = input("Enter the Name: ")
        username = input("Enter the Username: ")
        while username in cls.user:
            print("Username already present!")
            username = input("Enter the Username: ")
        password = input("Enter the password: ")

        cls.user[username] = User(name=name, username=username, password=password)
        print("Registration Successfull!!")
        return cls.users[username]

    @classmethod
    def login(cls):
        username = input("Enter the username: ")
        password = hash(input("Enter the password: "))
        if username in cls.user and cls.user.get(username).password == password:
            print("Login Successfull!!")
            return cls.user[username]
        print("Username or Password is incorrect!!")
        return None
        

class Movie:
    """
    Movie: 
        Stores information about movies, showtimes, and available seats.
    """
    def __init__(self, title, showtime, total_seats):
        self.title = title
        self.showtime = showtime
        self.total_seats = int(total_seats)
        self.available_seats = int(self.total_seats)
    
    def __str__(self):
        return f"Movie: {self.title} | Show Time: {self.showtime} | Seats Available: {self.available_seats}"


class Booking:
    """
    Booking: 
            Manages booking information, such as movie, user, and seat details.
    """
    def __init__(self, user, movie, seats_booked):
        self.user = user
        self.movie = movie
        self.seats_booked = seats_booked
    
    def __str__(self):
        return f"User: {self.user.name} | Movie: {self.movie.title} | Showtime: {self.movie.showtime} | " \
               f"Seats Booked:{self.seats_booked}"


class Admin:
    """
    Admin:
         Manages movie and showtime additions.
    """
    __count_intances = 0
    movies = [] # H/W change this data structure to dictionary and rewrite the menu
    def __init__(self, password):
        self.password = hash(password)
    
    def __new__(cls):
        if cls.__count_intances > 2:
            raise Exception("Cannot create more Admins!!")
        return super().__new__(cls)

    @classmethod
    def get_movies(cls):
        return cls.movies

    @classmethod
    def add_movie(cls):
        title = input("Enter the movie title: ")
        showtime = input("Enter the movie showtime: ")
        total_seats = input("Ente the total number of seats: ")
        cls.movies.append(Movie(title, showtime, total_seats))
        print("A new movie has been added!!")


def main():
    admin = Admin(password=input("Enter the admin Password!!"))

    print("!!Movie Booking System Menu!!")
    while True:
        try:
            print("\n1. Register\n2. Login\n3. Admin\n4. Logout")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                user = User.register()
            elif choice == 2:
                user = User.login()
                if user:
                    print("Movie Booking Menu!!")
                    while True:
                        print("\n1. View Movie\n2. Book Movie\n3. View Bookings\n4. Logout")
                        user_choice = int(input("Enter your choice: "))
                        if user_choice == 1:
                            if admin.get_movies():
                                for movie in admin.get_movies():
                                    print(movie)
                            else:
                                print("No Shows available!! Please come back later:(")
                        elif user_choice == 2:
                            if not admin.get_movies():
                                print("No Shows available!! Please come back later:(")
                                continue
                            movie_title = input("Enter the title of the Movie: ")
                            for movie in admin.get_movies():
                                if movie.title == movie_title:
                                    if movie.available_seats > 0:
                                        print(f"Available seats: {movie.available_seats}")
                                        seat_to_book = int(input("Enter the nuumber of seats: "))
                                        if movie.available_seats >= seat_to_book:
                                            movie.available_seats -= seat_to_book
                                            booking = Booking(user, movie, seat_to_book)
                                            user.booking.append(booking)
                                            print("Booking Successfull!!")
                                        else:
                                            print("Not Enough Seats!!")
                                    else:
                                        print("Housefull!!")
                                else:
                                    print("The Movie you have entered doesnot exists!!")
                        elif user_choice == 3:
                            if user.booking:
                                for booking in user.booking:
                                    print(booking)
                            else:
                                print("Time to book your first movie!!")
                        elif user_choice == 4:
                            print("Logging Out...")
                            break
                        else:
                            print("Enter the correct choice again!!")
                else:
                    print("Invalid credentials. Please enter again!!")
            elif choice == 3:
                admin_password = hash(input("Enter the admin password!!"))
                if admin_password == admin.password:
                    print("Welcome to the Admin Dashboard!!")
                    while True:
                        print("\n1. Add Movie\n2. View Movie\3. Logout")
                        admin_choice = int(input("Enter the choice: "))
                        if admin_choice == 1:
                            admin.add_movie()
                        elif admin_choice == 2:
                            if admin.get_movies():
                                for movie in admin.get_movies():
                                    print(movie)
                            else:
                                print("Please add new movies!!")
                        elif admin_choice == 3:
                            print("Logging out from admin...")
                            break
                        else:
                            print("You have entered incorrect choice!!")
                else:
                    print("Incorrect Admin password!!")
            elif choice == 4:
                print("Thankyou for visiting!!!")
                break
            else:
                print("Your choice in Invalid, please enter again!!")
        except:
            print("Enter only numbers!!")
main()