This directory contains the FASTA files for the genes listed in spreadsheet WP_identifier_gene_list.xlsx.
Most of the list contains bacterial (and some viral) cds sequences obtained from [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets)
The cds sequences included in this project have been filtered based on length are are all greater than 2000 bp.

You can identify the FASTA file of your choice by querying the NC_ identifier and obtain the corresponding GCF identifier for download.
For example:
To know the GCF identifier for the gene YP_009666861.1 with NC_ identifier NC_043543.1:

*elink -db nuccore -id NC_043543.1 -target assembly | esummary | xtract -pattern DocumentSummary -element AssemblyAccession*
*GCF_004788835.1*

The Accession_to_contig_bucket_mapping.xlsx spreadsheet contains the list of accessions for which JGI has assembled contigs and provides a mapping to determine the corresponding bucket identifier when retrieving the contig sequences from s3://elasticblast-jgiworkshop-394212713216/.

The FASTA files for each of the accessions in the spreadsheet has been downloaded via SRAToolkit and are available here: s3://elasticblast-jgiworkshop-251683317823/fasta_files/.


