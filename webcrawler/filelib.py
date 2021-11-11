import os
from colorama import Fore

def create_dir(directory):
    if os.path.exists(directory):
        print(Fore.LIGHTRED_EX + '[*] A folder with your project name already exists !\nMove, remove or rename and then run the script to continue\n' + Fore.RESET)
        return False
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(Fore.LIGHTBLUE_EX + '[*] Crawl directory created : ' + directory + Fore.RESET + '\n')

def create_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
        
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_data(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_contents(path):
    with open(path, 'w'):
        pass

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(links, file):
    delete_contents(file)
    for link in sorted(links):
        append_data(file, link)

