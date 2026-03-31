from requests import get

print(get('http://localhost:8080/api/jobs').json())
print(get('http://localhost:8080/api/jobs/1').json())
print(get('http://localhost:8080/api/jobs/999').json())
print(get('http://localhost:8080/api/jobs/svssvsvvs').json())

# v2
print(get('http://localhost:8080/api/v2/jobs').json())
print(get('http://localhost:8080/api/v2/jobs/1').json())
print(get('http://localhost:8080/api/v2/jobs/999').json())
print(get('http://localhost:8080/api/v2/jobs/svssvsvvs').json())
