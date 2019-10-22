import os
import MySQLdb

# pip install MySQL-python==1.2.5
def app(environ, start_response):
        data = b"Hello, World!\n"
        
        db = MySQLdb.connect(
            host=os.environ["MYSQL_HOST"],
            user=os.environ["MYSQL_USER"],
            passwd=os.environ["MYSQL_PASSWORD"],
            db="mysql",
        )
        
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user")
        db.close()

        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
