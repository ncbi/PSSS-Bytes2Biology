This directory contains some artifacts from BLAST'ing the query sequences for PebbleScout (CDS sequences) against a database of the JGI contigs used in the BioIT hackathon on May 15-16, 2023.

Files present in the directory and notes on them:

* virus.csv
  * For virus queries
  * Two column comma separated file.  
    * First column is the number of times a query matched the contigs.  
    * Second column is the number of queries that matched this number of times

* bacteria.csv
  * For bacterial queries
  * Two column comma separated file. 
    * First column is the number of times a query matched the contigs.  
    * Second column is the number of queries that matched this number of times

* run_virus.sh
  * Script to run BLAST (with ElasticBLAST) for viral queries.  Documents the BLAST parameters used.

* run_bac.sh 
  * Script to run BLAST (with ElasticBLAST) for bacterial queries.  Documents the BLAST parameters used.

* parse_bioit_tab.py
  * Python script to parse BLAST tabular output produced by BLAST (see run_virus.sh or run_bac.sh to see BLAST -output values)
  * Produced data in virus.csv and bacteria.csv
