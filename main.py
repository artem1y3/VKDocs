from vk_parse import VkParse
from const import TOKEN
from gdrive import Gdrive


def main():
    vk = VkParse(TOKEN, 'фото.png', 2, './files')
    pathArchive = vk.zip()
    drive = Gdrive() # auth
    drive.upload(pathArchive)

if __name__ == "__main__":
    main()
