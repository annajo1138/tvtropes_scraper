import json
import ast
import scipy.io
from scipy.sparse import dok_matrix

def nameToUrl(string):
    return string.strip()

jsonfile = open("dumpfile")
print "json file"

jsonstr = jsonfile.read()
print "json string"

decoder = json.JSONDecoder()
print "file opened"

loaded = decoder.decode(jsonstr)
print "loaded"

jsonfile.close()

dictfile = open("dictfile", 'r+')
readdict = dictfile.read()
nameTypeDict = ast.literal_eval(readdict)
dictfile.close()

works = {}
tropes = {}

workIndex = 0
tropeIndex = 0

for page,pageType in nameTypeDict.iteritems():
    if pageType == "Trope":
        tropes[page] = tropeIndex
        tropeIndex += 1
    if pageType == "Work":
        works[page] = workIndex
        workIndex += 1

print "got index dictionaries"

workindexfile = open("workindexfile", 'w')
workjson = json.JSONEncoder().encode(works)
workindexfile.write(workjson)
workindexfile.close()

tropeindexfile = open("tropeindexfile", 'w')
tropejson = json.JSONEncoder().encode(tropes)
tropeindexfile.write(tropejson)
tropeindexfile.close()

print "index files written"

matrix = dok_matrix((workIndex+1,tropeIndex+1))
#[[0 for i in range(tropeIndex+1)] for j in range(workIndex+1)]

print "matrix made"

count = 0
for page in loaded:
    workIndex = works[page['title'][0]]
    for trope in page['all_links']:
        tropeIndex = tropes[trope]
        matrix[workIndex,tropeIndex] = 1
        count += 1

print "matrix values set"
print "num values: " + str(count)

matrixfile = open("matrixfile", 'w')
print "matrix file opened"

scipy.io.mmwrite(matrixfile, matrix)
print "matrix written"

matrixfile.close()
print "done"
