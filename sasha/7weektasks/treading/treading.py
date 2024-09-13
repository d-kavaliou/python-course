from threading import Thread, Lock
import urllib.request 


path = '/Users/alexandra/Desktop/python/python-course/sasha/7weektasks/treading/'

urls = [
    "https://www.gutenberg.org/files/1661/1661-0.txt",
    "https://www.gutenberg.org/files/1342/1342-0.txt",
    "https://www.gutenberg.org/files/84/84-0.txt"
            ]

count = len(urls) 

def doawland(i, lock : Lock):
    lock.acquire()
    destination = 'File' + i + '.txt'
    url = urls[int(i)]
    urllib.request.urlretrieve(url, path + destination)
    lock.release()
def words(i, lock : Lock):
    lock.acquire()
    words = 0 
    lines = 0
    destination = 'File' + i + '.txt'
    file = open(path + destination)
    for line in file:
        lines += 1
        words += len(line.split())
    print(words)    
    lock.release()



if __name__ == '__main__':
    lock = Lock()

    d1 = Thread(target=doawland, args = ('0',lock,))
    d2 = Thread(target=doawland, args = ('1',lock,))
    d3 = Thread(target=doawland, args = ('2',lock,))
    d1.start()
    d2.start()
    d3.start()
    d1.join()
    d2.join()
    d3.join()
    w1 = Thread(target=words, args = ('0',lock,))
    w2 = Thread(target=words, args = ('1',lock,))
    w3 = Thread(target=words, args = ('2',lock,))
    w1.start()
    w2.start()
    w3.start()
    w1.join()
    w2.join()
    w3.join()


