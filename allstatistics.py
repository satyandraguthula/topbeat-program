import json
process=open("process.txt", 'w')
filesystem=open("filesystem.txt", 'w')
system=open("system.txt", 'w')
try:
	with open("//tmp//topbeat//topbeat") as f:
		content = f.readlines()
		for i in range(0,len(content)):
		    result = json.loads(content[i])  
		    if (result is None)or (len(result)==0):
		        continue
		    else:
				if(result.get('type')=="process"):
					process.write("Process name: "+result.get('proc').get('name')+"\n\t PARENT PID: "+str(result.get('proc').get('ppid'))+"\n\t STATE: "+result.get('proc').get('state')+"\n\t CPU usage user: "+str(result.get('proc').get('cpu').get('user'))+"\n\t CPU usage user percentage: "+str(result.get('proc').get('cpu').get('user_p'))+"\n\t CPU usage system: "+str(result.get('proc').get('cpu').get('system'))+"\n\t CPU usage total: "+str(result.get('proc').get('cpu').get('total'))+"\n\t CPU usage start time: "+str(result.get('proc').get('cpu').get('start_time'))+"\n\t Memory usage virtual memory: "+str(result.get('proc').get('mem').get('size'))+"\n\t Memory usage resident memory: "+str(result.get('proc').get('mem').get('rss'))+"\n\t Memory usage resident memory percentage: "+str(result.get('proc').get('mem').get('rss_p'))+"\n\t Memory usage shared memory: "+str(result.get('proc').get('mem').get('share'))+"\n")
				elif(result.get('type')=="filesystem"):
					filesystem.write("Disk name:"+result.get('fs').get('device_name')+"\n\t Mounted at "+result.get('fs').get('mount_point')+"\n\t Total space"+str(result.get('fs').get('total'))+"\n\t Used space "+str(result.get('fs').get('used'))+"\n\t Used space percentage "+str(result.get('fs').get('used_p'))+"\n\t Free space "+str(result.get('fs').get('free'))+"\n\t Available space "+str(result.get('fs').get('avail'))+"\n")
				elif(result.get('type')=="system"):
					system.write("System\n\t Load in the last minute: "+str(result.get('load').get('load1'))+"\n\t Load in last 5 minutes "+str(result.get('load').get('load5'))+"\n\t Load in last 15 minutes "+str(result.get('load').get('load15'))+"\n\t User CPU usage "+str(result.get('cpu').get('user'))+"\n\t User CPU usage percentage "+str(result.get('cpu').get('user_p'))+"\n\t System CPU usage "+str(result.get('cpu').get('system'))+"\n\t System CPU usage percentage "+str(result.get('cpu').get('system_p'))+"\n\t CPU idle "+str(result.get('cpu').get('idle'))+"\n\t IOWait "+str(result.get('cpu').get('iowait'))+"\n\t Hardware interrupt handling "+str(result.get('cpu').get('irq'))+"\n\t Software interrupt handling "+str(result.get('cpu').get('softirq'))+"\n\t Total memory "+str(result.get('mem').get('total'))+"\n\t Used memory "+str(result.get('mem').get('used'))+"\n\t Used memory percentage "+str(result.get('mem').get('used_p'))+"\n\t Free memory "+str(result.get('mem').get('free'))+"\n\t actual memory used "+str(result.get('mem').get('actual_used'))+"\n\t actual memory free "+str(result.get('mem').get('actual_free'))+"\n\t actual memory used percentage "+str(result.get('mem').get('actual_used_p'))+"\n\t Total swap memory "+str(result.get('swap').get('total'))+"\n\t Swap memory used "+str(result.get('swap').get('used'))+"\n\t Swap memory free "+str(result.get('swap').get('free'))+"\n\t Acuta swap memory used "+str(result.get('swap').get('actual_used'))+"\n\t Actual swap memory free "+str(result.get('swap').get('actual_free'))+"\n\t Actual swap memory used percentage "+str(result.get('swap').get('actual_used_p'))+"\n")
	f.close()
	with open("//tmp//topbeat//topbeat.1") as f:
		content = f.readlines()
		for i in range(0,len(content)):
		    result = json.loads(content[i])  
		    if (result is None)or (len(result)==0):
		        continue
		    else:
				if(result.get('type')=="process"):
					process.write("Process name: "+result.get('proc').get('name')+"\n\t PARENT PID: "+str(result.get('proc').get('ppid'))+"\n\t STATE: "+result.get('proc').get('state')+"\n\t CPU usage user: "+str(result.get('proc').get('cpu').get('user'))+"\n\t CPU usage user percentage: "+str(result.get('proc').get('cpu').get('user_p'))+"\n\t CPU usage system: "+str(result.get('proc').get('cpu').get('system'))+"\n\t CPU usage total: "+str(result.get('proc').get('cpu').get('total'))+"\n\t CPU usage start time: "+str(result.get('proc').get('cpu').get('start_time'))+"\n\t Memory usage virtual memory: "+str(result.get('proc').get('mem').get('size'))+"\n\t Memory usage resident memory: "+str(result.get('proc').get('mem').get('rss'))+"\n\t Memory usage resident memory percentage: "+str(result.get('proc').get('mem').get('rss_p'))+"\n\t Memory usage shared memory: "+str(result.get('proc').get('mem').get('share'))+"\n")
				elif(result.get('type')=="filesystem"):
					filesystem.write("Disk name:"+result.get('fs').get('device_name')+"\n\t Mounted at "+result.get('fs').get('mount_point')+"\n\t Total space"+str(result.get('fs').get('total'))+"\n\t Used space "+str(result.get('fs').get('used'))+"\n\t Used space percentage "+str(result.get('fs').get('used_p'))+"\n\t Free space "+str(result.get('fs').get('free'))+"\n\t Available space "+str(result.get('fs').get('avail'))+"\n")
				elif(result.get('type')=="system"):
					system.write("System\n\t Load in the last minute: "+str(result.get('load').get('load1'))+"\n\t Load in last 5 minutes "+str(result.get('load').get('load5'))+"\n\t Load in last 15 minutes "+str(result.get('load').get('load15'))+"\n\t User CPU usage "+str(result.get('cpu').get('user'))+"\n\t User CPU usage percentage "+str(result.get('cpu').get('user_p'))+"\n\t System CPU usage "+str(result.get('cpu').get('system'))+"\n\t System CPU usage percentage "+str(result.get('cpu').get('system_p'))+"\n\t CPU idle "+str(result.get('cpu').get('idle'))+"\n\t IOWait "+str(result.get('cpu').get('iowait'))+"\n\t Hardware interrupt handling "+str(result.get('cpu').get('irq'))+"\n\t Software interrupt handling "+str(result.get('cpu').get('softirq'))+"\n\t Total memory "+str(result.get('mem').get('total'))+"\n\t Used memory "+str(result.get('mem').get('used'))+"\n\t Used memory percentage "+str(result.get('mem').get('used_p'))+"\n\t Free memory "+str(result.get('mem').get('free'))+"\n\t actual memory used "+str(result.get('mem').get('actual_used'))+"\n\t actual memory free "+str(result.get('mem').get('actual_free'))+"\n\t actual memory used percentage "+str(result.get('mem').get('actual_used_p'))+"\n\t Total swap memory "+str(result.get('swap').get('total'))+"\n\t Swap memory used "+str(result.get('swap').get('used'))+"\n\t Swap memory free "+str(result.get('swap').get('free'))+"\n\t Acuta swap memory used "+str(result.get('swap').get('actual_used'))+"\n\t Actual swap memory free "+str(result.get('swap').get('actual_free'))+"\n\t Actual swap memory used percentage "+str(result.get('swap').get('actual_used_p'))+"\n")
	f.close()
	with open("//tmp//topbeat//topbeat.2") as f:
		content = f.readlines()
		for i in range(0,len(content)):
		    result = json.loads(content[i])  
		    if (result is None)or (len(result)==0):
		        continue
		    else:
				if(result.get('type')=="process"):
					process.write("Process name: "+result.get('proc').get('name')+"\n\t PARENT PID: "+str(result.get('proc').get('ppid'))+"\n\t STATE: "+result.get('proc').get('state')+"\n\t CPU usage user: "+str(result.get('proc').get('cpu').get('user'))+"\n\t CPU usage user percentage: "+str(result.get('proc').get('cpu').get('user_p'))+"\n\t CPU usage system: "+str(result.get('proc').get('cpu').get('system'))+"\n\t CPU usage total: "+str(result.get('proc').get('cpu').get('total'))+"\n\t CPU usage start time: "+str(result.get('proc').get('cpu').get('start_time'))+"\n\t Memory usage virtual memory: "+str(result.get('proc').get('mem').get('size'))+"\n\t Memory usage resident memory: "+str(result.get('proc').get('mem').get('rss'))+"\n\t Memory usage resident memory percentage: "+str(result.get('proc').get('mem').get('rss_p'))+"\n\t Memory usage shared memory: "+str(result.get('proc').get('mem').get('share'))+"\n")
				elif(result.get('type')=="filesystem"):
					filesystem.write("Disk name:"+result.get('fs').get('device_name')+"\n\t Mounted at "+result.get('fs').get('mount_point')+"\n\t Total space"+str(result.get('fs').get('total'))+"\n\t Used space "+str(result.get('fs').get('used'))+"\n\t Used space percentage "+str(result.get('fs').get('used_p'))+"\n\t Free space "+str(result.get('fs').get('free'))+"\n\t Available space "+str(result.get('fs').get('avail'))+"\n")
				elif(result.get('type')=="system"):
					system.write("System\n\t Load in the last minute: "+str(result.get('load').get('load1'))+"\n\t Load in last 5 minutes "+str(result.get('load').get('load5'))+"\n\t Load in last 15 minutes "+str(result.get('load').get('load15'))+"\n\t User CPU usage "+str(result.get('cpu').get('user'))+"\n\t User CPU usage percentage "+str(result.get('cpu').get('user_p'))+"\n\t System CPU usage "+str(result.get('cpu').get('system'))+"\n\t System CPU usage percentage "+str(result.get('cpu').get('system_p'))+"\n\t CPU idle "+str(result.get('cpu').get('idle'))+"\n\t IOWait "+str(result.get('cpu').get('iowait'))+"\n\t Hardware interrupt handling "+str(result.get('cpu').get('irq'))+"\n\t Software interrupt handling "+str(result.get('cpu').get('softirq'))+"\n\t Total memory "+str(result.get('mem').get('total'))+"\n\t Used memory "+str(result.get('mem').get('used'))+"\n\t Used memory percentage "+str(result.get('mem').get('used_p'))+"\n\t Free memory "+str(result.get('mem').get('free'))+"\n\t actual memory used "+str(result.get('mem').get('actual_used'))+"\n\t actual memory free "+str(result.get('mem').get('actual_free'))+"\n\t actual memory used percentage "+str(result.get('mem').get('actual_used_p'))+"\n\t Total swap memory "+str(result.get('swap').get('total'))+"\n\t Swap memory used "+str(result.get('swap').get('used'))+"\n\t Swap memory free "+str(result.get('swap').get('free'))+"\n\t Acuta swap memory used "+str(result.get('swap').get('actual_used'))+"\n\t Actual swap memory free "+str(result.get('swap').get('actual_free'))+"\n\t Actual swap memory used percentage "+str(result.get('swap').get('actual_used_p'))+"\n")
	f.close()
finally:
	process.close()
	filesystem.close()
	system.close()
