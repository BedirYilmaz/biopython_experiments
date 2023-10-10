from Bio import SeqIO
from Bio import Align

aligner = Align.PairwiseAligner()

import json

def dump_annotations(seq):
    for key,value in seq.annotations.items():
        if key is not "abif_raw":
            print(f"{key}: {value}")



seq_list = []
for i, seq_record in enumerate(SeqIO.parse("mce1A1-4.ab1", "abi")):
    # print(i,seq_record)
    seq_list.append(seq_record)
    
dump_annotations(seq_list[0])
dump_annotations(seq_list[-1])

# the file has only one sequence in it so the first and last will match perfectly.
alignments = aligner.align(seq_list[0].seq, seq_list[-1].seq)


print(len(alignments))
for alignment in alignments:
    print(alignment)
