import helper as hl
from helper import Helper as h
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from joblib import dump,load
from sklearn.ensemble import RandomForestClassifier


#Load dataset
class ModelBuilder:
    
    def __init__(self, x, y)->pd.DataFrame:
        self.x = x
        self.y=y
        print ("your dataset is loaded!")
    # creating train test splits
    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=40)
    
    
    # creating scaler scale var.
    norm = MinMaxScaler()
    # fit the scal
    norm_fit = norm.fit(xtrain)
    dump(norm_fit,'model/scaler.joblib')
    # transfromation of trainig data
    scal_xtrain = norm_fit.transform(xtrain)
    
    # transformation of testing data
    scal_xtest = norm_fit.transform(xtest)
    print(scal_xtrain)
    
    
    
    
    
    # create model variable
    rnd = RandomForestClassifier()
    
    # fit the model
    fit_rnd = rnd.fit(scal_xtrain,ytrain)
    
    # checking the accuracy score
    rnd_score = rnd.score(scal_xtest,ytest) 
    
    print('score of model is : ',rnd_score)
    
    dump(rnd, 'model/model.joblib')
            
if __name__=='__main__':
    x=hl.read_csv('data/train.csv') 
    y=hl.read_csv('data/test.csv') 
    ModelBuilder(x,y)
    print ("your model is saved")
    print (len(y))
   
