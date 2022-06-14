# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------------
# find_Drive.py
# Created on: 2014-09-08
# Description: Unzips or zips a directory
# ---------------------------------------------------------------------------

# This script is zips/unzips a directory.

# Currently set up to unzip (unzipDir(inputDir).
# Comment out unzipDir(inputDir) and uncomment zipDir(inputDir) to zip a
# directory.

import os
import zipfile

try:
    import zlib
    mode= zipfile.ZIP_DEFLATED
except:
    mode= zipfile.ZIP_STORED

def unzipDir(inputDir):
    for root, dirs, files in os.walk(inputDir):
        for f in files:
            if f.endswith('.zip'):
                inFile = os.path.join(root, f)
                print 'Working on', inFile
                outDir = os.path.join(root, f[:-4])
                if not os.path.isdir(outDir):
                    os.mkdir(outDir)
                    print 'Created',outDir
                else:
                    continue

                with zipfile.ZipFile(inFile,'r') as z:
                    z.extractall(outDir)
                print f,'was successful.'

    print ('Done.')
 
#inputDir = r'C:\Users\kerni016\Documents\DRUM\200508\LargeShapefileTest\ALL_REGIONS_SHP_tr_2017_0700-0859'
inputDir = r'C:\MetadataWranglers\umn-thesis-metadata\test-batch'
for root, dirs, files in os.walk(inputDir):
    for f in files:
        if f.endswith('.zip'):
            #try:
                inFile = os.path.join(root, f)
                #print 'Working on', inFile
                outDir = os.path.join(root, f[:-4])
                if not os.path.isdir(outDir):
                    os.mkdir(outDir)
                    #print 'Created',outDir
                else:
                    continue
    
                with zipfile.ZipFile(inFile,'r') as z:
                    z.extractall(outDir)
                #print f,'was successful.'
            #except:
                #print f, 'ERROR!'
print 'Done.'

#def zipDir(inputDir):
#    zipFileName = os.path.join(inputDir,'zipfile.zip')
#    print zipFileName
#    zip= zipfile.ZipFile(zipFileName, 'w', mode)
#    for root, dirs, files in os.walk(inputDir):
#        for f in files:
#            if f.endswith('.xml'):
#                fileName = os.path.join(root,f)
#                zip.write(fileName, arcname=f)
#    print 'ZIP CREATED'
#    zip.close()
#    print 'Done.'
#
#
#inputDir = r'C:\Users\kerni016\Documents\C:\Users\kerni016\Documents\DRUM\200508'
#
#unzipDir(inputDir)
#zipDir(inputDir)




