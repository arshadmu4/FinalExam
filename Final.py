#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Umar Arshad
## December 9, 2022
## Final Exam
"""

#%%
import pandas as pd

## reading datasets
prices = pd.read_csv("https://tjfisher19.github.io/data/gasoline_prices.csv")
codes = pd.read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
regions = pd.read_csv("https://tjfisher19.github.io/data/censusRegions.csv")

## merging data together
finaldata = pd.merge(codes, prices, left_on="State", right_on="State")
finaldata = pd.merge(finaldata, regions, left_on="Code", right_on="State")
## removing DC then grouping by region
finaldata = finaldata[finaldata.State_x != "District of Columbia"]
finaldata["pricediff"] = ((finaldata["Diesel"] - finaldata["Regular"])/
                          finaldata["Regular"])*100
 #creating summary statistics for each region
finaldata = finaldata.groupby("Region")["pricediff"].agg(["mean","std"])
finaldata = finaldata.assign(cv = finaldata["std"]/finaldata["mean"])

print(finaldata)
