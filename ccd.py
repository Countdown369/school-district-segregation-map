#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:54:50 2024

@author: cabrown802
"""

import pandas as pd
import math
from pandasql import sqldf
import numpy as np
from scipy.stats import entropy

"PART ONE: MAKE A PIVOT TABLE OF DISTIRCT RACE POPULATIONS"
ccd = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/ccd_sch_052_2223_l_1a_083023.csv")
# import pdb; pdb.set_trace()
# run_query = lambda query: sqldf(query, globals())

# query_1 = """
# SELECT DISTINCT ST, ST_LEAID, SCH_NAME, SCHID, RACE_ETHNICITY, SUM(STUDENT_COUNT) AS STUCO
# FROM ccd
# GROUP BY ST_LEAID, SCHID, RACE_ETHNICITY;
# """
# df = run_query(query_1)


# xd = pd.pivot_table(df, values='STUCO', index=['ST_LEAID', 'SCHID'], columns=['RACE_ETHNICITY'], aggfunc="sum")

"PART TWO: CALCULATE ATKINSON FOR DISTRICT-IN-DISTRICT"
# df = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/honeycomb.csv")
# # Remove schools with Sum = 0 students
# df = df[df['Sum'] != 0]

# racelist = ['American Indian or Alaska Native','Asian','Black or African American','Hispanic/Latino','Native Hawaiian or Other Pacific Islander', 'Two or more races','White']
# df_atkinsons = {}

# for district in df.ST_LEAID.unique():
#     current_district = df[df['ST_LEAID'] == district]
#     old_district_sums = {}
#     for race in racelist:
#         old_district_sums[race] = sum(current_district[race])
#     district_sums = {k: v for k, v in old_district_sums.items() if v != 0}
#     distpop = sum(district_sums.values())
#     district_exponents = {k: v/distpop for k, v in district_sums.items()}
    
#     newcols = {}
#     for i, r in current_district.iterrows():
#         iternewcols = {}
#         for key in district_sums.keys():
#             iternewcols[key] = r[key] / district_sums[key]
#         newcols[r['SCHID']] = iternewcols


#     if len(newcols.keys()) == 1:
#         continue

#     atkinsons = {}
#     for k, v in newcols.items():
#         terms = []
#         for subk, subv in v.items():
#             terms.append(subv**district_exponents[subk])
        
#         atkinsons[k] = math.prod(terms)
        
#     # Come back here to add Adjusted Atkinson index, adding races that aren't
#     # present at EACH AND EVERY school to the least-greatest race that is
#     # present at each and every school.

#     # Why ZERO?
#     # In spreadsheets, an Atkinson Index of 0 always means
#     # the district has only ONE ethnic group.
#     # An Atkinson of 1 indicates that:
#     # "each school in a district lacks students from
#     # at least one ethnic group that
#     # is present at at least one school in the district.

#     atkinson_index = 1 - sum(atkinsons.values())
#     df_atkinsons[district] = atkinson_index

# pd.DataFrame.from_dict(data=df_atkinsons, orient='index').to_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/DIST_ATKINS_FIX3.csv', header=False)

"PART THREE: MERGE ATKINSON DATA WITH DISTRICT IDENTIFIERS"
# df = pd.read_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/DIST_ATKINS_FIX1.csv', header = None, names=['ST_LEAID', 'Atkinson'])
# mykey = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/GEOID_KEY.csv")
# df['ST_LEAID']=df['ST_LEAID'].astype(str)
# mykey['ST_LEAID']=mykey['ST_LEAID'].astype(str)
# import pdb; pdb.set_trace()

# I did this all in pdb appearently and can't be bothered to re-write it
# properly now that I have the relevant file. Sorry!

"PART FOUR: CALCULATE ATKINSON FOR DISTRICT-IN-STATE"
# df = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/honeycomb.csv")
# # # Remove schools with Sum = 0 students
# df = df[df['Sum'] != 0]

