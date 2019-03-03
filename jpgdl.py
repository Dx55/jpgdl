import urllib.request

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input("Enter URL\n")
file_name = input("Enter name\n")

dl_jpg(url, '/Downloads/image', file_name)
