from vk_parse import VkParse
from const import TOKEN
from gdrive import Gdrive


def main():
    q = 'фото.png'
    titleZip = (q.replace('.', '_')) + ".zip"
    path = './files'
    vk = VkParse(TOKEN, q, 2, path)
    pathArchive = vk.zip()
    # pathArchive = "./files/фото_png.zip"
    drive = Gdrive() # auth
    drive.upload(pathArchive, titleZip)

if __name__ == "__main__":
    main()
