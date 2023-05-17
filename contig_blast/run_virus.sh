#!/bin/bash

elastic-blast submit --aws-region us-east-1 --query s3://elasticblast-jgiworkshop-876740315567/VIRUSCDS/virus_cds_concatenated_input.fasta --db s3://elasticblast-jgiworkshop-548634766386/TEST_ALL/all_contigs --program blastn --num-nodes 20 --results s3://elasticblast-jgiworkshop-548634766386/results/ALLCONTIGS/VIRUS1 -- -evalue 0.00001 -max_target_seqs 100  -perc_identity 95 -outfmt "6 std qlen slen"
