from google_images_download import google_images_download   #importing the library
import os
import sys

response = google_images_download.googleimagesdownload()
las = []

def looplas(limit, terms):
	for p in las:
		downloadlots(p, limit, terms)
		las.remove(p)

def downloadlots(dirct, limit, terms):
	arguments = {"keywords":terms,"limit":limit,"print_urls":True,"output_directory":dirct, "no_directory":True}
	paths = response.download(arguments)
	print(paths)

def ma(dird, limit, terms):
	las.append(dird)
	output = [dI for dI in os.listdir(dird) if os.path.isdir(os.path.join(dird,dI))]
	for f in output:
		ot = [dF for dF in os.listdir(os.path.join(dird,f)) if os.path.isdir(os.path.join(dird, f, dF))]
		las.append(os.path.join(dird, f))
		for d in ot:
			oy = [dD for dD in os.listdir(os.path.join(dird,f,d)) if os.path.isdir(os.path.join(dird, f, d, dD))]
			las.append(os.path.join(dird, f, d))
			for s in oy:
				las.append(os.path.join(dird, f, d, s))
	
	looplas(limit, terms)

def writelog(dird):
	logfile = os.path.join(dird, "logs.txt")
	f = open(logfile, "w+")
	for ob in las:
		f.write(ob + "\n")

def frun(dird, limit, terms, loadLog):
	try:
		if loadLog:
			logfile = os.path.join(dird, "logs.txt")
			if os.path.exists(logfile):
				print "\nAttempting to reload log file\n"
				f = open(logfile, "r")
				if f.mode == "r":
					le = f.readlines()
					for x in le:
						las.append(x.rstrip())
				print las
				looplas(limit, terms)
					
				if len(las) >= 1:
					looplas(limit, terms)
			else:
				print "\nHey! Log file does not exist! \nRunning without loading log!\n"
				frun(dird, limit, terms, False)
		else:
			ma(dird, limit, terms)
		writelog(dird)
	except KeyboardInterrupt:
		print "\nInterrupted... Writing leftovers to log file."
		writelog(dird)
		exit()

def printHelp():
	print("Format is python-imager (DIR) (# OF IMAGES)")

if __name__ == '__main__':
	amount = sys.argv[2]
	dird = sys.argv[1]
	terms = sys.argv[3]
	
	if len(sys.argv) < 3:
		printHelp()
		exit()
	
	print(sys.argv)
	if sys.argv[1] == "":
		printHelp()
		exit()
		
	if sys.argv[2] == "":
		printHelp()
		exit()
		
	try:
		data=[]
		if os.path.exists(dird + "/" + "names.txt"):
			with open(dird + "/" +'names.txt', 'r') as f:
				data = f.readlines()
			
			print(data)
			print("\n")
			
			for s in data:
				terms = terms + s.replace("\n", '') + ", "
			
			print(terms)
			print("\n")
			
			frun(dird, amount, terms, True)
		else:
			print("names.txt not found. Assuming commandline usage.")
			frun(dird, amount, terms, True)
		
	except Exception as e:
		print(e)
		print("\n")
		
		exit()
	
	
	#if sys.argv[1] == "--log":
	#	frun(sys.argv[2], sys.argv[4], sys.argv[3], True)
	#else:
	#	frun(sys.argv[1], sys.argv[3], sys.argv[2], False)