# racelist = ['American Indian or Alaska Native','Asian','Black or African American','Hispanic/Latino','Native Hawaiian or Other Pacific Islander','Two or more races','White']
# df_atkinsons = {}

# for state in df.ST.unique():
#     current_state = df[df['ST'] == state]
#     old_state_sums = {}
#     for race in racelist:
#         old_state_sums[race] = sum(current_state[race])
#     state_sums = {k: v for k, v in old_state_sums.items() if v != 0}
#     statepop = sum(state_sums.values())
#     state_exponents = {k: v/statepop for k, v in state_sums.items()}
    
#     for district in current_state.ST_LEAID.unique():
#         newcols = {}
#         current_district = current_state[current_state['ST_LEAID'] == district]
#         old_district_sums = {}
#         for race in racelist:
#             old_district_sums[race] = sum(current_district[race])
#         district_sums = {k: v for k, v in old_district_sums.items() if v != 0}
#         for i, r in current_district.iterrows():
#             iternewcols = {}
#             for key in district_sums.keys():
#                 iternewcols[key] = r[key] / district_sums[key]
#             newcols[r['SCHID']] = iternewcols
        
#         if len(newcols.keys()) == 1:
#             continue
        
#         atkinsons = {}
#         for k, v in newcols.items():
#             terms = []
#             for subk, subv in v.items():
#                 terms.append(subv**state_exponents[subk])
#             # if district == 'AK-15':
#             #     import pdb; pdb.set_trace()
#             atkinsons[k] = math.prod(terms)

            
            
#         # bad idea below:        
#         # Come back here to add Adjusted Atkinson index, adding races that aren't
#         # present at EACH AND EVERY school to the least-greatest race that is
#         # present at each and every school.
#         atkinson_index = 1 - sum(atkinsons.values())
#         df_atkinsons[district] = atkinson_index

# pd.DataFrame.from_dict(data=df_atkinsons, orient='index').to_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/STATE_ATKINS.csv', header=False)

"PART FIVE: CALCULATE MUTUAL INFORMATION FOR DISTRICT"
# df = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/honeycomb.csv")
# # # Remove schools with Sum = 0 students
# df = df[df['Sum'] != 0]

# racelist = ['American Indian or Alaska Native','Asian','Black or African American','Hispanic/Latino','Native Hawaiian or Other Pacific Islander', 'Two or more races','White']
# df_mutual = {}

# for district in df.ST_LEAID.unique():
#     current_district = df[df['ST_LEAID'] == district]
#     if len(current_district) == 1:
#         continue
#     old_district_sums = {}
#     for race in racelist:
#         old_district_sums[race] = sum(current_district[race])
#     district_sums = {k: v for k, v in old_district_sums.items() if v != 0}
    
#     district_distribution = []
#     distpop = sum(district_sums.values())
#     if distpop == 0:
#         continue
    
#     for k, v in district_sums.items():
#         district_distribution.append(v/distpop)

#     district_entropy = entropy(district_distribution, base=2)
    
#     addends = []
    
#     for i, r in current_district.iterrows():
#         school_entropy = entropy([r['PercAA'], r['PercA'], r['PercB'], r['PercH'], r['PercNH'], r['PercM'], r['PercW']], base=2)
#         mcand = district_entropy - school_entropy
#         mer = r['Sum']/distpop
#         addends.append(mer*mcand)
    
#     df_mutual[district] = sum(addends)

# pd.DataFrame.from_dict(data=df_mutual, orient='index').to_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/DIST_MUTUAL.csv', header=False)

"PART SIX: CALCULATE ATKINSON FOR DISTRICT-IN-USA"
# df = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/honeycomb.csv")
# # # Remove schools with Sum = 0 students
# df = df[df['Sum'] != 0]

# racelist = ['American Indian or Alaska Native','Asian','Black or African American','Hispanic/Latino','Native Hawaiian or Other Pacific Islander','Two or more races','White']
# df_atkinsons = {}

