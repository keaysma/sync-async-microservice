from time import sleep
from requests import get

def test():
    sleep(5)
    get('http://0.0.0.0:5001/')

if __name__ == '__main__':
    test()