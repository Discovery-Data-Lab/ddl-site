# Se você não esta entendendo nada, não tem problema. 
# Aqui queremos demonstrar apenas a diferença de tempo  ;)
from multiprocessing import Pool
import time

USE_MULTIPROCESSING = False

COUNT = 50000000
def countdown(n):
   while n>0:
      n -= 1

if __name__ == '__main__':
   start_time = time.time()
   
   if USE_MULTIPROCESSING:
      with Pool(processes=4) as pool:
         # Split work into 4 equal chunks
         chunk_size = COUNT // 4
         pool.map(countdown, [chunk_size] * 4)
   else:
      countdown(COUNT)

   elapsed_time = time.time() - start_time
   print(f'Time taken: {elapsed_time:.2f} seconds')