# old_state_sums = {}
# for race in racelist:
#     old_state_sums[race] = sum(df[race])
# state_sums = {k: v for k, v in old_state_sums.items() if v != 0}
# statepop = sum(state_sums.values())
# state_exponents = {k: v/statepop for k, v in state_sums.items()}

# for district in df.ST_LEAID.unique():
#     newcols = {}
#     current_district = df[df['ST_LEAID'] == district]
#     old_district_sums = {}
#     for race in racelist:
#         old_district_sums[race] = sum(current_district[race])
#     district_sums = {k: v for k, v in old_district_sums.items() if v != 0}
#     for i, r in current_district.iterrows():
#         iternewcols = {}
#         for key in district_sums.keys():
#             iternewcols[key] = r[key] / district_sums[key]
#         newcols[r['SCHID']] = iternewcols
    
#     if len(newcols.keys()) == 1:
#         continue
    
#     atkinsons = {}
#     for k, v in newcols.items():
#         terms = []
#         for subk, subv in v.items():
#             terms.append(subv**state_exponents[subk])
#         atkinsons[k] = math.prod(terms)
    
#     atkinson_index = 1 - sum(atkinsons.values())
#     df_atkinsons[district] = atkinson_index

# pd.DataFrame.from_dict(data=df_atkinsons, orient='index').to_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/USA_ATKINS.csv', header=False)

"PART SEVEN: MERGE ALL INDEX DATA WITH DISTRICT IDENTIFIERS"
# df1  = pd.read_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/_Usable Index Data/DIST_ATKINS_FIX3.csv', header = None, names=['ST_LEAID', 'DistDistAtkinson'])
# df2  = pd.read_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/_Usable Index Data/STATE_ATKINS.csv', header = None, names=['ST_LEAID', 'DistStateAtkinson'])
# df4  = pd.read_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/_Usable Index Data/USA_ATKINS.csv', header = None, names=['ST_LEAID', 'DistNationAtkinson'])
# df3  = pd.read_csv('/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/_Usable Index Data/DIST_MUTUAL.csv', header = None, names=['ST_LEAID', 'DistMutual'])
# mykey = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/GEOID_KEY.csv")
# df1['ST_LEAID']=df1['ST_LEAID'].astype(str)
# df2['ST_LEAID']=df2['ST_LEAID'].astype(str)
# df4['ST_LEAID']=df4['ST_LEAID'].astype(str)
# df3['ST_LEAID']=df3['ST_LEAID'].astype(str)
# mykey['ST_LEAID']=mykey['ST_LEAID'].astype(str)

# merged_df = (
#     mykey
#     .drop_duplicates(subset=['ST_LEAID'])  # Ensure one observation per ST_LEAID
#     .merge(df1[['ST_LEAID', 'DistDistAtkinson']], on='ST_LEAID', how='left')
#     .merge(df2[['ST_LEAID', 'DistStateAtkinson']], on='ST_LEAID', how='left')
#     .merge(df4[['ST_LEAID', 'DistNationAtkinson']], on='ST_LEAID', how='left')
#     .merge(df3[['ST_LEAID', 'DistMutual']], on='ST_LEAID', how='left')
# )
# import pdb; pdb.set_trace()

"PART EIGHT: MERGE THIS TO HONEYCOMB"
# honeycomb = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/honeycomb.csv")
# oxford_comma = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/oxford_comma.csv")

# honeycomb['ST_LEAID']=honeycomb['ST_LEAID'].astype(pd.StringDtype())
# oxford_comma['ST_LEAID']=oxford_comma['ST_LEAID'].astype(pd.StringDtype())
# #import pdb; pdb.set_trace()


