import builtins
import sys
import getopt
import argparse
import compago

def add(list):
	list = map(int, list)
	sum = 0
	for i in list:
		sum += i
	print('{0} {1} '.format('sum =', sum))

def sub(list):
	list = map(int, list)
	sum = list[0]
	for i in list[1:]:
		sum -= i
	print('{0} {1} '.format('sum =', sum))

def mult(list):
	list = map(int, list)
	sum = list[0]
	for i in list[1:]:
		sum *= i
	print('{0} {1} '.format('sum =', sum))

def div(list):
	list = map(int, list)
	sum = list[0]
	for i in list[1:]:
		sum /= i
	print('{0} {1} '.format('sum =', sum))

def help():
	print("		-h for help")
	print("		-a [1, 2, 3, ...] for add")
	print("		-s [1, 2, 3, ...] for subtract")
	print("		-m [1, 2, 3, ...] for multiply")
	print("		-d [1, 2, 3, ...] for divide")
	print("		-g [name] for greeting")
	print("		-u [name] for ungreeting")
	print("		-f for reading file")

def readFile():
	try:
		file = open("read.txt", "r+")
		for line in file:
			print line
	except IOError:
		print "File not found"

def greet(to="world"):
	print "Hello,", to, "!"

def ungreet(to="world"):
	print "Goodbye,", to, "!"

def main():
	try:
		opts, arg = getopt.getopt(sys.argv[1:], "hasmdguf")
	except getopt.GetoptError as err:
		print str(err)
		sys.exit(2)
		
	for o, a in opts:
		if o in ("-h", "--help"):
			help()
			sys.exit()
		elif o == "-a":
			list = sys.argv[2:]
			add(list)
			sys.exit()
		elif o == "-s":
			list = sys.argv[2:]
			sub(list)
			sys.exit()
		elif o == "-m":
			list = sys.argv[2:]
			mult(list)
			sys.exit()
		elif o == "-d":
			list = sys.argv[2:]
			div(list)
			sys.exit()
		elif o == "-g":
			greet(sys.argv[2])
			sys.exit()
		elif o == "-u":
			ungreet(sys.argv[2])
			sys.exit()
		elif o == "-f":
			readFile()
			sys.exit()
		else:
			assert False, "Wrong Option"
	print("Hello World")

main()