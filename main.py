#!/usr/bin/python2
#Should work with both python2 and python3(i've tested with both, but mostly have tested python2

from google_images_download import google_images_download   #importing the library
import os
import sys
import random
import time

response = google_images_download.googleimagesdownload()
foundFolders = []

dird = ""
count = "1"
rands = "3"
enableRands = False
terms = ""
masterTerms = ""
includedTerm = ""
load_log=True
save_log=True

def looplas(limit, terms):
	for p in foundFolders:
		downloadlots(p, limit, terms)
		foundFolders.remove(p)

def downloadlots(dirct, limit, terms):
	if enableRands:
		rndAmount = int(rands)
		strs = masterTerms.split(",")
		amountOfTermsToGenerate = len(strs)
		termsd = [None] * amountOfTermsToGenerate
		random.seed(int(round(time.time() * 1000)))
		for p in range(0, amountOfTermsToGenerate):
			finalStr = ""
			for i in range(0, rndAmount):
				finalStr = finalStr + strs[random.randint(0, len(strs) - 1)] + " "
			finalStr[:-1]
			finalStr = finalStr + includedTerm
			termsd[p] = finalStr
		
		finalTerms = ""
		
		for i in range(0, amountOfTermsToGenerate):
			finalTerms = finalTerms + termsd[i] + ", "
		
		finalTerms[:-1]
		terms = finalTerms
		print(terms)
	else:
		terms = masterTerms
	
	terms = terms + ", " + includedTerm
	
	arguments = {"keywords":terms,"limit":limit,"print_urls":True,"output_directory":dirct, "no_directory":True}
	paths = response.download(arguments)
	print(paths)

def ma(dird, limit, terms):
	foundFolders.append(dird)
	
	for i in range(0, 10):
		for f in foundFolders:
			if (os.path.isdir(f)):
				output = [dI for dI in os.listdir(f) if os.path.isdir(os.path.join(f,dI))]
				for f1 in output:
					foundFolders.append(os.path.join(f, f1))
	
	#output = [dI for dI in os.listdir(dird) if os.path.isdir(os.path.join(dird,dI))]
	#for f in output:
	#	ot = [dF for dF in os.listdir(os.path.join(dird,f)) if os.path.isdir(os.path.join(dird, f, dF))]
	#	foundFolders.append(os.path.join(dird, f))
	#	for f2 in ot:
	#		oy = [dD for dD in os.listdir(os.path.join(dird,f,f2)) if os.path.isdir(os.path.join(dird, f, f2, dD))]
	#		foundFolders.append(os.path.join(dird, f, f2))
	#		for s in oy:
	#			foundFolders.append(os.path.join(dird, f, f2, s))
	
	looplas(limit, terms)

def writelog(dird):
	if save_log:
		logfile = os.path.join(dird, "logs.txt")
		f = open(logfile, "w+")
		for ob in foundFolders:
			f.write(ob + "\n")

def frun(dird, limit, terms, loadLog):
	try:
		if loadLog:
			logfile = os.path.join(dird, "logs.txt")
			if os.path.exists(logfile):
				print("\nAttempting to reload log file\n")
				f = open(logfile, "r")
				if f.mode == "r":
					le = f.readlines()
					for x in le:
						foundFolders.append(x.rstrip())
				print(foundFolders)
				looplas(limit, terms)
					
				if len(foundFolders) >= 1:
					looplas(limit, terms)
			else:
				print("\n Hey! Log file does not exist! \nRunning without loading log!\n")
				frun(dird, limit, terms, False)
		else:
			ma(dird, limit, terms)
		writelog(dird)
	except KeyboardInterrupt:
		print("\n Interrupted... Writing leftovers to log file.")
		writelog(dird)
		exit()

def printHelp():
	print("__________         __  .__                    .___                                     ")
	print("\______   \___.___/  |_|  |__   ____   ____   |   | _____ _____    ____   ___________  ")
	print(" |     ___<   |  \   __|  |  \ /  _ \ /    \  |   |/     \\__   \  / ___\_/ __ \_  __ \ ")
	print(" |    |    \___  ||  | |   Y  (  <_> |   |  \ |   |  Y Y  \/ __ \/ /_/  \  ___/|  | \/ ")
	print(" |____|    / ____||__| |___|  /\____/|___|  / |___|__|_|  (____  \___  / \___  |__|    ")
	print("           \/               \/            \/            \/     \/_____/      \/        ")
	print("A names.txt file needs to be placed inside the running directory, or inside the download directory.")
	print("If a names.txt file is not found in either of these diirectories then the command --terms must be used.")
	print("A log file will be created inside the run directory which allows the script to resume operation if exited before finishing the download. \n")
	print("--dir/-d				Sets the directoy for the images to be downloaded to. Usage: --dir $DIRECTORY")
	print("--count/-c				Sets the number of images per generated search term. Usage: --count $NUMBER")
	print("--rand/-r/--random			Sets whether or not to generate the search terms. Includes a number that indicates the number of words to add per term. Usage: --rand $NUMBER")
	print("--terms/-t/--term			Sets what terms to be searched, if not using a names.txt inside the image download directory or run directory. Usage: --terms $TERM $TERM $TERM")
	print("--garn/-g				Sets a word that is always at the end of the search term. Usage: --garn $TERM")
	print("--no-save-log/--ls/--ll			Prevents the saving of progress to the log file")

