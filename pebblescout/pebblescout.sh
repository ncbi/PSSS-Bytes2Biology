#!/bin/sh
# Script to run PebbleScout from a Unix command line.
# Make sure this script is executable with chmod +x pebblescout.sh

if [ $# -ne 1 ]; then
  echo "Usage: $0 query.fa\n  Where query.fa is a FASTA file containing your PebbleScout query.\n"
  exit
fi

if [ ! -f $1 ]; then
  echo "File $1 not found!"
  exit
fi

# FASTA file to upload (command-line parameter).
FILENAME=$1

# Alternately, id-acc parameter could be used to query by accession.


# The database, one of:
# meta - Metagenomic
# wgs - WGS
# refseq - RefSeq
# run - PH3HS_Runs
# biosample - PH3HS_Biosample
# hrna_2021 - Human RNAseq 2021
DATABASE=meta

# Masking threshold (min: 1, max: 3500000)
MASK_THRESH=5663

# Score constant (min: 1, max: 1000000)
SCORE_CONSTANT=13000

# Max number of subjects per query (min: 1, max: 100000)
MAX_SUBJECTS=100

URL="https://pebblescout.ncbi.nlm.nih.gov/sra-cl-be/sra-cl-be.cgi?rettype=pebblescout&m=2&id-report=download&db=$DATABASE&g=$MASK_THRESH&c=$SCORE_CONSTANT&_r=$MAX_SUBJECTS"

curl -X POST "$URL" -F "fasta_file=@$1"

