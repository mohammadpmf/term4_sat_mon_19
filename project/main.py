from myclass import *
from settings import *

def change_window(show_window: Toplevel, hide_window: Toplevel):
    show_window.deiconify()
    hide_window.withdraw()

connection = MyConnection()

root = Tk()
root.geometry('500x300')
root.config(bg=BG)
search_window = Toplevel(root)
management_window = Toplevel(root)
insert_window = Toplevel(management_window)
update_window = Toplevel(management_window)
delete_window = Toplevel(management_window)
search_window.withdraw()
management_window.withdraw()
insert_window.withdraw()
update_window.withdraw()
delete_window.withdraw()
search_window.config(bg=BG)
management_window.config(bg=BG)
insert_window.config(bg=BG)
update_window.config(bg=BG)
delete_window.config(bg=BG)

btn_management=Button(root, text='Management', cnf=config_btns_root,
    command=lambda:change_window(management_window, root))
btn_search=Button(root, text='Search', cnf=config_btns_root)
btn_management.pack(cnf=config_btns_root_pack)
btn_search.pack(cnf=config_btns_root_pack)
mainloop()