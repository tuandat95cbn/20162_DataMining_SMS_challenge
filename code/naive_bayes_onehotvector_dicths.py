# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:27:49 2017

@author: T420
"""
f = open('train.txt', 'r')
g = open('test.txt','r')
test= g.read().splitlines()
g.close()
g=open('spam-harm-dict.txt','r')
e=g.read();
dictHarmSpam=e.split(' ');
print set(dictHarmSpam).__len__()
g.close()
def getInputOneHotVector(data,dict):
    inputY=[]
    inputWord=[];
    for x in data:
        y=x.split(" ")
        inputWord.append(y[1:])
        inputY.append(y[0])
    inputX=[]

    for x in inputWord:
        v=[]
        for xx in dict:
            if xx in x:
                v.append(1)
            else:
                v.append(0)
        for xx in dictHarmSpam:
            if xx in x:
                v.append(1)
            else:
                v.append(0)
        inputX.append(v)
    return inputX,inputY
#f.read()
LTrain=100
nTimes=1
t= f.read().splitlines()
f.close()
nTrain=t.__len__()
dict=[]
def aRunProcess(dict):
    inputY=[]
    for x in t:
        y=x.split(" ")
        dict.extend(y[1:])
    dict=set(dict)
    inputX=[]

    [inputX,inputY]=getInputOneHotVector(t,dict);
    [testX,testY]=getInputOneHotVector(test,dict);
    trainX=inputX[:LTrain]
    trainY=inputY[:LTrain]
    

    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb.fit(trainX, trainY)
    res=gnb.predict(testX)
    print res
    #sol=(res==testY)
    #return sol.sum()
    return res
acc=0;
g0=open("test_nvb.txt","w");
res=aRunProcess(dict)
for i in range(0,test.__len__()):
    y=test[i].split(" ")
    g0.write(str(res[i])+" ")
    g0.write(" ".join(y[1:]))
    g0.write("\n");
g0.close()
testX=[]
testY=[]
g = open('test_human.txt','r')
test= g.read().splitlines()
g.close()
[testX,testY]=getInputOneHotVector(test,dict);

acc=(res==testY).sum()*1.0/test.__len__()
print "accuracy of "+str(1)+" is : "+ str(acc)
