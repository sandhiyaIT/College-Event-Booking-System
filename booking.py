from database import get_connection

class Booking:

    def book_ticket(self, user_id, event_id, tickets):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT TOTAL_SEATS FROM EVENTS WHERE EVENT_ID=:1", (event_id,))
            event = cursor.fetchone()

            if not event:
                print("Event not found")
                return

            if event[0] < tickets:
                print("Not enough seats")
                return

            cursor.execute("""
                INSERT INTO BOOKINGS (USER_ID, EVENT_ID, TICKETS)
                VALUES (:1, :2, :3)
            """, (user_id, event_id, tickets))

            cursor.execute("""
                UPDATE EVENTS
                SET TOTAL_SEATS = TOTAL_SEATS - :1
                WHERE EVENT_ID=:2
            """, (tickets, event_id))

            conn.commit()
            print("Booking Successful")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def cancel_booking(self, booking_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT EVENT_ID, TICKETS FROM BOOKINGS WHERE BOOKING_ID=:1
            """, (booking_id,))

            data = cursor.fetchone()

            if not data:
                print("Booking not found")
                return

            event_id, tickets = data

            cursor.execute("DELETE FROM BOOKINGS WHERE BOOKING_ID=:1", (booking_id,))

            cursor.execute("""
                UPDATE EVENTS
                SET TOTAL_SEATS = TOTAL_SEATS + :1
                WHERE EVENT_ID=:2
            """, (tickets, event_id))

            conn.commit()
            print("Booking Cancelled")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()