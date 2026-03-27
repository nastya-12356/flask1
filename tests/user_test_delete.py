from requests import delete, get

print(delete('http://localhost:8080/api/users/999').json())
# новости с id = 999 нет в базе
print(delete('http://localhost:8080/api/users/awfafafaf').json())
print(delete('http://localhost:8080/api/users/1').json())

print(get('http://localhost:8080/api/users').json())