if __name__ == "__main__":
	try:
		argsLength = len(sys.argv)
		# this does way too many checks for nulls and may be useless but its good to be sure!
		for p in range(0, argsLength):
			arg = sys.argv[p]
			if(arg == "--dir" or arg == "-d"):
				if p + 1 <= argsLength:
					dird = sys.argv[p + 1].replace("'", '').replace("\"", '')
					if dird is None:
						print(arg + " called but information was not found!")
						exit()
				else:
					print(arg + " called but information was not found!")
					exit()
			if(arg == "--count" or arg == "-c"):
				if p + 1 < argsLength:
					count = sys.argv[p + 1].replace("'", '').replace("\"", '')
					print(count)
					print("Hello!")
					if count is None:
						print(arg + " called but information was not found!")
						exit()
				else:
					print(arg + " called but information was not found!")
					exit()
			if(arg == "--rand" or arg == "-r" or arg == "--random"):
				if p + 1 < argsLength:
					rands = sys.argv[p + 1].replace("'", '').replace("\"", '')
					enableRands = True
					if rands is None:
						print(arg + " called but information was not found!")
						exit()
				else:
					print(arg + " called but information was not found!")
					exit()
			if(arg == "--terms" or arg == "-t" or arg == "--term"):
				if p + 1 < argsLength:
					terms = sys.argv[p + 1].replace("'", '').replace("\"", '')
					if terms is None:
						print(arg + " called but information was not found!")
						exit()
				else:
					print(arg + " called but information was not found!")
					exit()
			if(arg == "--garn" or arg == "-g"):
				if p + 1 < argsLength:
					includedTerm = sys.argv[p + 1].replace("'", '').replace("\"", '')
					if includedTerm is None:
						print(arg + " called but information was not found!")
						exit()
				else:
					print(arg + " called but information was not found!")
					exit()
			if(arg == "--no-load-log" or arg == "-ll"):
				load_log = False
			if(arg == "--no-save-log" or arg == "-ls"):
				save_log = False
			
		if (dird == ""):
			print("Directroy not set! Please set with --dir or -d!")
			printHelp()
			exit()
		
		try:
			data=[]
			namesPath=os.path.join(dird, "names.txt")
			if os.path.exists(namesPath):
				with open(namesPath, 'r') as f:
					data = f.readlines()
				
				print(data)
				
				for s in data:
					masterTerms = masterTerms + s.replace("\n", '') + ", "
				
			else:
				if os.path.exists("names.txt"):
					with open("names.txt", 'r') as f:
						data = f.readlines()
					
					print(data)
					
					for s in data:
						masterTerms = masterTerms + s.replace("\n", '') + ", "
					
				else:
					print("names.txt not found. Assuming commandline usage.")
	
		except Exception as e:
			print(e)
			exit()
			
		print("Directory: " + dird)
		print("Count: " + count)
		print("Use randoms: " + str(enableRands) + ". Number of randoms: " + rands)
		print("Terms: " + masterTerms)
		
		# Please ignore how bad this code is.
		if enableRands:
			rndAmount = int(rands)
			strs = masterTerms.split(",")
			amountOfTermsToGenerate = len(strs)
			termsd = [None] * amountOfTermsToGenerate
			random.seed(int(round(time.time() * 1000)))
			for p in range(0, amountOfTermsToGenerate):
				finalStr = ""
				for i in range(0, rndAmount):
					finalStr = finalStr + strs[random.randint(0, len(strs) - 1)]
				finalStr[:-1]
				termsd[p] = finalStr
			
			finalTerms = ""
			
			for i in range(0, amountOfTermsToGenerate):
				finalTerms = finalTerms + termsd[i] + ", "
			
			finalTerms[:-1]
			terms = finalTerms
			print(terms)
		else:
			terms = masterTerms
		frun(dird, count, terms, load_log)
	except KeyboardInterrupt:
		print("\nInterrupted... Writing leftovers to log file.")
		writelog(dird)
		exit()
	#if sys.argv[1] == "--log":
	#	frun(sys.argv[2], sys.argv[4], sys.argv[3], True)
	#else:
	#	frun(sys.argv[1], sys.argv[3], sys.argv[2], False)
