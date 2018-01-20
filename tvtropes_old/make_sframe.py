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

#dictfile = open("dictfile", 'r+')
#readdict = dictfile.read()
#nameTypeDict = ast.literal_eval(readdict)
#dictfile.close()

works = {}
tropes = {}

workIndex = 0
tropeIndex = 0

for page,info in loaded.iteritems():
    if info[0] == "Trope":
        tropes[page] = tropeIndex
        tropeIndex += 1
    if info[0] == "Work":
        works[page] = workIndex
        workIndex += 1

print tropeIndex
print workIndex

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

csv = open("sframe.csv", 'w')
csv.write((u'title`trope`hasTrope\n').encode('utf8'))

count = 0

for page,info in loaded.iteritems():
    if info[0] == "Work":
        title = page
        links = info[1]
        for trope in tropes:
            if trope in links:
                count += 1
                towrite = title+u'`'+trope+u'`'+u"1\n"
                csv.write(towrite.encode('utf8'))

csv.close()

print "lines written: " + str(count)
#matrixfile = open("matrixfile", 'w')
#print "matrix file opened"

#scipy.io.mmwrite(matrixfile, matrix)
#print "matrix written"

#matrixfile.close()
print "done"
