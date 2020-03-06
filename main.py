from datetime import date, timedelta
import os
import requests

base_url = 'http://webdisk.diariooficial.rn.gov.br/Jornal/1'
headers = {'User-Agent': 'Mozilla/5.0'}
current_date = date.today()

while True:
    if current_date.day == 1:
        break;

    date_url = current_date.strftime("%Y-%m-%d")
    file_path = f'output/{date_url}.pdf'

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path,'wb') as f:
        url = f'{base_url}{date_url}.pdf'
        print(f'requesting {url!r}')
        response = requests.get(url, headers=headers)
        content_type = response.headers['content-type']

        if 'pdf' in content_type:
            print(f'[OK] {url}')
            f.write(response.content)
        else:
            print(f'[Fail] {url}')
        current_date = current_date - timedelta(days=1)

