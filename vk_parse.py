import vk
import urllib
import os
import zipfile


class VkParse(object):
    def __init__(self, token, search, count, folderPath):
        self.folderPath = folderPath
        self.search = search.replace('.', '_')
        session = vk.Session(access_token=token)
        api = vk.API(session, v=5.74)
        # print(api.users.get(user_ids=1))
        docs = api.docs.search(q=search, offset=0, search_own=0, count=count)
        print('==Обнаружено {} файл(ов)=='.format(docs['count']))
        # print(docs)
        self.show_docs(docs)
        self.load_docs(docs, count)

    def show_docs(self, docs):
        i = 1
        for doc in docs['items']:
            for key, att in doc.items():
                print(key, att)
            print('===========', i)
            i += 1

    def load_docs(self, dict, count):
        # url = ''
        # urllib.request.urlretrieve(url, './25.psd')
        if int(count) > int(dict['count']):
            print('Введено число превышающее количество')
            return
        i = 1
        s = self.folderPath + '/' + self.search
        if not os.path.exists(self.folderPath):
            os.makedirs(self.folderPath)
        if not os.path.exists(s):
            os.makedirs(s)
        for doc in dict['items']:
            urllib.request.urlretrieve(doc['url'], './{0}/{1}/{2}'.format(self.folderPath, self.search, doc['title']))
            print('Загружено: {} файл(ов) из {}'.format(i, count))
            i += 1
        print('Загрузка завершена!')

    def zip(self):
        # Распаковка
        # extract_archive(zip,path)
        # Список файлов
        lst = os.listdir(path=self.folderPath + "/" + self.search)
        try:
            newzip = zipfile.ZipFile(self.folderPath + "/" + self.search + '.zip', 'w')  # создаем архив
            print("Архив создан!")
            print("Загрузка файлов в архив: ")
            for file in lst:
                newzip.write(self.folderPath + "/" + self.search + "/" + file, "/" + file)
                print(file)

            newzip.close()  # закрываем архив
        except:
            print("Что-то пошло не так с архивом")
        return self.folderPath + "/" + self.search + '.zip'

