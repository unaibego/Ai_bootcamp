from tqdm import tqdm
import time


# def ft_progress(lista):
#     for elem  in tqdm(lista):
#        pass     
#     return lista

listy = range(1000)
ret = 0
for elem in tqdm(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)