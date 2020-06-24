import os
import label_sp_filenames
from label_sp_filenames import *

labguide = open('labelguide.csv','w')
labguide.write('"original","sandp"')
labguide.write('\n')

newlabpath = '/Users/Matthias/Documents/LexisNexis/SEC_10qs/scraped_files/num_labels_new/'


for f in os.listdir(newlabpath):

  labguide.write(f + ',' + label_fileName(f))
  labguide.write('\n')

labguide.close()
