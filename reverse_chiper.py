import sys
import getopt
class cipher:
	def usage(self):
		usage1="""\
		tool -d|--decode
		tool -e|--encode
		"""
		return usage1
	def main(self):
		mes=sys.stdin.read()
		tran=""
		i=len(mes)-1
		while i>=0:
			tran=tran+mes[i]
			i=i-1
		if enco:
			print("encode mes \n")
			print(tran)
		else:
			print("decode mes \n")
			print(tran[::-1][::-1])

obj=cipher()
global enco
if not len(sys.argv[1:]):
	print('ERR')
	print(obj.usage())
	sys.exit(1)

try:
	opts,args=getopt.getopt(sys.argv[1:],"de",["decode","encode"])
except getopt.GetoptError as err:
	print(err)
	print(obj.usage())
	#print("EEEEEEEEEEEEEEEEEEE")
	sys.exit(2)

for o, a in opts:
	if o in ('-d','--decode'):
		enco=False
	elif o in ('-e','--encode'):
		enco=True
	else:
			print("ERR")
			print(obj.usage())
			sys.exit(1)
obj.main()
