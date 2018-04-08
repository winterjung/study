import os
import time


worker = [1, 2, 4]
threads = [1, 2, 4]
worker_class = ['sync', 'gevent', 'gaiohttp']
endpoints = ['sleep/3', 'request/3', 'compute/2000000']
app = 'blocking_flask:app'

num = 32
con = 16
folder = 'result'

os.system(f'mkdir {folder}')
for w in worker:
    for t in threads:
        for c in worker_class:
            for end in endpoints:
                task = end.split('/')[0]
                name = f'test-{w}-{t}-{c}-{task}'
                gunicorn = f'gunicorn -D -w {w} --threads {t} -k {c} -n {name} {app}'
                ab = f'ab -n {num} -c {con} 127.0.0.1:8000/{end} > {folder}/{name}'
                print(f'launch {gunicorn}')
                os.system(gunicorn)
                print('waiting')
                time.sleep(2)
                print(f'test using {ab}')
                os.system(ab)
                print('test done')
                print('kill gunicorn')
                os.system(f'pgrep {name} | xargs kill -9')
                print('finish')
                print('-' * 40)
