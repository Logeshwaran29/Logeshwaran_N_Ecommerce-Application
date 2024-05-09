import mysql.connector as sql


class exception(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class customer(exception):
    db = sql.connect(host='localhost', database='sample', user='root', password='log123@#')

    def __init__(self):
        self.custId = int(input('Enter Cust_id:'))
        self.name = input('Enter Cust_name:')
        self.city = input('Enter Cust_City:')
        self.phno = int(input('Enter Phno:'))

    def store(self):
        try:
            for i in range(0, 10):
                if str(i) in self.name:
                    raise exception('User Name contains number...')
                if str(i) in self.city:
                    raise exception('City contains number...')

            stmt = self.db.cursor()
            query = '''insert into customer (custName, city,phNo) values(%s,%s,%s)'''
            data = [self.name, self.city, self.phno]
            stmt.execute(query, data)
            self.db.commit()
        except Exception as e:
            print(e)

    def view(self):
        stmt = self.db.cursor()
        query = '''select * from customer'''
        stmt.execute(query)
        rec = stmt.fetchall()
        print(rec)

    def select(self, id):
        stmt = self.db.cursor()
        stmt.execute(f'''select * from customer where custId = {id}''')
        res = stmt.fetchall()
        if res:
            query = f'''delete from customer where custId = {id}'''
            stmt.execute(query)
            self.db.commit()
        else:
            print('Id not found...')


l = customer()
# l.select(1)
l.store()
l.view()
