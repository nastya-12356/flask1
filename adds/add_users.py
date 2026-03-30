from data.users import User
from data import db_session

db_session.global_init("db/mars_explorer.db")
data = [{'name': 'Ridley',
         'age': 21,
         'surname': 'Scott',
         'position': "captain",
         'email': 'scott_chief@mars.org',
         'speciality': 'research engineer',
         'address': 'module_1',
         'city_from': 'Paris'},
        {'name': 'Sam',
         'age': 19,
         'surname': 'Smith',
         'position': "sailor",
         'email': 'sam_durak@mars.org',
         'speciality': 'navigator',
         'address': 'module_2',
         'city_from': 'Moscow'},
        {'name': 'Dan',
         'age': 18,
         'surname': 'Williams',
         'position': "sailor",
         'email': 'williams_chief@mars.org',
         'speciality': 'boatswain',
         'address': 'module_3',
         'city_from': 'New York'},
        {'name': 'Jimmi',
         'age': 17,
         'surname': 'Brown',
         'position': "sailor",
         'email': 'brown_chief@mars.org',
         'speciality': 'sailor',
         'address': 'module_4',
         'city_from': 'Dubai'}
        ]

def insert_users():
    for elem in data:
        user = User()
        user.name = elem['name']
        user.age = elem['age']
        user.surname = elem['surname']
        user.position = elem['position']
        user.email = elem['email']
        user.speciality = elem['speciality']
        user.address = elem['address']
        user.city_from = elem['city_from']
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()

if __name__ == '__main__':
    insert_users()

