from multiprocessing import Process
import urllib.request 


path = '/Users/alexandra/Desktop/python/python-course/sasha/7weektasks/multiprocessing/'

urls = [
    "https://www.gutenberg.org/files/1661/1661-0.txt",
    "https://www.gutenberg.org/files/1342/1342-0.txt",
    "https://www.gutenberg.org/files/84/84-0.txt"
            ]


def doawland(i):
    destination = 'File' + i + '.txt'
    url = urls[int(i)]
    urllib.request.urlretrieve(url, path + destination)
def words(i):
    words = 0 
    lines = 0
    destination = 'File' + i + '.txt'
    file = open(path + destination)
    for line in file:
        lines += 1
        words += len(line.split())
    print(words)     


if __name__ == '__main__':
    d1 = Process(target=doawland, args = ('0'))
    d2 = Process(target=doawland, args = ('1'))
    d3 = Process(target=doawland, args = ('2'))
    d1.start()
    d2.start()
    d3.start()
    d1.join()
    d2.join()
    d3.join()
    w1 = Process(target=words, args = ('0'))
    w2 = Process(target=words, args = ('1'))
    w3 = Process(target=words, args = ('2'))
    w1.start()
    w2.start()
    w3.start()
    w1.join()
    w2.join()
    w3.join()


