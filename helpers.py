import os
from datetime import date

import requests


output_path = 'output'
base_url = 'http://webdisk.diariooficial.rn.gov.br/Jornal/1'
headers = {'User-Agent': 'Mozilla/5.0'}


def check_output_path():
    if not os.path.isdir(output_path):
        os.mkdir(output_path)


def get_pdf_by_date(date_value, ignore_cache=False):
    date_url = date_value.strftime("%Y-%m-%d")
    file_path = f'output/{date_url}.pdf'

    if os.path.exists(file_path):
        print(f'[CACHE] {file_path}')
        if not ignore_cache:
            return
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