# combined_df = pd.merge(
#     honeycomb,
#     oxford_comma[['ST_LEAID', 'LEAID', 'DistDistAtkinson', 'DistStateAtkinson', 'DistNationAtkinson', 'DistMutual']],
#     on='ST_LEAID',  # Column in `honeycomb`
#     how='left'           # Preserve all rows from `honeycomb`
# )

# combined_df.to_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/brat.csv")

# And that's where we're at, 1 PM, Nov 26, 2024.

"PART NINE: REMOVE SCHOOL DISTRICT GEOMETRY OVERLAPS FROM MERGED DATASET"
import geopandas as gpd
import matplotlib.pyplot as plt

# df = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/oxford_comma.csv")
# geo = gpd.read_file("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/EDGE_SCHOOLDISTRICT_TL23_SY2233/EDGE_SCHOOLDISTRICT_TL_23_SY2223.shp")

# # Ensure both 'LEAID' and 'GEOID' are of the same type (e.g., string)
# df['LEAID'] = df['LEAID'].astype(pd.StringDtype())
# geo['GEOID'] = geo['GEOID'].astype(pd.StringDtype())
# df['LEAID'] = df['LEAID'].astype(pd.Int32Dtype())
# geo['GEOID'] = geo['GEOID'].astype(pd.Int32Dtype())
# #import pdb; pdb.set_trace()
# print('Wow!')

# # Perform the merge
# geo2 = geo.merge(df, how='left', left_on='GEOID', right_on='LEAID')

# # # Drop the redundant 'LEAID' column if no longer needed
# geo2 = geo2.drop(columns=['LEAID', 'ST_SCHID','NCESSCH', 'SCHID', 'GRADE', 'RACE_ETHNICITY', 'SEX', 'STUDENT_COUNT', 'TOTAL_INDICATOR', 'DMS_FLAG', 'Unnamed: 0.1', 'Unnamed: 0', 'SCHOOL_YEAR', 'FIPST', 'STATENAME', 'ST', 'SCH_NAME', 'STATE_AGENCY_NO', 'UNION', 'STATEFP', 'ELSDLEA', 'SCSDLEA', 'UNSDLEA', 'SDADMLEA', 'MTFCC', 'FUNCSTAT', 'GEO_YEAR', 'SCHOOLYEAR'])

# geo2.to_file("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/geojson_data_for_upload.geojson", driver="GeoJSON")

# fig, ax = plt.subplots(1, 1)
# geo2.plot(column='DistMutual', cmap='OrRd', legend=True, ax=ax)
# plt.title('deseg_one')
# plt.show()
# # import pdb; pdb.set_trace()

# # Create an empty GeoDataFrame to store overlapping geometries
# overlaps = gpd.GeoDataFrame(columns=geo.columns, geometry='geometry', crs=geo.crs)

# # Use a spatial join to find intersecting polygons
# for i, polygon in geo.iterrows():
#     # Find polygons that intersect with the current polygon (excluding itself)
#     intersecting_polygons = geo[geo.geometry.intersects(polygon.geometry) & (geo.index != i)]
    
#     # If any intersecting polygons were found, concatenate them to the overlaps GeoDataFrame
#     if not intersecting_polygons.empty:
#         intersecting_polygons.insert(6, "IntersectGEOID", [polygon.GEOID] * len(intersecting_polygons), True)
#         overlaps = pd.concat([overlaps, intersecting_polygons])

# # Remove duplicate overlaps
# overlaps = overlaps.drop_duplicates()
# overlaps_lite = overlaps.drop(columns=['geometry'])
# overlaps_lite.to_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/intersects.csv")

"PART TEN: JOIN GEOID COUNT DATA TO GEOID INTERSECT DATA"

# copy = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/intersects_working_copy_prefix.csv")
# counts = pd.read_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/geoid_intersect_counts.csv")

# df = copy.merge(counts, how='left', on='GEOID')
# df.to_csv("/Users/cabrown802/Downloads/ccd_sch_052_2223_l_1a_083023/intersects_working_copy_postfix.csv")
