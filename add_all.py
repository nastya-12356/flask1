from adds.add_categories import add_categories
from adds.add_departaments import insert_departments
from adds.add_users import insert_users
from adds.add_jobs import insert_jobs

if __name__ == '__main__':
    add_categories()
    insert_departments()
    insert_users()
    insert_jobs()