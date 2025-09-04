import peewee
from datetime import datetime

database = peewee.MySQLDatabase('pythondb', 
                     host='localhost', 
                     port=3306,
                     user='root',
                     password='intro123'
                     )

# users
class User(peewee.Model):
    username=peewee.CharField(max_length=50, unique=-True, index=True)
    email=peewee.CharField(max_length=60, null=False)
    active=peewee.BooleanField(default=False)
    created_at=peewee.DateTimeField(default=datetime.now)
    
    class Meta:
        database=database
        db_table='users'
        
if __name__ == '__main__':
    User.create_table()
