import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def read_csv(file_name):
    dataframe=pd.read_csv(file_name)
    return dataframe
class Helper:
    def __init__(self, df:pd.DataFrame)->pd.DataFrame:
        self.df = df
        print ("your dataset is loaded!")
    
    @classmethod
    def information(self, df:pd.DataFrame)->pd.DataFrame:
        print(df.info())# to see generalinformation about the data.
        
        print(df.nunique())# summarize the number of unique values in each column
    
    @classmethod
    def missing_value (self, df:pd.DataFrame)->pd.DataFrame:
        # % of values missing in each column
        values_list = list()
        cols_list = list()
        
        for column in df.columns:
            pct_missing = np.mean(df[column].isnull())*100
            cols_list.append(column)
            values_list.append(pct_missing)
            
        pct_missing_df = pd.DataFrame()
        pct_missing_df['colums'] = cols_list
        pct_missing_df['pct_missing'] = values_list
        return pct_missing_df
    
    @classmethod
    def replce_with_median(self, df:pd.DataFrame)->pd.DataFrame:
        
        df_numeric = df.select_dtypes(include=[np.number])
        numeric_cols = df_numeric.columns.values
        
        for col in numeric_cols:
            missing = df[col].isnull()
            num_missing = np.sum(missing)
           
            if num_missing > 0:  # impute values only for columns that have missing values
                med = df[col].median() #impute with the median
                df[col] = df[col].fillna(med)
        
        print ("Missing values has been sucessfully replaced with median. ")
        return df
    
    
    @classmethod
    def replace_with_frequency(self, df:pd.DataFrame)->pd.DataFrame:
        """
        replace missing values for non numeric data type with most frequent value
        
        """
        df_non_numeric = df.select_dtypes(exclude=[np.number])
        non_numeric_cols = df_non_numeric.columns.values
        
        for col in non_numeric_cols:
            missing = df[col].isnull()
            num_missing = np.sum(missing)
           
            if num_missing > 0:  # impute values only for columns that have missing values
                mod = df[col].describe()['top'] # impute with the most frequently occuring value
                df[col] = df[col].fillna(mod)
       
        print ("Missing values has been sucessfully replaced with most frequent value. ")
        return df
        
    @classmethod
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df.drop_duplicates(inplace=True)
        
        return df    
    @classmethod
    def fix_missing_ffill(self, df: pd.DataFrame,col)->pd.DataFrame:
        df[col] = df[col].fillna(method='ffill')
        return df[col]
    
    @classmethod
    def fix_missing_bfill(self, df: pd.DataFrame, col):
        df[col] = df[col].fillna(method='bfill')
        return df[col] 
    
    
    @classmethod
    def encoder (self, df: pd.DataFrame):
        lb = LabelEncoder() 
        df['repaglinide'] = lb.fit_transform(df['repaglinide'])
        df['nateglinide'] = lb.fit_transform(df['nateglinide'])
        df['chlorpropamide'] = lb.fit_transform(df['chlorpropamide'])
        df['glimepiride'] = lb.fit_transform(df['glimepiride'])
        df['acetohexamide'] = lb.fit_transform(df['acetohexamide'])
        df['glipizide'] = lb.fit_transform(df['glipizide'])
        df['glyburide'] = lb.fit_transform(df['glyburide'])
        df['tolbutamide'] = lb.fit_transform(df['tolbutamide'])
        df['pioglitazone'] = lb.fit_transform(df['pioglitazone'])
        df['rosiglitazone'] = lb.fit_transform(df['rosiglitazone'])
        df['acarbose'] = lb.fit_transform(df['acarbose'])
        df['miglitol'] = lb.fit_transform(df['miglitol'])
        df['troglitazone'] = lb.fit_transform(df['troglitazone'])
        df['tolazamide'] = lb.fit_transform(df['tolazamide'])
        df['examide'] = lb.fit_transform(df['examide'])
        df['citoglipton'] = lb.fit_transform(df['citoglipton'])
        df['insulin'] = lb.fit_transform(df['insulin'])
        df['glyburide-metformin'] = lb.fit_transform(df['glyburide-metformin'])
        df['glipizide-metformin'] = lb.fit_transform(df['glipizide-metformin'])

        df['glimepiride-pioglitazone'] = lb.fit_transform(df['glimepiride-pioglitazone'])
        df['metformin-rosiglitazone'] = lb.fit_transform(df['metformin-rosiglitazone'])
        df['metformin-pioglitazone'] = lb.fit_transform(df['metformin-pioglitazone'])
        df['change'] = lb.fit_transform(df['change'])
        df['diabetesMed'] = lb.fit_transform(df['diabetesMed'])
        df['readmitted'] = lb.fit_transform(df['readmitted'])
        df['race'] = lb.fit_transform(df['race'])
        df['gender'] = lb.fit_transform(df['gender'])
        return df
    
    
