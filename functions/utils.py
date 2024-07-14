#!/usr/bin/env python
# coding: utf-8

"""
Utility functions supporting 'Watershed_Tools' code
@authors: orig hongli liu, 2020; rewritten AW Wood, 2021
"""

import os, sys

# Function to extract a given setting from the configuration file
def read_from_control(control_file, setting):
    
    # Open and read control file
    with open(control_file) as contents:
        for line in contents:
            read_setting = line.split('|',1)[0].strip()
            
            # find the line with the requested setting
            if (read_setting == setting) and (not line.startswith('#')):
                break
    # Extract the setting's value
    substring = line.split('|',1)[1]      # Remove the setting's name (split into 2 based on '|', keep only 2nd part)
    substring = substring.split('#',1)[0] # Remove comments, does nothing if no '#' is found
    substring = substring.strip()         # Remove leading and trailing whitespace, tabs, newlines                
       
    # Return this value    
    return substring

# Specify the default filename (including directory path)
def set_filename(control_file, setting):
    fileName        = read_from_control(control_file, setting)
    basin_data_path = read_from_control(control_file, 'basin_data_path')
    gis_path        = basin_data_path + 'gis'

    if not os.path.isabs(fileName):
        # files in main basin_data directory
        if setting in ['basin_gruId_txt', 'basin_gruNo_gruId_txt' ]:
            fileName = basin_data_path + fileName
        # files in GIS directory
        else:
            # special case for refraster
            if setting == 'refraster' and fileName == 'default':
                fileName = read_from_control(control_file, 'basin_dem_raster')
            # special case for basin_gru_shp
            if setting == 'basin_gru_shp' and fileName == 'default':
                fileName = 'gru.shp'     # create this file rather than read it        
            fileName = os.path.join(gis_path, fileName)                   
        # else:
        #     print('utility set_filename() not successful for file ', setting)
        #     print('STOP')     # warning in jupyter notebook; use exit() in normal script
    else:
        fileName = fileName  
    return fileName
