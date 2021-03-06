import random
import string
import MySQLdb

choice = string.ascii_letters + string.digits
DB_host = "127.0.0.1"
DB_user = "root"
DB_pass = "root"
DB_name = "py"
used_id = []


def gen_code(no_id):
    h_id = hex(no_id)[2:]
    code = h_id + 'L'
    other_code = ( random.choice(choice) for i in range(15-len(code)) )
    code = code + "".join(other_code)
    return code


db = MySQLdb.connect(host=DB_host, user=DB_user,
                        passwd=DB_pass, db=DB_name)
cursor = db.cursor()
sql = '''DELETE FROM `code`'''
cursor.execute(sql)

for i in range(200):
    no_id = (int)(random.random()*10000)
    while no_id in used_id:
        no_id = (int)(random.random()*10000)
    used_id.append(no_id) 
    code = gen_code(no_id)
    sql = '''INSERT INTO `code`(`idx`,`code1`) VALUES (%d,'%s')'''%(
                no_id, code)
    cursor.execute(sql)
    sql = '''SELECT `idx` FROM `code` where (`code1`='{0}')'''.format(code)
    cursor.execute(sql)
    af_id = cursor.fetchone()[0]

    print af_id,"\t",code
