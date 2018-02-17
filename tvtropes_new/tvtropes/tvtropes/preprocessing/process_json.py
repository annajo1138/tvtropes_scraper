import json
import ast

def nameToUrl(string):
    return string.strip()

def namespaceFromUrl(string):
    return string.split("/")[-2]

def titleFromUrl(string):
    return string.split("/")[-1].split("?")[0]

json_file = open("../tropes_01-22-2018.json")
print("json file")

json_str = json_file.read()
print("json string")

decoder = json.JSONDecoder()
print("file opened")

json_dict = decoder.decode(json_str)
print("loaded")

json_file.close()

length = range(0,len(json_dict))

# all_namespaces = set()
# for i in length:
#     all_namespaces.add(json_dict[i]['namespace'])
#     # if json_dict[i]['namespace'] == 'FullmetalAlchemist':
#     #     print("HI SHORTY")
#
# for name in all_namespaces:
#     print(name)

# from list at http://tvtropes.org/pmwiki/pmwiki.php/Administrivia/Namespace
# made them all lowercase and only compare against .lower() because they're
# super inconsistent about this stuff
work_namespaces = ["advertising", "animation", 'anime', 'arg', 'art',
    'audioplay', 'blog', 'bollywood', 'comicbook', 'comicstrip', 'fanfic',
    'film', 'franchise', 'larp', 'letsplay', 'lightnovel', 'literature',
    'machinima', 'magazine', 'manga', 'manhua', 'manhwa', 'music', 'myth',
    'pinball', 'podcast', 'radio', 'ride', 'roleplay', 'script', 'series',
    'tabletopgame', 'theatre', 'toys', 'videogame', 'visualnovel',
    'webanimation', 'webcomic', 'website', 'weboriginal', 'webvideo',
    'westernanimation', 'wiki', 'wrestling']





# work_and_review = 0
# work_and_no_review = 0
# other_and_review = 0
# other_and_no_review = 0
#
# for i in length:
#     if json_dict[i]['namespace'] in work_namespaces:
#         if json_dict[i]['can_review']:
#             work_and_review += 1
#         else:
#             work_and_no_review += 1
#     else:
#         if json_dict[i]['can_review']:
#             other_and_review += 1
#         else:
#             other_and_no_review += 1
#
# print("work and review:", work_and_review)
# print("work and no review:", work_and_no_review)
# print("other and review:", other_and_review)
# print("other and no review:", other_and_no_review)

# results on Jan. scrape:
# work and review: 75484
# work and no review: 10653
# other and review: 12281
# other and no review: 275760
# in other words, using can_review is useless


work_dict = {}

print("building work dict")
# if a title is in a work namespace, we keep it
# throw away everything else
for i in length:
    if json_dict[i]['namespace'].lower() in work_namespaces:
        work_dict[titleFromUrl(json_dict[i]['url_name'])] = json_dict[i]['all_links']

# if a namespace matches a work name, throw all of its stuff in with that work
for i in length:
    if json_dict[i]['namespace'] in work_dict.keys():
        work_dict[json_dict[i]['namespace']] += json_dict[i]['all_links']

# if a namespace matches a trope name, we don't care; we're only getting
# the trope side of the matrix from the works; if a trope isn't linked from
# a work, it's kind of useless

# clean up all the links in the work dict

print("cleaning up all links")
key_list = work_dict.keys()

for key, val in work_dict.items():
    cleaned_links = []
    for i in range(len(val)):
        clean = titleFromUrl(val[i])
        if clean not in key_list:
            cleaned_links += [clean] # python why
    work_dict[key] = cleaned_links

print(work_dict["FullmetalAlchemist"])

print("writing clean json")
workfile = open("tropes_01-22-2018_clean.json", 'w')
# worksjson = json.JSONEncoder().encode(work_dict)
# workfile.write(worksjson)
json.dump(work_dict, workfile, indent=4)
workfile.close()



    # for name in loaded[i]['title']:
    #     if len(title) < 1:
    #         #get rid of broken names
    #         loaded[i]['title'].remove(title)

# for i in reversed(length):
#     if len(loaded[i]['title']) < 1:
#         #sometimes it fails to grab the name
#         del loaded[i]
#
# print "broken names gone"
#
# length = range(0,len(loaded))
#
# fixed_dict = {}
# #essentially doing reduceByKey on the dictionary
#
# for i in length:
#     title = loaded[i]['title'][0].replace(" ", "")
#     try:
#         if fixed_dict[title][0] == "Trope" and loaded[i]['pageType'] == "Work":
#             fixed_dict[title][0] = "Work"
#         fixed_dict[title][1].extend(loaded[i]['all_links'])
#     except KeyError:
#         fixed_dict[title] = [loaded[i]['pageType'], loaded[i]['all_links']]
#
# print "did reduce by title on dictionary"
#
# #works_dict = {}
# #tropes_dict = {}
# #creators_dict = {}
#
# #for page,info in fixed_dict.iteritems():
# #    if info[0] == "Work":
# #        works_dict[page] = info
# #    elif info[0] == "Trope":
# #        tropes_dict[page] = info
# #    elif info[0] == "Creator":
# #        creators_dict[page] = info
#
# #workfile = open("works", 'w')
# #worksjson = json.JSONEncoder().encode(works_dict)
# #workfile.write(worksjson)
# #workfile.close()
#
# #tropefile = open("tropes", 'w')
# #tropesjson = json.JSONEncoder().encode(tropes_dict)
# #tropefile.write(tropesjson)
# #tropefile.close()
#
# #creatorfile = open("creators", 'w')
# #creatorsjson = json.JSONEncoder().encode(creators_dict)
# #creatorfile.write(creatorsjson)
# #creatorfile.close()
#
# print "made and wrote dicts of works, tropes, and creators"
#
# for page,info in fixed_dict.iteritems():
#     indexes = range(0,len(info[1]))
#     for j in reversed(indexes):
#         name = info[1][j].split('/')[-1]
#         info[1][j] = name
#
#         try:
#             lookup = fixed_dict[name]
#         except KeyError:
#             del info[1][j]
#         else:
#             if lookup[0] != "Trope":
#                 del info[1][j]
#
# print "removed non-trope links from works"
#
#
# print fixed_dict["IronMan3"]
#
# dumpfile = open("dumpfile", 'w')
# goodjson = json.JSONEncoder().encode(fixed_dict)
# dumpfile.write(goodjson)
#
# print "dumpfile written"
#
# dumpfile.close()
#
# print "DONE"
