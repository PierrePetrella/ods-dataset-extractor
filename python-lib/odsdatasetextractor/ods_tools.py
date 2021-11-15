#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Extracts public data from OpenDataSoft given a dataset id
"""

import pandas as pd
import json
import requests

def fetch_ods_dataset(dataset_id):
    source = "https://data.opendatasoft.com/api/v2/opendatasoft/datasets/"
    output_format = "json"
    params = {}

    url_endpoint = source + dataset_id + "/exports/" + output_format

    response = requests.get(url_endpoint, params = params)
    records_json = json.dumps(response.json())
    return pd.read_json(records_json)