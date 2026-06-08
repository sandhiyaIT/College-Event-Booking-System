import oracledb
def get_connection():
    connection = oracledb.connect(
        user="YOUR USERNAME",
        password="YOUR PASSWORD",
        dsn="localhost/XEPDB1"
    )
    return connection
from database import get_connection

conn = get_connection()

print("Database Connected")