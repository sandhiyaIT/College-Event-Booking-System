from database import get_connection

class Student:

    def register(self, user_id, name, email, password):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO USERS VALUES (:1, :2, :3, :4)
            """, (user_id, name, email, password))

            conn.commit()
            print("Registration Successful")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def login(self, email, password):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT * FROM USERS
                WHERE EMAIL=:1 AND PASSWORD=:2
            """, (email, password))

            user = cursor.fetchone()

            if user:
                print("Login Successful")
                return user
            else:
                print("Invalid Login")
                return None

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def view_events(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT EVENT_ID, EVENT_NAME, EVENT_DATE, VENUE, TOTAL_SEATS, TICKET_PRICE
                FROM EVENTS
            """)

            for e in cursor.fetchall():
                print(e)

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def view_bookings(self, user_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT B.BOOKING_ID, E.EVENT_NAME, B.TICKETS
                FROM BOOKINGS B
                JOIN EVENTS E ON B.EVENT_ID = E.EVENT_ID
                WHERE B.USER_ID=:1
            """, (user_id,))

            data = cursor.fetchall()

            if not data:
                print("No bookings")
                return

            for d in data:
                print(d)

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()