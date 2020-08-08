#!/usr/bin/env python

import numpy as np
import pylab as plt
import glob as glob
import os
import pandas as pd

df1=pd.read_csv("geom_combined.xyz", header=None, delimiter=r"\s+",
                names=["atom","atom_nr","step","z","charge","vel_x","vel_y","vel_z"])


nAtoms = int(df1.iloc[0,0])
#nGeomSteps = int(df1.iloc[-nAtoms-1,2]) # step number is written in 3rd column of geom.out.xyz
nGeomSteps = 15613

print(nGeomSteps)
print(nAtoms)

df1=df1.drop(['z','vel_x','vel_y','vel_z'],axis=1)

df1=df1.dropna()
df1=df1.reset_index(drop=True)

df1['step']=df1.index // nAtoms
df1['atom_nr']=df1.index % nAtoms

values_dict = {'C':4,'N':5,'H':1,'S':6,'O':6,'P':5,'Mg':2,'F':7}
df1['real'] = df1['atom'].map(values_dict)-df1['charge']

grpdat=df1.groupby('atom_nr')
for i in range(0,nAtoms):
    a = grpdat.get_group(i)['real'].reset_index()['real']
    print(a)
    a.to_csv("charges_of_everything/%d.txt" % i, sep="\t", header=False) 

