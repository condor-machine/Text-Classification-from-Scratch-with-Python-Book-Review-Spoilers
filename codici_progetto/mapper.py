# MAPPER (PROCEDURA MAPREDUCE)

import sys
 
# ricezione input
for line in sys.stdin:
	# rimozione spazi prima e dopo la stringa
	line = line.strip()

	# separazione stringa
	words = line.split()

	# output tuple
	for word in words:
		print( '%s\t%s' % (word, "1"))

