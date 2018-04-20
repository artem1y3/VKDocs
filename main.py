import vk


def main():
    session = vk.Session(access_token='bc04953d549913e2e3f6888152e6e4e9a1c7b1048bbc66831e720f8b8e0a21801edd52acd36dc3f8a4cdc')
    api = vk.API(session,v = 5.74)
    # print(api.users.get(user_ids=1))
    docs = api.docs.search(q='site.psd', count=5)
    print(docs)
    i = 0
    for doc in docs['items']:
        for key,att in doc.items():
            print(key,att)
        print('===========', i)
        i += 1


if __name__ == "__main__":
    main()