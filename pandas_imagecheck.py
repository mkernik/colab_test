# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:23:34 2020

@author: kerni016
"""

import csv
import pandas as pd 
import numpy as np


####Add in source spreadsheet
source = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_flagged.csv"
good_to_go_csv = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_goodtogo.csv"


df = pd.read_csv(source) 

for col in df.columns: 
    print(col) 

###Create a list of unique Township Ranges
df.sort_values(by='Township_Range', inplace=True)

# set the index to be this and don't drop
df.set_index(keys=['Township_Range'], drop=False,inplace=True)

# get a list of names
TR_list = df['Township_Range'].unique().tolist()


### identifies township range filenames where there is only 1 image; it is full, independent with no description flags -- in other words good to go 

good_to_go = []

fi_1image = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        if (len(TR_item) == 1) & (TR_item["Image_Type"][0] == "i") & (TR_item["Image_Number"][0] == 1.0) & (pd.isnull(TR_item["Remove"][0]) == True):
            fi_1image.append(TR_item["filename"][0])
            good_to_go.append(TR_item["filename"][0])
except:
    print (TR)

len(fi_1image)

### Prints this list to a spreadsheet
with open(good_to_go_csv, 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(good_to_go)





####Checking through multi-image and flagged records



####Add in source spreadsheet
source = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_flagged_check.csv"
checked_csv = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_checked.csv"


df = pd.read_csv(source) 

for col in df.columns: 
    print(col) 

###Create a list of unique Township Ranges
df.sort_values(by='Township_Range', inplace=True)

# set the index to be this and don't drop
df.set_index(keys=['Township_Range'], drop=False,inplace=True)

# get a list of names of unique Township Ranges (612) 
TR_list = df['Township_Range'].unique().tolist()

########Other attempts to examine the spreadsheet and identify good or duplicate images

###3   (in the PLSS google doc for manual review)
oneimage_notfi = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        if (len(TR_item) == 1) & (TR_item["Image_Type"][0] != "i"):
            oneimage_notfi.append(TR_item["filename"][0])
except:
    print (TR)

len(oneimage_notfi)

### 11 (in the PLSS google doc for manual review)
fi_1image_check = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        if (len(TR_item) == 1) & (TR_item["Image_Type"][0] == "i") & (TR_item["Image_Number"][0] == 1.0) & (pd.isnull(TR_item["Remove"][0]) == False):
            fi_1image_check.append(TR_item["filename"][0])

except:
    print (TR)

len(fi_1image_check)


##############  takeaways 6 unsigned are the only image for the area
mi_unsigned = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        #if len(TR_item) > 1:
        for x in range(len(TR_item)):
            if TR_item["why_removed"][x] == "unsigned":
                for x in range(len(TR_item)):
                    mi_unsigned.append(TR_item["filename"][x])
except:
    print (TR)

len(mi_unsigned)

with open(checked_csv, 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(mi_unsigned)


#######

mi_1fi = {}
multi_images= {}

for TR in TR_list:
    TR_item = df.loc[df.Township_Range==TR]
    if len(TR_item) > 1:
        item_types = []
        for x in range(len(TR_item)):
            item_types.append(TR_item["Image_Type"][x])
        multi_images[TR_item["Township_Range"][0]] = item_types
      

image2_i = []
image2_iplus = []
image2_noni = {}
image2plus = {}      
      
for k, v in multi_images.items():
    if len(v) == 2:
        if ('i' in v) and (v[0] == v[1]):
            image2_i.append(k)
        elif ('i' in v) and (v[0] != v[1]):
            image2_iplus.append(k)
        else:
            image2_noni[k] = v
    else:
        image2plus[k] = v



############ WHY DOESN'T IT REMOVE FLAGGED ROWS?
check_TRs = []
noflags_TRs = []

for TR in image2_iplus:
    TR_item = df.loc[df.Township_Range==TR]
    for x in range(len(TR_item)):
        flags = []
        if TR_item["Flag"][x] != "n":            
            flags.append(x)
    if len(flags) > 0:
        check_TRs.append(TR)
    else:
        noflags_TRs.append(TR)
            

checked3_csv = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_checked3.csv"
with open(checked3_csv, 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(check_TRs)
                

###

check_ii_TRs = []
noflags_ii_TRs = []

for TR in image2_i:
    TR_item = df.loc[df.Township_Range==TR]
    for x in range(len(TR_item)):
        flags = []
        if TR_item["Flag"][x] != "n":            
            flags.append(TR_item["Township_Range"])
    if len(flags) > 0:
        check_ii_TRs.append(TR)
    else:
        noflags_ii_TRs.append(TR)


checked3_csv = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_checked3.csv"
with open(checked3_csv, 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(noflags_ii_TRs)





checked2_csv = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_checked2.csv"
with open(checked2_csv, 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(image2_iplus)




if ('i' in test) & (test[0] = test[1]):
            
if (test[0] == test[1]) & (test[0]=='i'):
    print ("matching i's")
            
                
                if (TR_item["Image_Type"][x] == "i") & (pd.isnull(TR_item["Remove"][x]) == True):
                    ind = str(x)
                    #print (ind)
                    for y in range(len(TR_item)):
                        if (str(y) != ind) & (TR_item["Image_Type"][y] != "i") & (pd.isnull(TR_item["Remove"][y]) == True):  
                            mi_1fi.append(TR_item["Township_Range"][y]) if (TR_item["Township_Range"][y]) not in mi_1fi else mi_1fi
                        else:
                            mi_multifi.append(TR_item["Township_Range"][y]) if (TR_item["Township_Range"][y]) not in mi_multifi else mi_multifi
                        
except:
    print (TR)

print (len(mi_1fi))
print (len(mi_multifi))

checked2_csv = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_checked2.csv"
with open(checked2_csv, 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(mi_1fi)

checked3_csv = "C:/MapLibraryProjects/PLSS/05a-03_Minnesota_Plats_checked3.csv"
with open(checked3_csv, 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(mi_multifi)



##56
multiimage_fiN1 = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        if (len(TR_item) > 1) & (TR_item["Image_Type"][0] == "i") & (TR_item["Image_Number"][0] > 1.0) & (pd.isnull(TR_item["Remove"][0]) == True):
            multiimage_fiN1.append(TR_item["Township_Range"][0])
except:
    print (TR)

len(multiimage_fiN1)

unique_fi = [x for x in multiimage_fi1 if x not in multiimage_fiN1 ]


##########




###314
multiimage_fi1 = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        if (len(TR_item) > 1) & (TR_item["Image_Type"][0] == "i") & (TR_item["Image_Number"][0] == 1.0) & (pd.isnull(TR_item["Remove"][0]) == True):
            multiimage_fi1.append(TR_item["Township_Range"][0])
except:
    print (TR)

len(multiimage_fi1)

##56
multiimage_fiN1 = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        if (len(TR_item) > 1) & (TR_item["Image_Type"][0] == "i") & (TR_item["Image_Number"][0] > 1.0) & (pd.isnull(TR_item["Remove"][0]) == True):
            multiimage_fiN1.append(TR_item["Township_Range"][0])
except:
    print (TR)

len(multiimage_fiN1)

unique_fi = [x for x in multiimage_fi1 if x not in multiimage_fiN1 ]


##########

### 322
multiimage_fi1 = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        if (len(TR_item) > 1) & (TR_item["Image_Type"][0] == "i") & (TR_item["Image_Number"][0] == 1.0):
            multiimage_fi1.append(TR_item["Township_Range"][0])
except:
    print (TR)

len(multiimage_fi1)

## 67
multiimage_fiN1 = []
try:
    for TR in TR_list:
        TR_item = df.loc[df.Township_Range==TR]
        if (len(TR_item) > 1) & (TR_item["Image_Type"][0] == "i") & (TR_item["Image_Number"][0] > 1.0):
            multiimage_fiN1.append(TR_item["Township_Range"][0])
except:
    print (TR)

len(multiimage_fiN1)

non1_fi = [x for x in multiimage_fiN1 if x not in multiimage_fi1 ]



###### Testing things


# count = []
# TR = TR_list[9]
# TR_item = df.loc[df.Township_Range==TR]
# if (len(TR_item) == 1) & (TR_item["Image_Number"][0] == 1.0) & (pd.isnull(TR_item["Remove"][0]) == True):
#     count.append(TR_item["Township_Range"][0])
    
# if TR_item["Image_Number"][0] == 1.0:
#     print ("good")

# if pd.isnull(TR_item["Remove"][0]) == True:
#     print ("good to go")
        
    



df['good'] = np.where(((df['Image_Type']== 'i')), True, False)
df.good.value_counts()


df['flag'] = np.where(df['Image_Type']== 'm', True, False)

df.flag.value_counts()


print(df.loc[df['Description'] != ''])

###terms to look for: duplicate, unsigned, "Same as map ID1214, but missing meanders", not signed, 
mask = df[['Description']].apply(
    lambda x: x.str.contains(
        'duplicate|unsigned',
        regex=True
    )
).any(axis=1)
print(df[mask]['Description'])



variables = ["Order", "Remove",	"why_removed", "Title",	"Alternative Title", "Township Range", "Bounding Box", "Information", "counties", "Description", "Date Issued",	"Creator", "survey", "type", "Is Version Of", "Area", "Image_Type",	"Image_Number",	"Download",	"Image", "Documentation"]

