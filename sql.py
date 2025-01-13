import sqlite3

conction = sqlite3.connect('server.db')




def data_passed(name:str,age:int):
    try:
        cursor = conction.cursor()
        cursor.execute("BEGIN TRNSACTION")
        cursor.execute('''
                       CREATE TABLE ONLY IF NOT EXISTS users(
                           user_name TEXT,
                           user_age INTIGER
                       )
                       
                       
                       
                       
                       
                       
                       ''')
    except sqlite3.DatabaseError as e:
        return('Hey man you failed! : '+e)
    
    finally:
        conction.commit()
        conction.close()
        return('data saved..')

def data_shows():
    cursor = conction.cursor()
    
    cursor.execute("SELECT * FROM users")
    
    row = cursor.fetchall()
    lts = []
    for rows in row:
        its = its + row
    conction.commit()
    conction.close()
    
    
    
    
data_passed('frank',20)           
    
print(data_shows)
