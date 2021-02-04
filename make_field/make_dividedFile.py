# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:09:07 2021

@author: tiger
"""

import os
import pandas as pd

sr = 'dynamics'

for i in range (21):
    
   os.chdir(r"C:\Users\%03.f"%(i*300+1)+"-%03.f"%(i*300+300)+"")
   path= os.getcwd() # 現在のディレクトリ取得
   print(path)
   df = pd.read_table('mergefile.txt', header=None, delim_whitespace=True)
   df.to_csv('mergefile.csv', index=False, header=False)

       
        
   # f = open(r"0.1-cicle-frequency number-%02.f"%(i*300+60*(j+1))+".txt", 'r')
   #read_text_file = pd.read_csv (r"mergefile.txt",)
    #read_text_file.to_csv (r"mergefile.csv", float_format='%.3f', )
    
"""
   if os.path.exists('mergefile.txt'):
     print("ファイルを削除します。")
     os.remove('mergefile.txt')
"""

"""
    datalist = f.read()
    print(datalist)
    fl = open('mergefile.txt', 'x')
    fl.writelines(datalist)
    
    f.close()
    fl.close()
"""
   
   
   
   


"""

sr = 'activity-degree'
    
path = f"../{sr}/all"
os.mkdir(path)
"""
