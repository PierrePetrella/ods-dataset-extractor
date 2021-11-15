#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Recipe for downloading data from ODS
"""

import dataiku
from dataiku.customrecipe import *
import pandas as pd, numpy as np

from odsdatasetextractor.ods_tools import fetch_ods_dataset


### READ PLUGIN INPUTS ###

# Retrieve input and output dataset names
output_dataset_name = get_output_names_for_role('main_output')[0]

# Retrieve mandatory user-defined parameters
dataset_id = get_recipe_config().get('dataset_id', "dataset_id")

# Fetch data
ods_data_df = fetch_ods_dataset(dataset_id)

# save to output dataset
ods_data = dataiku.Dataset(output_dataset_name)
ods_data.write_with_schema(ods_data_df)