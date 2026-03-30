from data.users import User
from data import db_session
from data.departments import Department

db_session.global_init("db/mars_explorer.db")
data = [{'title': 'Mars explores',
         'chief': 6,
         'email': 'tinker@mars.space',
         'members': '2, 3',},
        {'title': 'Mars hz',
         'chief': 5,
         'email': 'tinker2@mars.space',
         'members': '1, 4', },
        {'title': 'Mars shadows',
         'chief': 7,
         'email': 'tinker3@mars.space',
         'members': '5, 6', },
        ]

def insert_departments():
    for elem in data:
        department = Department()
        department.title = elem['title']
        department.chief = elem['chief']
        department.members = elem['members']
        department.email = elem['email']
        db_sess = db_session.create_session()
        db_sess.add(department)
        db_sess.commit()

if __name__ == '__main__':
    insert_departments()
