import pandas as pd
import numpy as np
from extract_data import *
from scrape_utils import *
import sys

companies = pd.read_csv('/Users/Matthias/Downloads/companylist.csv')
bigticklist = list(companies.Symbol)
bigsectlist = list(companies.Sector)
B = len(bigticklist)
j = int(sys.argv[1])
batchsize = int(sys.argv[2])

ticklist = bigticklist[j:min((j+batchsize),B)]
sectlist = bigsectlist[j:min((j+batchsize),B)]
if B<=j+batchsize:
  print('NO MORE DATA TO PROCESS AFTER THIS...')

for i in range(len(ticklist)):
  print('|'+int(i/5)*'#'+int((batchsize-i)/5)*' '+'|'+str(i*100/batchsize)+'%'+'current: '+ticklist[i])
  
  try:
    xmldata = process_list([ticklist[i]])
  except:
    print(j+i)
    break
  
  scrape_path = '/Users/Matthias/Documents/LexisNexis/SEC_10qs/scraped_files/'

  for x in xmldata:
    xml_file = open(scrape_path+foldpath(sectlist[i])+'/'+x[2].lower()+'_'+fixdate(x[-1])+'_10q.xml','w')
    xml_file.write(x[0])
    xml_file.close()

print(j+i)
