from pydrive.auth import GoogleAuth

gauth = GoogleAuth()

# gauth = GoogleAuth()
# auth_url = gauth.GetAuthUrl() # Create authentication url user needs to visit
# code = AskUserToVisitLinkAndGiveCode(auth_url) # Your customized authentication flow
# gauth.Auth(code) # Authorize and build service from the code

# auth_url = gauth.GetAuthUrl() # Create authentication url user needs to visit
# code = AskUserToVisitLinkAndGiveCode(auth_url) # Your customized authentication flow
# gauth.Auth(code) # Authorize and build service from the code

gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
# gauth.CommandLineAuth() # Creates local webserver and auto handles authentication.

#Create hello.txt and write ...
from pydrive.drive import GoogleDrive
drive = GoogleDrive(gauth)


file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Hello World!') # Set content of the file from given string.
file1.Upload()

# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))



# auth_url = gauth.GetAuthUrl() # Create authentication url user needs to visit
# code = AskUserToVisitLinkAndGiveCode(auth_url) # Your customized authentication flow
# gauth.Auth(code) # Authorize and build service from the code

# import json
# import requests
# headers = {"Authorization": "Bearer ya29.GlyrBVkEet6p8MCCB8OEdBuWs0GaTFrS3uEGYzHYl5p-8dmwrDR3IVvjdJQtWfwiW9bX7cPcrAhKEZ9ORESAfXJtvvyYkhuh5OIsbFatt8Ds1riH6r1iuJ4bqHcDmw"}
# para = {
#     "name": "sample.png",
#     "parents": ["1N3JiCMOcSfw8MqywuNz5YDc13MFPIZOg"]
# }
# files = {
#     'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#     'file': open("./sample.png", "rb")
# }
# r = requests.post(
#     "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#     headers=headers,
#     files=files
# )
# print(r.text)