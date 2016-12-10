
import numpy as np
import matplotlib.pyplot as pl
import csv
import random
#

colors = ['b','g','r','c','m','y','k']
bins = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,1,1.5,2]

# borders in nm
min_end = -2
max_end = 3

filenames_3depict = [
'vsl1_sw01_proxigram_data_3depict.txt',
'vsl1_sw02_proxigram_data_3depict.txt',
'vsl1_sw03_proxigram_data_3depict.txt',
'vsl1_sw04_proxigram_data_3depict.txt',
'vsl1_sw05_proxigram_data_3depict.txt',
'vsl1_sw06_proxigram_data_3depict.txt',
'vsl1_sw_07_proxigram_data_3depict.txt'
#'vsl1_sw15_proxigram_data_3depict.txt',
#'vsl1_sw1_proxigram_data_3depict.txt',
#'vsl1_sw2_proxigram_data_3depict.txt'
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
        
        ax2.plot(distance, conc, color=str(x/10), linewidth=2.0, label='binsize ' + str(bins[x]))
        pl.xlabel('distance / nm')
        pl.ylabel('concentration')
        pl.grid()
        pl.legend()

filenames_ivas = [
'proxi_bin_01_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv',
'proxi_bin_02_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv',
'proxi_bin_03_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv',
'proxi_bin_04_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv',
'proxi_bin_05_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv',
'proxi_bin_06_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv',
'proxi_bin_07_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv'
#'proxi_bin_1_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv' ,
#'proxi_bin_15_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv',
#'proxi_bin_2_sharp_ref_pos__number_of_precipitations_1_atomic_density_25_radius_8.csv' 
]

fig1 = pl.figure()
ax1 = fig1.add_subplot(111)

for x,f in enumerate(filenames_ivas):
    
    color = 0
    with open(f) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        conc = []
        distance = []        
        
        for num, row in enumerate(reader):     
            distance.append(row['Distance (nm)'])
            conc.append(row['Cu %'])
        
        # adapt the same sign from 3depict to ivas data
        distance = np.array([float(i)*-1 for i in distance])
        conc = np.array([float(i)/100 for i in conc])

        # cut the uninteresting sections
        indices1 = np.where(distance  > min_end)
        indices2 = np.where(distance  < max_end)
        section_of_interest = np.intersect1d(indices1,indices2)
        
        distance = np.take(distance, section_of_interest)
        conc = np.take(conc, section_of_interest)
        
        ax1.plot(distance, conc, color=str(x/10), linewidth=2.0, label='binsize ' + str(bins[x]))
        pl.xlabel('distance / nm')
        pl.ylabel('concentration')
        pl.grid()
        pl.legend()
