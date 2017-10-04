contents = open('./proxy_raw.txt').readlines()
out = open('./80proxy.txt', 'w')

for line in contents:
	words = line.split('\t')
	proxy = 'http://' + words[0] + ':' + words[1]
	out.write(proxy + '\n')

out.close()

import os
print os.path.dirname(os.path.dirname(os.path.abspath(__file__)), 'proxy')
