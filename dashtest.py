import dash
import numpy as np

wave = np.arange(2500, 10000, 2)
flux = np.ones(len(wave))
filename = np.array([wave, flux])

classification = dash.Classify([filename], [0.], classifyHost=False, rlapScores=True)
bestFits, redshifts, bestTypes, rlapFlag, matchesFlag = classification.list_best_matches(n=5)

print(bestFits)
