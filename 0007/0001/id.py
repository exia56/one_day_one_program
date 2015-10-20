import random
import string

choice = string.ascii_letters + string.digits

def gen_code(no_id):
    h_id = hex(no_id)[2:]
    code = h_id + 'L'
    other_code = ( random.choice(choice) for i in range(15-len(code)) )
    code = code + "".join(other_code)
    return code

for i in range(200):
    no_id = (int)(random.random()*10000)
    code = gen_code(no_id)
    af_id = int("0x"+code.split("L")[0] , 16)
    print af_id,"\t",code
