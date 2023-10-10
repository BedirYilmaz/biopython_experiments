from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

seq_list = []
for i, seq_record in enumerate(SeqIO.parse("ls_orchid.fasta", "fasta")):
    print(i,seq_record)
    seq_list.append(seq_record)
    
alignments = pairwise2.align.globalxx(seq_list[0].seq, seq_list[-1].seq)


print(len(alignments))
for alignment in alignments:
    print(format_alignment(*alignment))
    print(alignment.score, alignment.end - alignment.start, len(alignment.seqA), len(alignment.seqB))
