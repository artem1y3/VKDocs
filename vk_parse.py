import vk
import urllib


class VkParse(object):
    def __init__(self, token, search, count, folderPath):
        self.folderPath = folderPath
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
        if count > dict['count']:
            print('Введено число превышающее количество')
            return
        i = 1
        for doc in dict['items']:
            urllib.request.urlretrieve(doc['url'], './files/{0}/{1}'.format(self.folderPath, doc['title']))
            print('Загружено: {} файл(ов) из {}'.format(i, count))
            i += 1
        print('Загрузка завершена!')

