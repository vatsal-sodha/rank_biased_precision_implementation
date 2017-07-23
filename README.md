# rank_biased_precision_implementation
It is used to evaluate Information Retrieval System on RBP (Rank Biased Precision) matrix.

Parameters:
--p         pValue (required) ranges from 0 to 1


--qrel      qrel file (required) similar to sample.qrels


--trecFile  file in TREC Format(required)simliar to sample.txt 


--range     (default=1) Highest judged relevance label


--save      (optional) will save the output to file

How to Run:

1) When range=1 and output isn’t saved

python3.5 RBP.py RBP_eval --p 0.50 --qrel sample.qrels --trecFile sample.txt

2)Output will be saved in RBP_eval_sample.txt

python3.5 RBP.py RBP_eval --p 0.50 --qrel sample.qrels --trecFile sample.txt --save RBP_eval_sample.txt --range 3


File Formats:

.qrels file:

	 1   0   100       1
       Query-Id 0 DocumentID Relevence

TREC File:

	 1   Q0  100         -1  4.20    vatsal
      Query-Id Q0 DocumentID rank  sim     run_id
Sim is assumed to be higher for the docs to be retrieved first. 
File may contain no NULL characters. 
Lines may contain fields after the run_id; they are ignored.
This file should be sorted by sim in descending order

Output file: 
     
     Query-Id RBP-Score .

