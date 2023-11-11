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
search_window.protocol('WM_DELETE_WINDOW', root.destroy)
management_window.protocol('WM_DELETE_WINDOW', root.destroy)
insert_window.protocol('WM_DELETE_WINDOW', root.destroy)
update_window.protocol('WM_DELETE_WINDOW', root.destroy)
delete_window.protocol('WM_DELETE_WINDOW', root.destroy)

######################## Management window widgets ########################
btn_add=Button(management_window, text='Add Game', cnf=config_btns_root,
    command=lambda:change_window(insert_window, management_window))
btn_update=Button(management_window, text='Update Game', cnf=config_btns_root,
    command=lambda:change_window(update_window, management_window))
btn_delete=Button(management_window, text='Delete Game', cnf=config_btns_root,
    command=lambda:change_window(delete_window, management_window))
btn_back_management=Button(management_window, text='Back', cnf=config_btns_root,
    command=lambda:change_window(root, management_window))
btn_add.pack(cnf=config_btns_root_pack)
btn_update.pack(cnf=config_btns_root_pack)
btn_delete.pack(cnf=config_btns_root_pack)
btn_back_management.pack(cnf=config_btns_root_pack)
######################## End Management window widgets ########################
######################## Insert window widgets ########################
game = MyGame(insert_window)
game.grid()
######################## End Insert window widgets ########################


btn_management=Button(root, text='Management', cnf=config_btns_root,
    command=lambda:change_window(management_window, root))
btn_search=Button(root, text='Search', cnf=config_btns_root)
btn_management.pack(cnf=config_btns_root_pack)
btn_search.pack(cnf=config_btns_root_pack)
mainloop()