from data import db_session
from data.category import Category

db_session.global_init("db/mars_explorer.db")


def add_categories():
    db_sess = db_session.create_session()

    categories = [
        '1',
        '2',
        '3',
        '4'
    ]
    for elem in categories:
        category = Category()
        category.name = elem
        db_sess = db_session.create_session()
        db_sess.add(category)
        db_sess.commit()

if __name__ == '__main__':
    add_categories()
