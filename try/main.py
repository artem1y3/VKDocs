import vk
import urllib
from const import TOKEN

def show_docs(docs):
    i = 1
    for doc in docs['items']:
        for key,att in doc.items():
            print(key,att)
        print('===========', i)
        i += 1


def load_docs(dict, count):
    # url = ''
    # urllib.request.urlretrieve(url, './25.psd')
    if count>dict['count']:
        print('Введено число превышающее количество')
        return
    i = 1
    for doc in dict['items']:
        urllib.request.urlretrieve(doc['url'],'./files/{}'.format(doc['title']))
        print('Загружено: {} файл(ов) из {}'.format(i,count))
        i += 1
    print('Загрузка завершена!')


def main():
    count = 2
    session = vk.Session(access_token=TOKEN)
    api = vk.API(session,v = 5.74)
    # print(api.users.get(user_ids=1))
    docs = api.docs.search(q='site.psd',offset=0, search_own=0, count=count)
    print('==Обнаружено {} файл(ов)=='.format(docs['count']))
    # print(docs)
    show_docs(docs)
    # load_docs(docs,count)






if __name__ == "__main__":
    main()











