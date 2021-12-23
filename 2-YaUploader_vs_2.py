import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json', 
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        resp = requests.get(upload_url, headers=headers, params=params)
        return resp.json()

    def upload_file_to_remote_disk(self, disk_file_path, filename):
        href_attr = self._get_upload_link(disk_file_path=disk_file_path).get('href', '')
        resp = requests.put(href_attr, data=open(filename, 'rb'))
        resp.raise_for_status()
        if resp.status_code == 201:
            print('Success')

if __name__ == '__main__':
    path_to_local_file = ''
    path_to_remote_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload_file_to_remote_disk(path_to_remote_file, path_to_local_file)