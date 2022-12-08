# %% [Markdown]
"""
Let's get data from a SERP-API
"""

# %%

import os
from typing import Any
import serpapi
from serpapi import GoogleSearch
import pandas as pd

# %%

# Run the API over 4 different coordinates
coords: dict[str, str] = {
    "Hisingen": "@57.7206299,11.9373853,13z",
    "Majorna": "@57.692164,11.921590,13z",
    "Linne": "@57.694282,11.956661,13z",
    "Inom Vallgraven": "@57.704607,11.967238,13z",
}

# The params needed for the API request
params: dict[str, Any] = {
    "api_key": os.getenv("SERP_API_KEY"),
    "device": "desktop",
    "engine": "google_maps",
    "type": "search",
    "google_domain": "google.se",
    "q": "Retauranger göteborg",
    "hl": "sv",
    "ll": "@57.7067841,11.9735851,13z",
    "gl": "se",
    "start": 0,
}

# Empty pandas dataframe to append data to.
df: pd.DataFrame = pd.DataFrame()


for area, coord in coords.items():
    print(f"Running {area}")
    params["ll"]: str = coord
    for start_num in range(0, 100, 20):
        print(start_num)
        if start_num == 0:
            params["start"]: int = start_num
            search: serpapi.google_search.GoogleSearch = GoogleSearch(params)
            results: dict = search.get_dict()
            try:
                df: pd.DataFrame = pd.concat(
                    [df, pd.DataFrame(search.get_dict()["local_results"])]
                )
            except Exception:
                pass
        else:
            if "next" in results["serpapi_pagination"]:
                params["start"]: int = start_num
                search: serpapi.google_search.GoogleSearch = GoogleSearch(params)
                results: dict = search.get_dict()
                try:
                    df: pd.DataFrame = pd.concat(
                        [df, pd.DataFrame(search.get_dict()["local_results"])]
                    )
                except Exception:
                    pass
            else:
                break

df.to_csv("data_1.csv")
