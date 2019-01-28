import os
from glob import glob

from Tools.scripts.win_add2path import PATH

result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], 'ok.md'))]
print (result)
