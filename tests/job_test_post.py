from requests import post

print(post('http://localhost:8080/api/jobs', json={}).json())

print(post('http://localhost:8080/api/jobs',
           json={'job': 'asfafafasfasfas'}).json())

print(post('http://localhost:8080/api/jobs',
           json={'team_leader': 2,
                 'job': 'Clean room',
                 'collaborators': '1, 2',
                 'work_size': 22,
                 'is_finished': True}).json())