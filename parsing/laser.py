import time

from tqdm import tqdm
a=range(10)
for _ in tqdm(range(10), desc='Fetching data...', colour='GREEN'):
    print('Hello world')