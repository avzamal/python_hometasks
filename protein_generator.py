from Bio import SeqIO


def protein_generator(fasta_file, table=1):
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        gene = seq_record.seq
        length = 3 * (len(gene)//3)
        first_protein = gene[0:length].translate(table, to_stop=True)
        yield first_protein


print(list(protein_generator("/Users/Zamalutdinov/Desktop/test.fasta")))
