from database import get_connection
from report import Report

class Admin:

    def __init__(self):
        self.report = Report()

    def add_event(self, event_id, name, date, venue, seats, price):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO EVENTS
                (EVENT_ID, EVENT_NAME, EVENT_DATE, VENUE, TOTAL_SEATS, TICKET_PRICE)
                VALUES (:1, :2, TO_DATE(:3,'DD-MON-YYYY'), :4, :5, :6)
            """, (event_id, name, date, venue, seats, price))

            conn.commit()
            print("Event Added Successfully")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def view_events(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM EVENTS")
            rows = cursor.fetchall()

            if not rows:
                print("No Events Found")
                return

            for r in rows:
                print(r)

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def delete_event(self, event_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM EVENTS WHERE EVENT_ID=:1", (event_id,))
            conn.commit()

            print("Event Deleted")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def full_report(self):
        self.report.full_report()