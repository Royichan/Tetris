import mysql.connector

def searchDB(username,password):
    try:
        db=mysql.connector.connect(host="localhost",user="root",password="root",db="testdatabase")
        print(db)
    except Exception:
        print("Error in connecting DB")
    if db != None:
        cursor = db.cursor(dictionary=True)
        print(cursor)
        if cursor != None:
            cursor.execute("SELECT * FROM user where username = '"+ username +"' and password = '"+ password +"';")
            myresult = cursor.fetchone()
            if myresult!= None:
                cursor.close()
                db.close()
                return True
            else:
                cursor.close()
                db.close()
                return False
    else:
        db.close()
        return False
            

def addUser(username,nickname,password):
    try:
        db=mysql.connector.connect(host="localhost",user="root",password="root",db="testdatabase")
        print(db)
    except Exception:
        print("Error in connecting DB")
    if db != None:
        cursor = db.cursor(dictionary=True)
        print(cursor)
        if cursor != None:
            cursor.execute("INSERT INTO user (password,username,nickname) VALUES(%s,%s,%s)",(password,username,nickname))
            db.commit()
            cursor.close()
            db.close()
            return True
    else:
        return False