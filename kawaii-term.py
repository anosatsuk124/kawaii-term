import sys
import os
import re
if '--mem' in sys.argv:
  for line in os.popen('free').read().split('\n'):
      if 'Mem:' in line:
          line = line.strip()
          mem2  = re.split(r'\s{1,}', line)[2]
      if 'Mem:' in line:
          line = line.strip()
          # デフォルトではKB表現だから、メガバイトで表現する
          mem  = re.split(r'\s{1,}', line)[1]
          mem3  = str((int(mem) - int(mem2)) // 1000) + 'MB'
          per = str(round(int(mem2) / int(mem), 1)*100) + '%'
          print(mem3 + ' ' + per)
          break

if '--vmstat' in sys.argv:
  buff = os.popen('vmstat').read().split('\n')
  keys = re.split(r'\s{1,}', buff[1])
  vals = re.split(r'\s{1,}', buff[2])
  obj  = dict( zip(keys, vals) )
  ucpu = 'CPU={0:03d}%'.format( int(obj['us']) )
  print( ucpu )

if '--disk' in sys.argv:
  buff =os.popen('df -hT').read().split('\n')
  # 末尾が/で終わるのが、ルートディレクトリ表示
  keys = re.split(r'\s{1,}', buff[0])
  vals = re.split(r'\s{1,}', list( filter(lambda x:len(x) != 0 and x[-1] == '/', buff[1:]) )[0] )
  obj  = dict(zip( keys, vals) )
  try:
    use  = obj['Use%']
  except KeyError:
    try:
      use = obj['使用']
    except KeyError:
      use = 'NaN'

  try:
    free = obj['Avail']
  except KeyError:
    try:
      free = obj['残り']
    except KeyError:
      free = 'NaN'

  result = 'DiskUse%={}, DiskAvail={}'.format(use, free)
  print(result)
