#!/usr/bin/env python

import numpy as np
import pylab as plt
import glob as glob
import os
import pandas as pd


#nAtoms = int(df1.iloc[0,0])
nAtoms = 792 
##nGeomSteps = int(df1.iloc[-nAtoms-1,2]) # step number is written in 3rd column of geom.out.xyz
nGeomSteps = 15613

atom_list_1 = np.array(list(range(0,792)))
atom_list_2 = np.array(list(range(429,444))+list(range(777,792)))
atom_list_3 = np.array(list(range(0,96)))
atom_list_4 = np.array(list(range(96,429))+list(range(444,777)))

fig, ax = plt.subplots(figsize=(10,10))
array = np.zeros(nGeomSteps+1)
for i in range(0,len(atom_list_1)):
    df=pd.read_csv("%d.txt" %atom_list_1[i], header=None, delimiter=r"\s+",
            names=["index", "charge"])
    for j in range(0,nGeomSteps+1):
        array[j] = array[j] + df.iloc[j,1]
ax.plot(df["index"]*0.3/1000,array,linewidth=4.0, label='all')

array = np.zeros(nGeomSteps+1)
for i in range(0,len(atom_list_2)):
    df=pd.read_csv("%d.txt" %atom_list_2[i], header=None, delimiter=r"\s+",
            names=["index", "charge"])
    for j in range(0,nGeomSteps+1):
        array[j] = array[j] + df.iloc[j,1]
ax.plot(df["index"]*0.3/1000,array,linewidth=4.0, label='Mg(PF6)2')

array = np.zeros(nGeomSteps+1)
for i in range(0,len(atom_list_3)):
    df=pd.read_csv("%d.txt" %atom_list_3[i], header=None, delimiter=r"\s+",
        names=["index", "charge"])
    for j in range(0,nGeomSteps+1):
        array[j] = array[j] + df.iloc[j,1]
ax.plot(df["index"]*0.3/1000,array,linewidth=4.0, label='Mg surface')

array = np.zeros(nGeomSteps+1)
for i in range(0,len(atom_list_4)):
    df=pd.read_csv("%d.txt" %atom_list_4[i], header=None, delimiter=r"\s+",
        names=["index", "charge"])
    for j in range(0,nGeomSteps+1):
        array[j] = array[j] + df.iloc[j,1]
ax.plot(df["index"]*0.3/1000,array,linewidth=4.0, label='G4 solvent')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size' : '22'}


ax.legend(loc='lower left', prop={'size':20})
ax.yaxis.set_ticks_position('both')
ax.set_title("Mg(PF6)2 in 18 G4 all",pad=20)
ax.set_xlabel("Time step [ps]",fontsize=30)
ax.set_ylabel("Charge [e]",fontsize=30)
ax.tick_params(labelsize=20)
plt.show()



#for i in range(0,len(atom_list_4)):
#    df=pd.read_csv("%d.txt" %atom_list_4[i], header=None,names=["charge"])
#    for j in range(0,nGeomSteps):
#        array[j] = array[j] + df.iloc[j]
#plt.plot(range(0,nGeomSteps),array)
#
#
#for i in range(0,len(atom_list_5)):
#    df=pd.read_csv("%d.txt" %atom_list_5[i], header=None,names=["charge"])
#    for j in range(0,nGeomSteps):
#        array[j] = array[j] + df.iloc[j]
#plt.plot(range(0,nGeomSteps),array)
#
#
#for i in range(0,len(atom_list_6)):
#    df=pd.read_csv("%d.txt" %atom_list_6[i], header=None,names=["charge"])
#    for j in range(0,nGeomSteps):
#        array[j] = array[j] + df.iloc[j]
#plt.plot(range(0,nGeomSteps),array)
#
#
#for i in range(0,len(atom_list_7)):
#    df=pd.read_csv("%d.txt" %atom_list_7[i], header=None,names=["charge"])
#    for j in range(0,nGeomSteps):
#        array[j] = array[j] + df.iloc[j]
#plt.plot(range(0,nGeomSteps),array)


plt.show()




