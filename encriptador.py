import random
from werkzeug.security import generate_password_hash

class Hash_pass:

    def __init__(self):
        self.custom_pass = ''
        self.minus = 'abcdefghijklmnopqrstuvwxyz'
        self.mayus = self.minus.upper()
        self.num = '0123456789'
        self.simb = '!@#$%&/¡¿+*'
        self.longitud = 12
        
        
        
    def __str__(self) -> str:
            return (f'minus:{self.minus},mayus:{self.mayus},num:{self.num},simb:{self.simb},longitud:{self.longitud}')
    
    def get_chain(self):
        return self.minus + self.mayus + self.num + self.simb
    
    def get_random_hash(self,longitud):
        
        chain = random.sample(self.get_chain(),longitud)
        str_chain = ''.join(chain)
        hash_pass = generate_password_hash(str_chain)
        return (f'pass:{str_chain} || encript:{hash_pass}')
    
    def get_hash(self,custom_pass):
        hash_pass = generate_password_hash(custom_pass)
        return (f'custom_pass:{custom_pass} || encript:{hash_pass}')

new_hash = Hash_pass()
print(new_hash)

print(new_hash.get_random_hash(8))
print(new_hash.get_hash('123asdzxc!'))
print(new_hash.longitud)