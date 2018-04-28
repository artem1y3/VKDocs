"""
Shows basic usage of the Drive v3 API.

Creates a Drive v3 API service and prints the names and ids of the last 10 files
the user has access to.
"""
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

# from apiclient import discovery
# from oauth2client import client
# from oauth2client import tools
# from oauth2client.file import Storage
# import os

# Setup the Drive v3 API
SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('drive', 'v3', http=creds.authorize(Http()))

# Call the Drive v3 API
results = service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])
if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print('{0} ({1})'.format(item['name'], item['id']))



# media = MediaFileUpload('pig.png', mimetype='image/png')
# response = media.insert(media_body=media, body={'name': 'Pig'}).execute()



# def uploadFile(filename, filepath, mimetype):
#     file_metadata = { 'name' : filename}
#     media = MediaFileUpload(filepath, mimetype=mimetype)
#     file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()