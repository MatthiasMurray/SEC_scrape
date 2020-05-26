import numpy as np

def fixdate(dateString):
  return ''.join(dateString.split('-'))

def foldpath(sectString):
  sectdict = {'Technology':'Technology','Health Care':'HealthCare','Consumer Services':'ConsumerServices','Consumer Durables':'ConsumerDurables','Capital Goods':'CapitalGoods',np.nan:'nan','Finance':'Finance','Miscellaneous':'Miscellaneous','Consumer Non-Durables':'ConsumerNonDurables','Public Utilities':'PublicUtilities','Basic Industries':'BasicIndustries','Transportation':'Transportation','Energy':'Energy'}
  return sectdict[sectString]
