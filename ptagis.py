"""
Code to retrieve data from ptagis.py 
"""

# imports
import ftplib
import pandas as pd


"""
ftp://ftp.ptagis.org/RawDataFiles/Interrogation/Loaded/158/2011/

"""
#directory to save the data files
out_dir = '../../data/effective_computing/'

def retrieve_data(year = '2005', day_of_year = '001', extension = '.A1'):
    try:
        folder = 'BO1/' # name of the folder in which contains the file you want (also the name of the damn)
        year = year + '/' #data from year 2014
        path = 'RawDataFiles/Interrogation/Loaded/' + folder + year #latter part of the url (path to file in the website)
        filename = folder[0:-1] + year[2:-1] + day_of_year + extension #'15811333.INT' #name of the file we want to download
        # first three digits are name of the folder, next 2 indicated the year
        #and the last three indicate day of year. This can be put in a loop.
        ftp = ftplib.FTP("ftp.ptagis.org") #server IP of the website we want to download from
        ftp.login() #we do not need username and password for this data
        ftp.cwd(path) #change currect working path on the website to the location where the file is
        ftp.retrbinary("RETR " + filename ,open(out_dir+filename, 'wb').write) #this will download the file into the same folder as your code
        ftp.quit()

        print(' Retrieved ' + filename)   
        
    except:
        print(' -- Failed to retrieve' + filename)
        pass

df = pd.read_csv(out_dir+filename,delim_whitespace=True, skiprows=4, skipfooter = 3, 
        engine = 'python')#last argument might not be required



