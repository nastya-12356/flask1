from requests import get, put

print(put('http://localhost:8080/api/jobs/1', json={}).json())

print(put('http://localhost:8080/api/jobs/1',
           json={'job': 'asfafafasfasfas'}).json())

print(put('http://localhost:8080/api/jobs/2',
           json={'team_leader': 2,
                 'job': 'Remake room',
                 'collaborators': '2, 1',
                 'work_size': 11,
                 'is_finished': False}).json())

print(get('http://localhost:8080/api/jobs').json())

# v2

print(put('http://localhost:8080/api/v2/jobs/1', json={}).json())

print(put('http://localhost:8080/api/v2/jobs/1',
           json={'job': 'asfafafasfasfas'}).json())

print(put('http://localhost:8080/api/v2/jobs/2',
           json={'team_leader': 3,
                 'job': 'Remake room',
                 'collaborators': '3, 4',
                 'work_size': 22,
                 'is_finished': False}).json())

print(get('http://localhost:8080/api/v2/jobs').json())