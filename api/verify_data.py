from json import loads
import requests
import sys

URL_API = 'https://api.publicapis.org/entries'


def get_values_of_field(entries, field):
   dif_values = []

   for row in entries:
      
      if row[field] not in dif_values:
         dif_values.append(row[field])

   return dif_values


def get_max_len_of_field(entries, field): 

   length_list = []
   append = length_list.append

   for row in entries:
      append(len(row[field]))

   return max(length_list)


def get_content():

    res = requests.get(URL_API)

    if res.status_code == 200:
        content = res.json()

        return content['entries']
    
    return None


def get_content():

    res = requests.get(URL_API)

    if res.status_code == 200:
        content = res.json()

        return content['entries']


def Main():

    entries = get_content()

    if entries is None:
        sys.exit('Request failed')

    max_api = get_max_len_of_field(entries, 'API')
    max_description = get_max_len_of_field(entries, 'Description')
    list_auth = get_values_of_field(entries, 'Auth')
    list_cors = get_values_of_field(entries, 'Cors')

    print(max_api)
    print(max_description)
    print(list_auth)
    print(list_cors)


if __name__ == '__main__':
   Main()