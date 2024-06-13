import json
from pydataformat.loadData import LoadData
from pyciderevalcap.eval import CIDErEvalCap as ciderEval


config = json.loads(open('params.json', 'r').read())

pathToData = config['pathToData']
refName = config['refName']
candName = config['candName']
resultFile = config['resultFile']
df_mode = config['idf']

loadDat = LoadData(pathToData)
gts, res = loadDat.readJson(refName, candName)

scorer = ciderEval(gts, res, df_mode)
scores = scorer.evaluate()

with open(resultFile, 'w') as outfile:
    json.dump(scores, outfile)
