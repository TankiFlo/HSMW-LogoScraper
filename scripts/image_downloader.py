import requests # for GET requests
import shutil # for writing images

def download_image(url, path, name):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(path + name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ', path + name)
    else:
        print('Image <- ' + name + ' -> Couldn\'t be retrieved')