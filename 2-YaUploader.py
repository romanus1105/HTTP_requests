import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json', 
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, local_path: str, remote_path: str, replace=True):
        host = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        res = requests.get(f'{host}/upload?path={remote_path}&overwrite={replace}', headers=headers).json()
        with open(local_path, 'rb') as f:
            try:
                requests.put(res['href'], files={'file':f})
            except KeyError:
                print(res)

if __name__ == '__main__':
    path_to_local_file = ''
    path_to_remote_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_local_file, path_to_remote_file)