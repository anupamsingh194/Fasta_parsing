##islands=gaps, oceans=NNN --------------> Code to find oceans and islands
import collections
import re
seq_list={}
key=""
gap= 1
no_gap=1


with open("/Users/anupamsi/Downloads/test.fasta","r") as fasta_seq:
    with open("/Users/anupamsi/Downloads/test_subset_CDCFrontier.txt","w") as fasta_seq_with_gaps:
        for line in fasta_seq:
            line=line.rstrip('\n')
            if line.startswith('>'):
                line=line.strip('>')
                key=line
                seq_list[key]=[line]
                
            else:
               seq_list[key].append(line)
        seq_list=collections.OrderedDict(sorted(seq_list.iteritems()))

        for real_key, value in seq_list.iteritems():
            value=''.join(value[1:])
            seq_list[real_key]=value
            
            islands_Dictionary =({real_key : [[real_key,(m.start(1))+1, (m.end()-1)+1] for m in re.finditer('(N+)', value)]})
            oceans_Dictionary =({real_key : [[real_key,(m.start(1))+1, (m.end()-1)+1] for m in re.finditer('([ATGC]+)', value)]})
            for real_key1, value1 in oceans_Dictionary.iteritems():
                for i, element1 in enumerate(value1):
                    value1[i].append('S'+(str(no_gap).zfill(5)))
                    no_gap+=1
                    print value1[i]
                    fasta_seq_with_gaps.write('\t'.join(str(s) for s in value1[i]) + '\n')
            for real_key2, value2 in islands_Dictionary.iteritems():
                for j, element in enumerate(value2):
                    value2[j].append('G'+(str(gap).zfill(5)))
                    gap+=1
                    print value2[j]
                    fasta_seq_with_gaps.write('\t'.join(str(s) for s in value2[j]) + '\n')
