import json
import ast

def nameToUrl(string):
    return string.strip()

jsonfile = open("actual_min_mem_tropes_real_copy.json")
print "json file"

jsonstr = jsonfile.read()
print "json string"

decoder = json.JSONDecoder()
print "file opened"

loaded = decoder.decode(jsonstr)
print "loaded"

jsonfile.close()

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

length = range(0,len(loaded))

fixed_dict = {} 
#essentially doing reduceByKey on the dictionary

for i in length:
    title = loaded[i]['title'][0].replace(" ", "")
    try: 
        if fixed_dict[title][0] == "Trope" and loaded[i]['pageType'] == "Work": 
            fixed_dict[title][0] = "Work"
        fixed_dict[title][1].extend(loaded[i]['all_links'])
    except KeyError:
        fixed_dict[title] = [loaded[i]['pageType'], loaded[i]['all_links']]

print "did reduce by title on dictionary"

#works_dict = {}
#tropes_dict = {}
#creators_dict = {}

#for page,info in fixed_dict.iteritems():
#    if info[0] == "Work":
#        works_dict[page] = info
#    elif info[0] == "Trope":
#        tropes_dict[page] = info
#    elif info[0] == "Creator":
#        creators_dict[page] = info

#workfile = open("works", 'w')
#worksjson = json.JSONEncoder().encode(works_dict)
#workfile.write(worksjson)
#workfile.close()

#tropefile = open("tropes", 'w')
#tropesjson = json.JSONEncoder().encode(tropes_dict)
#tropefile.write(tropesjson)
#tropefile.close()

#creatorfile = open("creators", 'w')
#creatorsjson = json.JSONEncoder().encode(creators_dict)
#creatorfile.write(creatorsjson)
#creatorfile.close()

print "made and wrote dicts of works, tropes, and creators"

for page,info in fixed_dict.iteritems():
    indexes = range(0,len(info[1]))
    for j in reversed(indexes):
        name = info[1][j].split('/')[-1]
        info[1][j] = name

        try:
            lookup = fixed_dict[name]
        except KeyError:
            del info[1][j]
        else:
            if lookup[0] != "Trope":
                del info[1][j]

print "removed non-trope links from works"


print fixed_dict["IronMan3"]

dumpfile = open("dumpfile", 'w')
goodjson = json.JSONEncoder().encode(fixed_dict)
dumpfile.write(goodjson)

print "dumpfile written"

dumpfile.close()

print "DONE"

    
