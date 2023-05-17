#!/usr/bin/env python3
import sys

#  
# ===========================================================================
#
#                            PUBLIC DOMAIN NOTICE
#               National Center for Biotechnology Information
#
#  This software/database is a "United States Government Work" under the
#  terms of the United States Copyright Act.  It was written as part of
#  the author's official duties as a United States Government employee and
#  thus cannot be copyrighted.  This software/database is freely available
#  to the public for use. The National Library of Medicine and the U.S.
#  Government have not placed any restriction on its use or reproduction.
#
#  Although all reasonable efforts have been taken to ensure the accuracy
#  and reliability of the software and data, the NLM and the U.S.
#  Government do not and cannot warrant the performance or results that
#  may be obtained by using this software or data. The NLM and the U.S.
#  Government disclaim all warranties, express or implied, including
#  warranties of performance, merchantability or fitness for any particular
#  purpose.
#
#  Please cite the author in any work or product based on this material.
#
# ===========================================================================
#
# Authors:  Tom Madden
#


# parse tabular file using -outfmt '7 std qlen slen'

# Read in 14 fields.  Look at query and subject length
def GetMatches(f, ident_cutoff, coverage_cutoff, verbose):
 last_subj = "NONE"
 last_query = "NONE"
 good_matches = 0
 q_dic = {}
 for x in f:
  line = x.split()
  if line[0] == "#":
   continue
  query = line[0]
  subj = line[1]
  ident = float(line[2])
  align_len = int(line[3])
  qlen = int(line[12])
  slen = int(line[13])
# only first HSP per subject
  if last_subj == subj:
   continue
  coverage_diff = float(align_len)/float(min(qlen, slen))
#  print("{0} {1} {2:4.2f} {3} {4} {5} {6:4.2f}".format(query, subj, ident, qlen, slen, align_len, coverage_diff))
  if ident > ident_cutoff and coverage_diff > coverage_cutoff:
    if verbose:
      print("{0} {1} {2:4.2f} {3} {4} {5} {6:4.2f}".format(query, subj, ident, qlen, slen, align_len, coverage_diff))
    if query in q_dic.keys():
      num = q_dic[query]
      q_dic[query] = num+1
    else:
      q_dic[query] = 1
    good_matches = good_matches + 1
  last_subj = line[1]
 if verbose:
   print("Good matches: {0}".format(good_matches))

 if verbose:
   for x in sorted(q_dic, key=q_dic.get, reverse=True):
     print("{0} {1}".format(x, q_dic[x]))

 hist_dic = {}
 for x in q_dic.values():
   if x in hist_dic.keys():
     num = hist_dic[x]
     hist_dic[x] = num + 1
   else:
     hist_dic[x] = 1

 #for x in sorted(hist_dic, key=hist_dic, reverse=True):
 for x in sorted(hist_dic):
   print("{0} , {1}".format(x, hist_dic[x]))

   


def main():
 if len(sys.argv) != 5:
  sys.stderr.write("Usage: %s input-file, percent-ident-match, frac-length-diff verbose \n"% sys.argv[0])
  sys.exit(1) 


 startInputFile = sys.argv[1]
 f1 = open(startInputFile, "r")
 perc_ident = int(sys.argv[2])
 coverage = float(sys.argv[3])
 verbose = int(sys.argv[4])
 if verbose:
   print("Processing: {0}".format(sys.argv[1]))
 GetMatches(f1, perc_ident, coverage, verbose)
 f1.close()
 

if __name__ == "__main__":
 main()
