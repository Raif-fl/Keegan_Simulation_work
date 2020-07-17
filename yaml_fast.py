import subprocess
import numpy as np

param=np.array([[0.05,5],[0.1,9]])

x=np.zeros((len(param)))
y=np.zeros((len(param)))

for rows in param:
    x=rows[0]
    y=rows[1]
    args=(
        ['./bin/partis', 'simulate','--simulate-from-scratch', '--outfname', 'simu.yaml',
        '--scratch-mute-freq',x,'--mean-indel-length',y,'--n-sim-events', '3'])
    str_args=[str(n) for n in args]
    subprocess.call(str_args)
    extr=(
        ['./bin/extract-fasta.py', '--input-file','simu.yaml',
        '--fasta-output-file',x])
    str_extr=[str(i) for i in extr]
    subprocess.call(str_extr)













#for rows in param:
    #for cells in rows:

#x=np.zeros((len(param)))
#y=np.zeros((len(param)))
#print(x)

#for n in range(0,(len(param)-1)):
#    x[n]=param[n,0]
#    y[n]=param[n,1]
#    print(x)
#    print(y)

#parse= argparse.Argumentparser(description='run a simulation given a vector of values and output a fasta file',
#epilog='the values currently ordered as:')
#parser.add_argument(--shm_freq,-shm,default=0.5)
