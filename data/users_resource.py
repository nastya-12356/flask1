from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.users import User
from data.reqparse_user import parser


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"Users {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.get(User, users_id)
        return jsonify({'users': users.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.get(User, users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, users_id):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        users = db_sess.get(User, users_id)
        users.surname = args['surname']
        users.name = args['name']
        users.age = args['age']
        users.position = args['position']
        users.speciality = args['speciality']
        users.address = args['address']
        users.email = args['email']
        users.set_password(args['password'])
        users.city_from = args['city_from']
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            city_from=args['city_from'],
        )
        users.set_password(args['password'])
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})






