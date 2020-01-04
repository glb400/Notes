#文本中获取特征
#coding:utf-8
from numpy import *
import sys
sys.path.append("E:\....")

##从文本中构建向量
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    ##分别表示标签
    return postingList,classVec ##返回输入数据和标签向量
                 
def createVocabList(dataSet):
    vocabSet = set([])  
    for document in dataSet:
        vocabSet = vocabSet | set(document) 
    return list(vocabSet)##输出不重复的元素

def setOfWords2Vec(vocabList, inputSet):###判断了一个词是否出现在一个文档当中。
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec###输入中的元素在词汇表时，词汇表相应位置为1，否则为0

'''
#测试
dataSet,classes = loadDataSet()
print(dataSet)
vocabList = createVocabList(dataSet)
print(vocabList)
setWordsVec = setOfWords2Vec(vocabList,dataSet[0])
print(setWordsVec)
'''

#得到每个特征的条件概率
##得到每个特征的条件概率
def trainNB0(trainMatrix,trainCategory):###输入的文档信息和标签
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)      
    p0Denom = 2.0
    p1Denom = 2.0                     
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)          
    p0Vect = log(p0Num/p0Denom)   
    return p0Vect,p1Vect,pAbusive
'''
#测试
dataSet,classes = loadDataSet()
vocabList = createVocabList(dataSet)
trainMat = []
for item in dataSet:
    trainMat.append(setOfWords2Vec(vocabList,item))
                    
p0v,p1v,pAb = trainNB0(trainMat,classes)
print(p0v)
print(p1v)
print(pAb)
'''

#分类
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

#词袋模型(返回所有词汇出现的次数）
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)
'''
#测试
testingNB()
'''