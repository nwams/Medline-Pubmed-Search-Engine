# Medline-Pubmed-Search-Engine
mapped with CPT and ICD codes

### Only required to do this one-time!
	1.	Download metamap 2012 https://metamap.nlm.nih.gov/MainDownload.shtml. It’s a large file and will take a while 
	  * Note: Specifically must be version 2012, because it’s what was tested and created by Anthony Rios, the author of Python Metamap wrapper 
	2.	unzip it - this will take a while 
	3.	detailed install instructions can be found by following the instructions here https://buttelab.stanford.edu/metamap#installation or here https://metamap.nlm.nih.gov/Installation.shtml#Stopping the servers 
	  1. cd public_mm 
	  2. export JAVA_HOME=/System/Library/Frameworks/System/Library/Frameworks/JavaVM.framework/Versions/1.6/Home/ 
	  3. export PATH=$PATH:$JAVA_HOME/bin:/Users/nwams/Documents/MetaMap/public_mm/bin 
	  4. ./bin/install.sh 
	  5. click the enter button twice 
	  6. ./bin/skrmedpostctl start 
	  7. ./bin/wsdserverctl start 
	  8. ./bin/metamap12 
	4.	Download this Python metamap wrapper: https://github.com/AnthonyMRios/pymetamap  
	5.	I created an app.py file in the pymetamap folder 
	6.	I created a folder called “Code” to store the cpt and ics csv files. Note that for ICD code, DX means diagnosis while SG means procedure. ICD codes in the CSV file start on row 915.  
	7.	[MH_items](https://mbr.nlm.nih.gov/Download/) here and [description](https://mbr.nlm.nih.gov/Reference/MEDLINE_Baseline_Repository_Detail.pdf) here 

### Must Do This Manually Each Time Before Use
To start the MetaMap servers:
	1.	In command line, cd into the public_mm folder 
	2.	enter the following ./bin/skrmedpostctl start 
	3.	enter the following command ./bin/wsdserverctl start 
