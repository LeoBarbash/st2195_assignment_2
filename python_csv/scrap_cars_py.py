import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path

arr = np.array(BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Comma-separated_values").content,
                             'html.parser').find(class_="wikitable").get_text().split("\n")[:-1]).reshape((5, 7))[:, 2:]
pd.DataFrame(arr[1:], columns=arr[0]).to_csv(Path('/Users/levbarbash/LondonProg/Assignment2/python_csv/cars_py.csv'),
                                             index=False)
