#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 20:33:28 2021

@author: hantswilliams
"""


import streamlit as st
import pandas as pd
import numpy as np


st.title('CMS - Hospital Data ')

st.text('For this assignment, we were tasked with doing X, Y, Z; For the first part, here are some transofrmation that were applied....")

st.code("""
        inpatient_ny.groupby('drg_definition')['total_discharges'].sum().reset_index()
        """)


df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')


st.dataframe(df)


