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
        '--fasta-output-file','shm_freq'+str(x)+'indel_l'+str(y)+'.fasta'])
    str_extr=[str(i) for i in extr]
    subprocess.call(str_extr)

#we want to have this set up so that we can choose how many parameters are inputted,
#so I need something that will allow me to control the args section through
#passing information to args.parse
