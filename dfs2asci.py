#!/usr/bin/env python

import os
import sys
import shutil
import gdal
import numpy as np

import clr
sys.path.append('C:/Program Files (x86)/DHI/2017/MIKE SDK/bin')  # adding to path of environment variables doesn't work
clr.AddReference("DHI.Generic.MikeZero.DFS")
clr.AddReference("DHI.Generic.MikeZero.EUM")
clr.AddReference("System")

import System
from System import Array

from DHI.Generic.MikeZero.DFS import *
from DHI.Generic.MikeZero.DFS.dfs123 import *


def write_dfs2_timestep(numparray, index, outfile):
    # writes numpy array into an existing dfs2 file with the same dimensions
    out = Array[System.Single](numparray.tolist())
    dfs2File = Dfs2FileOpenEdit(outfile)
    dem = dfs2File.WriteItemTimeStep(index, 0, 0.0, out)
    dfs2File.Close()

def write_dfs2_timestep(numparray,index,outfile):
    #writes numpy array into an existing dfs2 file with the same dimensions
    out=Array[System.Single](numparray.tolist())
    dfs2File = Dfs2FileOpenEdit(outfile)
    dem = dfs2File.WriteItemTimeStep(index,0,0.0,out)
    dfs2File.Close()

def tif2dfs2(file_tif, file_dfs2):
    ds = gdal.Open(file_tif, gdal.GA_ReadOnly)
    arr = np.array(ds.GetRasterBand(1).ReadAsArray())  # only one band - DEM
    arr = np.fliplr(np.transpose(arr))
    print ds.GetGeoTransform()
    print ds.GetProjection()

    dfs2 = Dfs2Builder()
    print dir(IDfsProjection)
    print dir(dfs2.Projection)
    print dir(dfs2)
    #proj = IDfsProjection
    #proj = IDfsProjection(ds.GetProjection())
    #print proj
    print dfs2.GetType()


def tif2dfs(file_tif, file_dfs):
    if fh.GetType() == 'DHI.Generic.MikeZero.DFS.dfs123.Dfs0Builder':
        pass
    elif fh.GetType() == 'DHI.Generic.MikeZero.DFS.dfs123.Dfs1Builder':
        pass
    elif fh.GetType() == 'DHI.Generic.MikeZero.DFS.dfs123.Dfs2Builder':
        return tif2dfs2()
    elif fh.GetType() == 'DHI.Generic.MikeZero.DFS.dfs123.Dfs3Builder':
        pass
    elif fh.GetType() == 'DHI.Generic.MikeZero.DFS.dfs123.DfsuBuilder':
        pass
    else:
        raise ValueError('Dfs type')

def read_dfs2(infile):

    pass

def read_dfsu(infile):
    print dir(DfsFileFactory)
    fh = DfsFileFactory.DfsuFileOpenEdit(infile)
    print fh, dir(fh)
    print dir(fh.Projection)
    print fh.ToString()
    print fh.Projection, dir(fh.Projection)
    print fh.Projection.Latitude
    print fh.Projection.Longitude,fh.Projection.WKTString
    fact = DfsFactory()
    proj = fact.CreateProjection(fh.Projection.WKTString)

    print dir(proj)
    print proj
    fh.Close()

if __name__=='__main__':
    # easist to use another file as template
    read_dfs2('./tests/test.dfsu')
    tif2dfs2('./tests/test.tif', './tests/test.dfs2')
    #read_dfsu('./tests/test.dfsu')

    ds = gdal.Open('./tests/test.tif', gdal.GA_ReadOnly)
    arr = np.array(ds.GetRasterBand(1).ReadAsArray())  # only one band - DEM
    arr = np.fliplr(np.transpose(arr))
    #print arr.tolist()
    print dir(Array)
    #write_dfs2_timestep(arr, 1, './test/test.dfs2')
