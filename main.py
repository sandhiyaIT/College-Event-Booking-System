from admin import Admin
from student import Student
from booking import Booking

admin = Admin()
student = Student()
booking = Booking()

def main():

    while True:
        print("\n===== SYSTEM =====")
        print("1. Admin")
        print("2. Student")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            while True:
                print("\nADMIN MENU")
                print("1. Add Event")
                print("2. View Events")
                print("3. Delete Event")
                print("4. Report")
                print("5. Back")

                c = input("Choice: ")

                if c == "1":
                    admin.add_event(
                        int(input("ID: ")),
                        input("Name: "),
                        input("Date: "),
                        input("Venue: "),
                        int(input("Seats: ")),
                        float(input("Price: "))
                    )

                elif c == "2":
                    admin.view_events()

                elif c == "3":
                    admin.delete_event(int(input("ID: ")))

                elif c == "4":
                    admin.full_report()

                elif c == "5":
                    break

        elif choice == "2":

            while True:
                print("\nSTUDENT MENU")
                print("1. Register")
                print("2. Login")
                print("3. View Events")
                print("4. Book Ticket")
                print("5. View Bookings")
                print("6. Cancel Booking")
                print("7. Back")

                c = input("Choice: ")

                if c == "1":
                    student.register(
                        int(input("ID: ")),
                        input("Name: "),
                        input("Email: "),
                        input("Password: ")
                    )

                elif c == "2":
                    student.login(input("Email: "), input("Password: "))

                elif c == "3":
                    student.view_events()

                elif c == "4":
                    booking.book_ticket(
                        int(input("User ID: ")),
                        int(input("Event ID: ")),
                        int(input("Tickets: "))
                    )

                elif c == "5":
                    student.view_bookings(int(input("User ID: ")))

                elif c == "6":
                    booking.cancel_booking(int(input("Booking ID: ")))

                elif c == "7":
                    break

        elif choice == "3":
            print("Goodbye")
            break

if __name__ == "__main__":
    main()