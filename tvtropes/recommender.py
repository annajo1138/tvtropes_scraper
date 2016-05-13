import graphlab
from numba import autojit

# numba/autojit is a python compiler that optimizes for Intel processors.
# If you don't have it installed just delete the import and decorators.

def readfile():
    return graphlab.SFrame.read_csv('sframe.csv', delimiter='`')

sframe = readfile();

# these are correct
userid = 'title'
itemid = 'trope'

data_train, data_test = graphlab.recommender.util.random_split_by_user(sframe, user_id=userid, item_id=itemid, item_test_proportion=0.2)

@autojit
def makeModel():
    return graphlab.recommender.ranking_factorization_recommender.create(data_train, user_id=userid, item_id=itemid, target='hasTrope', solver='sgd')

model = makeModel();

@autojit
def doEval():
    return model.evaluate(data_test, target='hasTrope')

eva = doEval();

print "DONE"
