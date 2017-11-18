"""Test dash out on OSC data."""
from collections import OrderedDict
import dash
import json
import numpy as np
import urllib.request

event_name = 'SN2002er'

url = "https://api.sne.space/" + event_name + "/spectra/time+data?item=10"
response = urllib.request.urlopen(url)
data = json.loads(response.read(), object_pairs_hook=OrderedDict)

data = data[next(iter(data))]['spectra'][0][1]
data = np.array(list(map(list, zip(*data)))).astype(np.float)

url = "https://api.sne.space/" + event_name + "/redshift/value"
response = urllib.request.urlopen(url)
redshift = json.loads(response.read(), object_pairs_hook=OrderedDict)
redshift = float(redshift[next(iter(redshift))]['redshift'][0][0])

classification = dash.Classify(
    [data], [redshift], classifyHost=False, rlapScores=True)
(bestFits, redshifts, bestTypes, rlapFlag,
    matchesFlag) = classification.list_best_matches(n=5)

print(bestFits)
