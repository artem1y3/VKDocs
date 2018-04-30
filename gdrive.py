from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class Gdrive(object):
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.
        # self.gauth.CommandLineAuth() # Creates local webserver and auto handles authentication.

    def upload(self, filepath, title):
        print("Загрузка на облако началась...")
        drive = GoogleDrive(self.gauth)
        file1 = drive.CreateFile({'title': title})  # Create GoogleDriveFile instance with title 'Hello.txt'.
        file1.SetContentFile(filepath)  # Set content of the file from given string.
        file1.Upload()
        print("Загрузка завершена!")


        # # Auto-iterate through all files that matches this query
        # file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        # for file1 in file_list:
        #   print('title: %s, id: %s' % (file1['title'], file1['id']))
