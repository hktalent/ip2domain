import numpy as np

# def eculidDisSim(x,y):
#     '''
#     欧几里得相似度
#     '''
#     return np.sqrt(sum(pow(a-b,2) for a,b in zip(x,y)))
# 这个不错
def cosSim(x,y):
    '''
    余弦相似度
    '''
    tmp=np.sum(x*y)
    non=np.linalg.norm(x)*np.linalg.norm(y)
    return np.round(tmp/float(non),9)
def pearsonrSim(x,y):
    from scipy.stats import pearsonr
    '''
    皮尔森相似度
    '''
    return pearsonr(x,y)[0]

# def manhattanDisSim(x,y):
#     '''
#     曼哈顿相似度
#     '''
#     return sum(abs(a-b) for a,b in zip(x,y))

if __name__=='__main__':
    a=np.array([1,5,4])
    b=np.array([6,5,4])
    sim=manhattanDisSim(a,b)
    print(sim)