import pymysql
#                          localhost
db = pymysql.connect(host='127.0.0.1', user='root', password='root')
cursor = db.cursor()
cursor.execute("CREATE TABLE `store`.`games` (`id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NOT NULL,`company` VARCHAR(45) NULL,`pga` VARCHAR(45) NOT NULL,`price` INT NOT NULL,PRIMARY KEY (`id`));")
# cursor.execute("SELECT * FROM shop.fruits WHERE price<25000;")
# data = cursor.fetchall() # fetchall برو همه رو بیار
# data = cursor.fetchmany(3)
# for item in data:
#     print(item)
# data = cursor.fetchone()
# print(data)
cursor.execute("DELETE FROM shop.fruits WHERE (id=10);")
db.commit()
# دستوراتی که در تیبل تغییر ایجاد میکنند نیاز به کامیت کردن db دارند.