import vk
import urllib

def show_docs(docs):
    i = 0
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
    i = 1
    for doc in dict['items']:
        urllib.request.urlretrieve(doc['url'],'./files/{}'.format(doc['title']))
        print('Загружен: {} файл(ов) из {}'.format(i,count))
        i += 1
    print('Загрузка завершена!')


def main():
    count = 2
    session = vk.Session(access_token='bc04953d549913e2e3f6888152e6e4e9a1c7b1048bbc66831e720f8b8e0a21801edd52acd36dc3f8a4cdc')
    api = vk.API(session,v = 5.74)
    # print(api.users.get(user_ids=1))
    docs = api.docs.search(q='site.psd',offset=0, search_own=0, count=count)
    print(docs)
    show_docs(docs)
    load_docs(docs,count)






if __name__ == "__main__":
    main()











