from user import Users 
from roles import Privaleges, Admin

new_admin = Admin('Jane', 'Smith', 30, 'Los Angeles')
new_admin.privileges.show_privaleges()