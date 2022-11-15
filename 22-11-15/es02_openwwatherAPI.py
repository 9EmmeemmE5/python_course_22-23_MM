"""OpenweatherAPI"""
# per abilitare la virtual environment occorre digitare sul terminale "virtualenv venv" per creare 
# il virtual env, mentre per attivarlo occorre digitare "venv\Scripts\activate", usato per non 
# intaccare l'ambiente locale, NB occorre prima installarlo con pip

import json
import os
import requests
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
