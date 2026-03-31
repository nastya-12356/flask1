from requests import post

print(post('http://localhost:8080/api/users', json={}).json())

print(post('http://localhost:8080/api/users',
           json={'name': 'asfafafasfasfas'}).json())

print(post('http://localhost:8080/api/users',
           json={'surname': 'Virin',
                 'name': 'Samson',
                 'age': 66,
                 'position': 'pilot',
                 'email': 'superpilot@mars.space',
                 'address': 'module_2',
                 'password': 'sigmawork',
                 'city_from': 'Beijing',
                 'speciality': 'pilot_professional'}).json())


# v2
print(post('http://localhost:8080/api/v2/users', json={}).json())

print(post('http://localhost:8080/api/v2/users',
           json={'name': 'asfafafasfasfas'}).json())

print(post('http://localhost:8080/api/v2/users',
           json={'surname': 'Virin',
                 'name': 'Samson',
                 'age': 66,
                 'position': 'pilot',
                 'email': 'superpilot666@mars.space',
                 'address': 'module_2',
                 'password': 'sigmawork',
                 'city_from': 'Beijing',
                 'speciality': 'pilot_professional'}).json())