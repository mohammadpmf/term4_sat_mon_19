from myclass import *
from settings import *

root = Tk()
root.geometry('500x300')
root.config(bg='#333333')
btn_management=Button(root, text='Management', cnf=config_btns_root)
btn_search=Button(root, text='Search', cnf=config_btns_root)
btn_management.pack(cnf=config_btns_root_pack)
btn_search.pack(cnf=config_btns_root_pack)
mainloop()