## CF3SO2N
##atom_list = [662,663,664,665,666,667,668,669]
#
## SO2
##atom_list = [659,660,661]
#
## CF3
##atom_list = [655,656,657,658]
#
### TFSI 1
#atom_list_1 = np.array([425,426,427,428,429,430,431,432,433,434,435,436,437,438,439])
##
### TFSI 2
#atom_list_2 = np.array([440,441,442,443,444,445,446,447,448,449,450,451,452,453,454])
##
### TFSI 3
#atom_list_3 = np.array([800,801,802,803,804,805,806,807,808,809,810,811,812,813,814])
##
### TFSI 4
#atom_list_4 = np.array([785,786,787,788,789,790,791,792,793,794,795,796,797,798,799])
#
## PC
##atom_list = [382,383,384,385,386,387,388,389,390,391,392,393,394]
#
## Mg 1st layer
##atom_list = [766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781]
#
## Mg 2nd layer
##atom_list = [750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765]
#
## Mg 3rd layer
##atom_list = [734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749]
#
## Mg 4th layer
##atom_list = [718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733]
#
## Mg 5th layer
##atom_list = [702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717]
#
## Mg 6th layer
##atom_list = [686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701]
#
## Mg whole layer
##atom_list = [766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,
##            750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,
##            734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,
##            718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,
##            702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,
##            686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701]
#
## PC 1st layer
##atom_list=[382,383,384,385,386,387,388,389,390,391,392,393,394,
##           421,422,423,424,425,426,427,428,429,430,431,432,433,
##           343,344,345,346,347,348,349,350,351,352,353,354,355,
##           473,474,475,476,477,478,479,480,481,482,483,484,485,
##           486,487,488,489,490,491,492,493,494,495,496,497,498]
#
## PC 1
##atom_list=[421,422,423,424,425,426,427,428,429,430,431,432,433]
#
## Mg cation
##atom_list = [342]
#
#grpdat=df1.groupby('atom_nr')
##for i in range(0,nGeomSteps+1):
##    array.append(grpdat.get_group(atom_list[0])['real'].values[i])
##for i in range(0,nGeomSteps+1):
##    for j in range(1,len(atom_list)):
##        array[i]=array[i]+grpdat.get_group(atom_list[j])['real'].values[i]
##
#
#for i in range(0,nGeomSteps+1):
#    array_1=np.append(array_1,grpdat.get_group(atom_list_1[0])['real'].values[i])
#for i in range(0,nGeomSteps+1):
#    for j in range(1,len(atom_list_1)):
#        array_1[i]=array_1[i]+grpdat.get_group(atom_list_1[j])['real'].values[i]
#
#for i in range(0,nGeomSteps+1):
#    array_2=np.append(array_2,grpdat.get_group(atom_list_2[0])['real'].values[i])
#for i in range(0,nGeomSteps+1):
#    for j in range(1,len(atom_list_2)):
#        array_2[i]=array_2[i]+grpdat.get_group(atom_list_2[j])['real'].values[i]
#
#for i in range(0,nGeomSteps+1):
#    array_3=np.append(array_3,grpdat.get_group(atom_list_3[0])['real'].values[i])
#for i in range(0,nGeomSteps+1):
#    for j in range(1,len(atom_list_3)):
#        array_3[i]=array_3[i]+grpdat.get_group(atom_list_3[j])['real'].values[i]
#
#for i in range(0,nGeomSteps+1):
#    array_4=np.append(array_4,grpdat.get_group(atom_list_4[0])['real'].values[i])
#for i in range(0,nGeomSteps+1):
#    for j in range(1,len(atom_list_4)):
#        array_4[i]=array_4[i]+grpdat.get_group(atom_list_4[j])['real'].values[i]
#
#font = {'family' : 'normal',
#        'weight' : 'bold',
#        'size' : '22'}
#
#fig, ax = plt.subplots(figsize=(10,10))
##ax.plot(grpdat.get_group(0)['step']*0.3/1000,array,linewidth=4.0)
#
#ax.plot(grpdat.get_group(0)['step']*0.3/1000,array_1,linewidth=4.0,label='1st TFSI')
#ax.plot(grpdat.get_group(0)['step']*0.3/1000,array_2,linewidth=4.0,label='2nd TFSI')
#ax.plot(grpdat.get_group(0)['step']*0.3/1000,array_3,linewidth=4.0,label='3rd TFSI')
#ax.plot(grpdat.get_group(0)['step']*0.3/1000,array_4,linewidth=4.0,label='4th TFSI')
##ax.plot(grpdat.get_group(0)['step'],array_4,linewidth=4.0,label='4th')
##ax.plot(grpdat.get_group(0)['step'],array_4,linewidth=4.0,label='5th')
##ax.plot(grpdat.get_group(0)['step'],array_4,linewidth=4.0,label='6th')
#
#ax.legend(loc='lower left', prop={'size':20})
#ax.set_xlabel("Time step [ps]",fontsize=30)
#ax.set_ylabel("Charge [e]",fontsize=30)
#ax.tick_params(labelsize=20)
#plt.show()
##os.system("mkdir -p _figs")
#
##fig.tight_layout()
##fig.savefig("_figs/force.png")
#
