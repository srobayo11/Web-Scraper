from bs4 import BeautifulSoup
import requests
import re

if __name__ == '__main__':

    url = 'https://www.usc.edu.au/research/sustainability-and-environment/sustainability-research-centre'
    url1 = url.split('/')
    url_prefix = url1[0]+'//'+url1[2]
    source = requests.get(url).text
    source_array = []
    soup = BeautifulSoup(source, 'lxml')

    for link in soup.find_all('a'):

        if type(link.get('href'))is str:
            contact = link.get('href')
        if 'contact' in contact:
            source_array.append(url_prefix + contact)

    source_array = list(dict.fromkeys(source_array))
    name_list =[]
    email_list = []
    for urls in source_array:
         if 'research' in urls:
            source = requests.get(urls).text
            soup = BeautifulSoup(source, 'lxml')
            for names in soup.find_all(href=re.compile("staff")):
                if 'Professor' in names.text or 'Dr'in names.text or 'Associate'in names.text or '\n' not in names.text and len(names.text) > 15:
                    name_list.append(names.text)
            for emails in soup.find_all(href=re.compile("mailto")):
                email_list.append(emails.text)
    dictionary = dict(zip(name_list, email_list))
    print(dictionary)

