import json
import os
from urllib import urlopen

with open("//tmp//topbeat//topbeat") as f:
    content = f.readlines()
    for i in range(0,len(content)):
        result = json.loads(content[i])  
        if (result is None)or (len(result)==0):
            continue
        else:
            print "Process name: "+result.get('proc').get('name')+"\n\t PARENT PID: "+str(result.get('proc').get('ppid'))+"\n\t STATE: "+result.get('proc').get('state')+"\n\t CPU usage user: "+str(result.get('proc').get('cpu').get('user'))+"\n\t CPU usage user percentage: "+str(result.get('proc').get('cpu').get('user_p'))+"\n\t CPU usage system: "+str(result.get('proc').get('cpu').get('system'))+"\n\t CPU usage total: "+str(result.get('proc').get('cpu').get('total'))+"\n\t CPU usage start time: "+str(result.get('proc').get('cpu').get('start_time'))+"\n\t Memory usage virtual memory: "+str(result.get('proc').get('mem').get('size'))+"\n\t Memory usage resident memory: "+str(result.get('proc').get('mem').get('rss'))+"\n\t Memory usage resident memory percentage: "+str(result.get('proc').get('mem').get('rss_p'))+"\n\t Memory usage shared memory: "+str(result.get('proc').get('mem').get('share'))
