
import numpy as np
import matplotlib.pyplot as pl
import csv
import random
#

colors = ['b','g','r','c','m','y','k']
voxelsizes = [0.3,0.3,0.4,0.4]

wfs = ['false','true','false','true']

lineStyles = {':': '_draw_dotted', '--': '_draw_dashed', '-.': '_draw_dash_dot', '-': '_draw_solid'}
line_styles_list = list(lineStyles.keys())
# borders in nm
min_end = -1
max_end = 1

filenames_3depict = [
'WFfalse_dens50_iv05_vsl03_sw01_proxigram_data_3depict.txt',
'WFtrue_dens50_iv05_vsl03_sw01_proxigram_data_3depict.txt',
'WFfalse_dens50_iv05_vsl04_sw01_proxigram_data_3depict.txt',
'WFtrue_dens50_iv05_vsl04_sw01_proxigram_data_3depict.txt'

]

fig2 = pl.figure()
ax2 = fig2.add_subplot(111)

for x,f in enumerate(filenames_3depict):
    
    with open(f) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=' ')
        
        conc = []
        distance = []        

        for num, row in enumerate(reader):     
            distance.append(row['distance/nm'])
            conc.append(row['concentration'])
            
        distance = np.array([float(i) for i in distance])
        conc = np.array([float(i) for i in conc])
            
        # cut the uninteresting sections
        indices1 = np.where(distance  > min_end)
        indices2 = np.where(distance  < max_end)
        section_of_interest = np.intersect1d(indices1,indices2)
        
        distance = np.take(distance, section_of_interest)
        conc = np.take(conc, section_of_interest)
        
        ax2.plot(distance, conc, color=str(x/10), linestyle = line_styles_list[x] , linewidth=2.0, label='wf=' + str(wfs[x]) + ' vsl=' + str(voxelsizes[x]))
        pl.xlabel('distance / nm')
        pl.ylabel('concentration')
        pl.grid(True)
        pl.legend()
