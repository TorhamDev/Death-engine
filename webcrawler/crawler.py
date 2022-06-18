import threading
import os
from colorama import Fore
from queue import Queue
from .spider import Spider
from .domain import *
from .filelib import *


def create_workers(NUMBER_OF_THREADS):
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queues.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queues.task_done()


def create_jobs(QUEUE_FILE):
    for link in file_to_set(QUEUE_FILE):
        queues.put(link)
    queues.join()
    crawl_start(QUEUE_FILE)


def crawl_start(QUEUE_FILE):
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(
            Fore.CYAN + '[*]' + Fore.LIGHTCYAN_EX +
            str(len(queued_links)) + ' links in the queue' + Fore.RESET
        )
        create_jobs(QUEUE_FILE)


def crawl(HOMEPAGE):
    PROJECT_NAME = get_sub_domain_name(HOMEPAGE).split('.')
    PROJECT_NAME = PROJECT_NAME[-2]
    DOMAIN_NAME = get_domain_name(HOMEPAGE)
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
    NUMBER_OF_THREADS = int(str(os.cpu_count()))
    global queues
    queues = Queue()
    create_workers(NUMBER_OF_THREADS)
    crawl_start(QUEUE_FILE)
