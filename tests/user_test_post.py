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
                 'speciality': 'pilot_professional'}).json())