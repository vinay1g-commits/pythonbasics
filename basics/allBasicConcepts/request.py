import requests
"""data = requests.get("https://reqres.in/api/users?page=2")
assert data.status_code == 200
if data.status_code == 200:
    print("success")
else:
    print("request failure")
print(data.json())
"""
# Create a new user
user_data = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post("https://reqres.in/api/users", json=user_data)  # Use json parameter
assert response.status_code == 201  # 201 Created
print("User created:", response.json())

# Update user data
usr_data = {
    "name": "vinay",
    "job": "zion resident"
}
response2 = requests.put("https://reqres.in/api/users/2", json=usr_data)  # Use json parameter
assert response2.status_code == 200  # 200 OK
print("User updated:", response2.json())

url = "https://reqres.in/api/users/2"
response3 = requests.delete(url)
assert response3.status_code == 204
print(response3.json())
