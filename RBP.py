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
	qrelDict,trecDict=createDict(qrelFileList,trecFileList)
	print(trecDict)
	# print(trecDict["e5368b93d83ef87bf24e32820d85d2e96ab6ec07"])

	average=calculateRBP(p,gmax,qrelDict,trecDict)
	return(average)
	# print(trecDict)
@baker.command
def calculateRBP(p,gmax,qrelDict,trecDict):
	grandTotal=0.0
	noOfKeys=0
	for key in trecDict:
		total=0.0
		for index,value in enumerate(trecDict[key]):
			r=[x[2] for x in qrelDict[key] if x[1] == value[1]]
			r=float("".join(r))/float(gmax)
			# print(str(r)+" "+key+" "+str(value[1]))
			total+=r*(float(p)**(index))
		total=total*(1-float(p))
		print(key+" "+str(total))
		grandTotal+=total
		noOfKeys+=1
	print("Average is %f for %d number of queries"%(grandTotal/noOfKeys,noOfKeys))
	return(grandTotal/noOfKeys)
#this function create dict from file
@baker.command
def createDict(qrelFileList,trecFileList):
	qrelDict={}
	trecDict={}
	for qrelRow in qrelFileList:
		qrelRow=qrelRow.split(" ")
		if "".join(qrelRow[0]) in qrelDict:
			qrelDict["".join(qrelRow[0])].append(qrelRow[1:])
		else:
			qrelDict["".join(qrelRow[0])]=[]
			qrelDict["".join(qrelRow[0])].append(qrelRow[1:])


	for trecRow in trecFileList:
		trecRow=trecRow.split(" ")
		if "".join(trecRow[0]) in trecDict:
			trecDict["".join(trecRow[0])].append(trecRow[1:])
		else:
			trecDict["".join(trecRow[0])]=[]
			trecDict["".join(trecRow[0])].append(trecRow[1:])
	#sorting trecDict by score
	for key in trecDict:
		row=sorted(trecDict[key],key=lambda x:(float(x[3])),reverse=True)
		trecDict[key]=row
	return(qrelDict,trecDict)

if __name__ == '__main__':
    baker.run()