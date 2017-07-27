"""
Created on Wed July 23 16:10:30 2017

@author: vatsal-sodha
"""

import baker
from subprocess import check_output

@baker.command

def RBP_eval(p,qrel,trecFile,gmax=1,save=None):
	qrelFileObject=open(qrel,"r",newline='')
	trecFileObject=open(trecFile,"r",newline='')
	qrelFileList= qrelFileObject.readlines()
	trecFileList=trecFileObject.readlines()
	qrelFileObject.close()
	trecFileObject.close()
	if save != None:
		saveFileObject=open(save,"w",newline='')
	else:	
		print("QId"+" "+"RBP Score")
	previousQid=""
	total=0.0
	grandTotal=0.0
	noOfQuery=0
	index=0
	for i,row in enumerate(trecFileList):
		row=row.split(" ")
		query=row[0]+" 0 "+row[2]
		qrelRow=[x for x in qrelFileList if query in x]
		qrelRow=qrelRow[0].split(" ")
		if(qrelRow[0] == previousQid or i ==0):
			total=total+(float(qrelRow[3])/gmax)*(float(p)**index)
			index=index+1
		else:
			# print("index is %d" %index)
			total=(1-float(p))*total
			grandTotal+=total
			if save==None:
				print(previousQid+" "+"{0:.4f}".format(total))
			else:
				saveFileObject.write(previousQid+" "+"{0:.4f}".format(total)+"\n")
			index=0
			total=0.0
			noOfQuery+=1
		previousQid=qrelRow[0]
	total=(1-float(p))*total
	grandTotal+=total
	noOfQuery+=1
	if save== None:
		print(row[0]+" "+"{0:.4f}".format(total))
		print("Average is {0:.4f}".format(grandTotal/noOfQuery))
	else:
		saveFileObject.write(previousQid+" "+"{0:.4f}".format(total)+"\n")
		saveFileObject.write("Average is {0:.4f}".format(grandTotal/noOfQuery))

		saveFileObject.close()
baker.run()