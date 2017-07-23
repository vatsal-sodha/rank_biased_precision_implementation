"""
Created on Wed July 23 16:10:30 2017

@author: vatsal-sodha
"""

import baker
from subprocess import check_output

@baker.command

def RBP_eval(p,qrel,trecFile,range=1,save=None):
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
	index=0
	for i,row in enumerate(trecFileList):
		row=row.split(" ")
		query=row[0]+" 0 "+row[2]
		qrelRow=[x for x in qrelFileList if query in x]
		qrelRow=qrelRow[0].split(" ")
		if(qrelRow[0] == previousQid or i ==0):
			total=total+(float(qrelRow[3])/range)*(float(p)**index)
			index=index+1
		else:
			# print("index is %d" %index)
			total=(1-float(p))*total
			if save==None:
				print(previousQid+" "+str(total))
			else:
				saveFileObject.write(previousQid+" "+str(total)+"\n")
			index=0
			total=0.0
		previousQid=qrelRow[0]
	total=(1-float(p))*total
	if save== None:
		print(row[0]+" "+str(total))
	else:
		saveFileObject.write(previousQid+" "+str(total)+"\n")
		saveFileObject.close()
baker.run()