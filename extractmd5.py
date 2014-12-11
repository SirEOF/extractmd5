import re
import sys

if len(sys.argv) < 2:
	print "No file was given. Use: extractmd5.py filename"
else:
	try:
		f = open(sys.argv[1],"rb")
		data = f.read()
		f.close()
		md5s = re.findall(r'([^0-9a-fA-F])([0-9a-fA-F]{32})([^0-9a-fA-F])', data) #match any 32 long (no sorter or longer) string, which consists of 0-9a-fA-F charaters
		for item in sorted(list(set(md5s))):
			print item[1]
	except IOError:
		print "Couldn't open file: " + sys.argv[1]