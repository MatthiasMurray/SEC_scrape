import pandas as pd
import numpy as np
from extract_data import *
import sys

companies = pd.read_csv('/Users/Matthias/Downloads/companylist.csv')
bigticklist = list(companies.Symbol)
bigsectlist = list(companies.Sector)
B = len(bigticklist)
j = int(sys.argv[1])

ticklist = bigticklist[j:min((j+50),B)]
sectlist = bigsectlist[j:min((j+50),B)]
if B<=j+50:
  print('NO MORE DATA TO PROCESS AFTER THIS...')

def fixdate(dateString):
  return ''.join(dateString.split('-'))

def foldpath(sectString):
  sectdict = {'Technology':'Technology','Health Care':'HealthCare','Consumer Services':'ConsumerServices','Consumer Durables':'ConsumerDurables','Capital Goods':'CapitalGoods',np.nan:'nan','Finance':'Finance','Miscellaneous':'Miscellaneous','Consumer Non-Durables':'ConsumerNonDurables','Public Utilities':'PublicUtilities','Basic Industries':'BasicIndustries','Transportation':'Transportation','Energy':'Energy'}
  return sectdict[sectString]

for i in range(len(ticklist)):
  print('|'+int(i/2)*'#'+int((50-i)/2)*' '+'|'+str(2*i)+'%'+'current: '+ticklist[i])
  try:
    xmldata = process_list([ticklist[i]])

    scrape_path = '/Users/Matthias/Documents/LexisNexis/SEC_10qs/scraped_files/'

    for x in xmldata:
      xml_file = open(scrape_path+foldpath(sectlist[i])+'/'+x[2].lower()+'_'+fixdate(x[-1])+'_10q.xml','w')
      xml_file.write(x[0])
      xml_file.close()
  except:
    print(j+i)
    break

#for i in range(len(ticklist)):
#  print('|'+int(i/2)*'#'+int((50-i)/2)*' '+'|'+str(2*i)+'%'+'current: '+ticklist[i])
#
#  xmldata = process_list([ticklist[i]])
#
#  scrape_path = '/Users/Matthias/Documents/LexisNexis/SEC_10qs/scraped_files/'
#
#  for x in xmldata:
#    xml_file = open(scrape_path+foldpath(sectlist[i])+'/'+x[2].lower()+'_'+fixdate(x[-1])+'_10q.xml','w')
#    xml_file.write(x[0])
#    xml_file.close()

print(j+i)
