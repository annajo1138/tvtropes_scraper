import json
import ast

def nameToUrl(string):
    return string.strip()

jsonfile = open("fixed_tropes_real.json")

print "json file"

jsonstr = jsonfile.read()

print "json string"

decoder = json.JSONDecoder()


print "file opened"

#dictionary = dict(jsonfile)
loaded = decoder.decode(jsonstr)

print "loaded"

print type(loaded)

print loaded[0]['title']

jsonfile.close()
nameTypeDict = {}

length = range(0,len(loaded))

for i in length:
    for title in loaded[i]['title']:
        if len(title) < 1:
            #get rid of broken names
            loaded[i]['title'].remove(title)

for i in reversed(length):
    if len(loaded[i]['title']) < 1:
        #sometimes it fails to grab the name
        del loaded[i]

print "broken names gone" 

dictfile = open("dictfile",'r+')
read = dictfile.read()
if len(read) < 1:
    #make a dictionary of pages with their types to make lookup fast(er)
    for i in range(0, len(loaded)):
        nameTypeDict[nameToUrl(loaded[i]['title'][0])] = loaded[i]['pageType']
    dictfile.write(str(nameTypeDict))
    print "dictfile made"
else:
    nameTypeDict = ast.literal_eval(read)
    print "dictfile read from memeory"
dictfile.close()

dumpfile = open("dumpfile", 'w')
for i in range(0,len(loaded)):
    indexes = range(0,len(loaded[i]['all_links']))
    for j in reversed(indexes):
        page = loaded[i]['all_links'][j]
        loaded[i]['all_links'][j] = page.split('/')[-1]
        page = loaded[i]['all_links'][j]

        try:
            lookup = nameTypeDict[page]
        except KeyError:
            loaded[i]['all_links'].remove(page)
        else:
            if lookup != "Trope":
                loaded[i]['all_links'].remove(page) 

for i in range(0,len(loaded)):
    dumpfile.write("%s\n" % loaded[i]['title'])
    dumpfile.write("%s\n" % loaded[i]['all_links'])

works = []

print "dumpfile written"

dumpfile.close()

print "done"

    
