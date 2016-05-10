import graphlab
from numba import autojit

def readfile():
    return graphlab.SFrame.read_csv('sframe_big.csv', delimiter='`')

sframe = readfile();

data_train, data_test = graphlab.recommender.util.random_split_by_user(sframe, user_id='title', item_id='trope', item_test_proportion=0.2)

@autojit
def makeModel():
    return graphlab.recommender.ranking_factorization_recommender.create(data_train, user_id='title', item_id='trope', target='hasTrope', solver='sgd')

model = makeModel();

@autojit
def doEval():
    return model.evaluate(data_test, target='hasTrope')

eva = doEval();

print "DONE"
