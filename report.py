from database import get_connection

class Report:

    def total_events(self):
        self._count("EVENTS", "Total Events")

    def total_users(self):
        self._count("USERS", "Total Users")

    def total_bookings(self):
        self._count("BOOKINGS", "Total Bookings")

    def total_revenue(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT NVL(SUM(B.TICKETS * E.TICKET_PRICE),0)
                FROM BOOKINGS B
                JOIN EVENTS E ON B.EVENT_ID = E.EVENT_ID
            """)

            print("Total Revenue:", cursor.fetchone()[0])

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    def _count(self, table, label):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]

            print(f"{label} : {count}")

        except Exception as e:
            print(f"{label} : Table Missing or Error ({e})")

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    def full_report(self):
        print("\n===== REPORT =====")
        self.total_events()
        self.total_users()
        self.total_bookings()
        self.total_revenue()