from useapi import *

def label_fileName(origName):

  def midtrim(s):
    out=''
    for c in s:
      if c!=' ':
        out+=c
    return out

  def fixdate(s):
    out=''
    parts = s.split('_')
    date = parts[1]
    

  trimName = midtrim(origName)
  #step1 = origName.split('_')
  step1 = trimName.split('_')
  tick = step1[0]
  date = step1[1]
  year = int(date[:4])
  mnth = int(date[4:6])
  qtr  = setq(mnth)

  labels = exqtrlabs(tick.upper(),'s&p')
  
  label = [x for x in labels if x[0]==qtr and x[1]==year][0][-1]
  #return label , qtr, year
  return tick+'_'+str(year)+str(mnth)+date[-2:]+'_10q'+'_'+str(label)+'.xml' 
