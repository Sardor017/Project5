import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import *
from sklearn.preprocessing import OrdinalEncoder

def add_new_features(df):
    df['BMI'] = df['weight(kg)'] / ((df['height(cm)'] / 100) ** 2)
    df['WHR'] = df['waist(cm)'] / df['height(cm)']
    def categorize_blood_pressure(row):
        if row['systolic'] < 90 or row['relaxation'] < 60:
            return 'Low'
        elif 90 <= row['systolic'] < 120 and 60 <= row['relaxation'] < 80:
            return 'Normal'
        else:
            return 'High'
    df['Blood_Pressure_Category'] = df.apply(categorize_blood_pressure, axis=1)
    df['Cholesterol_Ratio'] = df['HDL'] / df['LDL']
    df['Liver_Enzyme_Ratio'] = df['AST'] / df['ALT']
    df['Hemoglobin_Gtp_Ratio'] = df['hemoglobin'] / df['Gtp']
    df['Systolic_Diastolic_Ratio'] = df['systolic'] / df['relaxation']
    return df

def add_advanced_features(df):
    df['Hearing_Imbalance'] = df['hearing(left)'] - df['hearing(right)']
    df['Eyesight_Imbalance'] = df['eyesight(left)'] - df['eyesight(right)']
    return df

def ordinal_encode_categories(df, columns):
    encoder = OrdinalEncoder()
    df[columns] = encoder.fit_transform(df[columns])
    return df

def WoE_create_and_encode_categories(df):
    ordinal_encoder = OrdinalEncoder()
    df['Age_Cat'] = pd.qcut(df['age'], q=5)
    df['Age_Cat'] = ordinal_encoder.fit_transform(df[['Age_Cat']])
    df['Waist_Cat'] = pd.qcut(df['waist(cm)'], q=5)
    df['Waist_Cat'] = ordinal_encoder.fit_transform(df[['Waist_Cat']])
    df['triglyceride_Cat'] = pd.qcut(df['triglyceride'], q=5)
    df['triglyceride_Cat'] = ordinal_encoder.fit_transform(df[['triglyceride_Cat']])
    return df

def process_dataframe(df):
    df = add_new_features(df)
    df = add_advanced_features(df)
    df = ordinal_encode_categories(df, ["Blood_Pressure_Category"])
    WoE_create_and_encode_categories(df)
    return df

def useful_features(data):
    data = process_dataframe(data)
    columns = ['height(cm)', 'weight(kg)', 'waist(cm)', 'eyesight(left)', 'eyesight(right)', 'hearing(left)', 'hearing(right)', 'systolic',
       'triglyceride', 'HDL', 'LDL', 'hemoglobin', 'Urine protein', 'serum creatinine', 'AST', 'ALT', 'Gtp', 'dental caries', 'BMI','WHR',
       'Blood_Pressure_Category', 'Cholesterol_Ratio', 'Liver_Enzyme_Ratio', 'Hemoglobin_Gtp_Ratio', 'Systolic_Diastolic_Ratio', 
       'Hearing_Imbalance', 'Eyesight_Imbalance', 'Age_Cat', 'Waist_Cat', 'triglyceride_Cat']
    if 'smoking' in data.columns:
        columns.append('smoking')
    return data[columns]