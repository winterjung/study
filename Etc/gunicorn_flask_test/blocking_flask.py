from time import sleep

import requests
from flask import Flask

app = Flask(__name__)


@app.route('/sleep/<int:count>')
def sleeping(count):
    print('sleep in {}s'.format(count))
    sleep(count)
    print('awake {}s sleep'.format(count))
    return 'done'


@app.route('/request/<int:count>')
def request(count):
    print('request')
    r = requests.get(f'http://httpbin.org/delay/{count}')
    print('request done')
    return str(r.status_code)


@app.route('/compute/<int:count>')
def compute(count):
    s = 0
    for i in range(count):
        s += i
    print(s)
    return str(s)


@app.route('/')
def main():
    print('main')
    return 'main'


if __name__ == '__main__':
    app.run(debug=True)
