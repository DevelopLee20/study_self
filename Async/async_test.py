import asyncio
import time
import pandas as pd

async def one():
    await pd.read_csv('C:/Users/dldls/바탕 화면/Coding/study_self/Async/airport_reviews.csv')
    x = await [i for i in range(100)]
    y = await [i for i in range(100)]
    
def two():
    pd.read_csv('C:/Users/dldls/바탕 화면/Coding/study_self/Async/airport_reviews.csv')
    x = [i for i in range(100)]
    y = [i for i in range(100)]

if __name__ == '__main__':
    start = time.time()
    one()
    end = time.time()
    print(f'one time : {end-start}')
    start = time.time()
    two()
    end = time.time()
    print(f'two time : {end-start}')