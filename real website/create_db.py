import sqlite3
def create_db():
    con=sqlite3.connect(database=r'Final Project.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Members(MembersID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Gender text,Age text,Contact text,Email text,Password text)")
    con.commit() 
create_db()