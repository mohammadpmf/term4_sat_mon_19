from fallah import *
from tkinter import *
import pymysql

class MyConnection():
    def __init__(self, user='root', password='root'):
        self.db = pymysql.connect(host='localhost', user=user, password=password)
        self.cursor = self.db.cursor()
        query = "CREATE SCHEMA IF NOT EXISTS `term4`;"
        self.cursor.execute(query)
        query = "CREATE TABLE IF NOT EXISTS `term4`.`games` (`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NOT NULL,`company` VARCHAR(40) NULL,`age` TINYINT UNSIGNED NULL,`price` INT UNSIGNED NOT NULL,`console` VARCHAR(30) NULL,`stock` SMALLINT UNSIGNED NOT NULL,`image` VARCHAR(200) NULL,PRIMARY KEY (`id`),UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE);"
        self.cursor.execute(query)
    
    def insert(self, name, price, stock, company='', age=0, console='', image=''):
        query = "INSERT INTO `term4`.`games` (`name`, `company`, `age`, `price`, `console`, `stock`, `image`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        values = name, company, age, price, console, stock, image
        self.cursor.execute(query, values)
        self.db.commit()

        
class AddGame(MyGame):
    def __init__(self, root, connection: MyConnection, bg='#333333', fg='orange', fg2='orange', text="Game Info", font=('Times', 20), bd=1, labelanchor='n', relief='raised', abg="orange", afg="#333333", padx=5, pady=5):
        super().__init__(root, bg, fg, fg2, text, font, bd, labelanchor, relief, abg, afg, padx, pady)
        self.connection = connection
        self.btn_save = Button(self.frame, text='Save', bg=bg, fg=fg2, font=font, bd=bd, activebackground=abg, activeforeground=afg, command=self.save)
        self.btn_reset = Button(self.frame, text='Reset', bg=bg, fg=fg2, font=font, bd=bd, activebackground=abg, activeforeground=afg, command=self.reset)
        self.btn_save.grid(row = 15, column=1)
        self.btn_reset.grid(row = 15, column=3)
    
    def reset(self):
        super().reset()
        self.e_name.focus_set()
    
    def save(self):
        name = self.e_name.get()
        company = self.e_company.get()
        age = self.e_age.get()
        price = self.e_price.get()
        console = self.e_console_type.get()
        stock = self.e_stock.get()
        address = self.file_address
        self.connection.insert(name, price, stock, company, age, console, address)
