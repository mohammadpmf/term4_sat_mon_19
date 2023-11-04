import pymysql
def sign_up():
    query = "INSERT INTO `login_register`.`users` (`full_name`, `username`, `password`) VALUES (%s, %s, %s);"
    f = input("Full Name: ")
    u = input("Username: ")
    query2 = "SELECT * FROM `login_register`.`users` WHERE `username`=%s"
    cursor.execute(query2, u)
    data = cursor.fetchone()
    if data==None:
        p = input("Password: ")
        values = f, u, p
        cursor.execute(query, values)
        db.commit()
    else:
        print("Account already taken")
def login():
    values = input("Username: ")
    query = "SELECT * FROM `login_register`.`users` WHERE `username`=%s"
    cursor.execute(query, values)
    data = cursor.fetchone()
    if data == None:
        print("Not registerd.")
    else:
        p=input("Password?")
        if data[3]==p:
            print(f"Welcome {data[1]}")
        else:
            print("Wrong password")
db = pymysql.connect(host='127.0.0.1', user='root', password='root')
cursor = db.cursor()
query = "CREATE SCHEMA IF NOT EXISTS `login_register`;"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS `login_register`.`users` (`id` INT NOT NULL AUTO_INCREMENT,`full_name` VARCHAR(45) NULL,`username` VARCHAR(45) NOT NULL,`password` VARCHAR(45) NOT NULL,PRIMARY KEY (`id`),UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);"
cursor.execute(query)
for i in range(3):
    answer = int(input("Press 1 to Sign up\nPress 2 to Login:"))
    if answer==1:
        sign_up()
    elif answer==2:
        login()
