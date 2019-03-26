import sys
#why
import getopt
import urllib
from urllib import request
import pickle

def getinfo(idx):
	try:


	    urli = "http://replbox.repl.it/data/web_hosting_1/InventorX/Memebean/" + idx +"info.txt"
	    print(urli)
	    datadown = urllib.request.urlretrieve(urli,"info.txt")
	    file = open("info.txt","rb")
	    infodata = pickle.load(file)
	    print(infodata)
	except:
	    print("Error, most likily no connecton to the internet")

def install(idx):
    try:
        url = "http://replbox.repl.it/data/web_hosting_1/InventorX/Memebean/" + idx +".py"
        datadown = urllib.request.urlretrieve(url, filename=idx + ".py")
    except:
        print("error")
def main(argv):
    
    try:
        opts, args = getopt.getopt(argv,"i:d:",["ifile=","dfile="])
        modei = 0
        moded = 0
    except getopt.GetoptError:
        print(opts,args)
        print ('test.py -d <packagename> or -i<package_name_for_info_get>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( 'test.py -d <packagename> or -i<package_name_for_info_get>i')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            infofile = arg
            modei = 1
            print("Getting info")
        elif opt in ("-d", "--dfile"):
            downfile = arg
            print("Downloading")
            moded = 1
    if modei == 1:
        getinfo(infofile)
    if moded == 1:
        install(downfile)
        
		
	   
if __name__ == "__main__":
    main(sys.argv[1:])
