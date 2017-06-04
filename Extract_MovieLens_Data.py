
# coding: utf-8

# # This notebook is to extract data from Movie Lens
# * The data contents are explained in http://files.grouplens.org/papers/ml-1m-README.txt
# 
# ## users.dat
# 
# UserID::Gender::Age::Occupation::Zip-code
# - Gender is denoted by a "M" for male and "F" for female
# - Age is chosen from the following ranges:
# 
# 	*  1:  "Under 18"
# 	* 18:  "18-24"
# 	* 25:  "25-34"
# 	* 35:  "35-44"
# 	* 45:  "45-49"
# 	* 50:  "50-55"
# 	* 56:  "56+"
# 
# - Occupation is chosen from the following choices:
# 
# 	*  0:  "other" or not specified
# 	*  1:  "academic/educator"
# 	*  2:  "artist"
# 	*  3:  "clerical/admin"
# 	*  4:  "college/grad student"
# 	*  5:  "customer service"
# 	*  6:  "doctor/health care"
# 	*  7:  "executive/managerial"
# 	*  8:  "farmer"
# 	*  9:  "homemaker"
# 	* 10:  "K-12 student"
# 	* 11:  "lawyer"
# 	* 12:  "programmer"
# 	* 13:  "retired"
# 	* 14:  "sales/marketing"
# 	* 15:  "scientist"
# 	* 16:  "self-employed"
# 	* 17:  "technician/engineer"
# 	* 18:  "tradesman/craftsman"
# 	* 19:  "unemployed"
# 	* 20:  "writer"
# 
# ## movies.dat
# MovieID::Title::Genres
# 
# ## ratings.dat
# UserID::MovieID::Rating::Timestamp

# In[1]:

import pandas as pd


# In[3]:

users_df = pd.read_csv("./ml-1m/users.dat"
                    , sep='::'
                    , header=None
                    , names=["UserID", "Gender", "Age", "Occupation", "Zip-code"])
ocupation_codes = {'ocupation_code': [x for x in range(21)]
                   , 'Occupation_name': ["other or not specified", "academic/educator", "artist"
                                  , "clerical/admin", "college/grad student", "customer service"
                                  , "doctor/health care", "executive/managerial", "farmer"
                                  , "homemaker", "K-12 student", "lawyer", "programmer", "retired"
                                  , "sales/marketing" ,"scientist", "self-employed", "technician/engineer"
                                  , "tradesman/craftsman", "unemployed", "writer"]
                  }
ocupation_codes = pd.DataFrame(ocupation_codes)
users_df = users_df.merge(ocupation_codes, left_on=["Occupation"], right_on=["ocupation_code"], how='left')
users_df = users_df.drop(["Occupation", "ocupation_code"], axis=1).rename(columns={'Occupation_name': 'Occupation'})


# In[4]:

movies_org_df = pd.read_csv("./ml-1m/movies.dat"
                            , sep='::'
                            , header=None
                            , names=["MovieID", "Title", "Genres"])
rows = []
for _, row in movies_org_df.iterrows():
    for gen in row.Genres.split('|'):
        rows.append([row['MovieID'], row['Title'], gen])
movies_df = pd.DataFrame(rows, columns=movies_org_df.columns)


# In[5]:

ratings_df = pd.read_csv("./ml-1m/ratings.dat"
                         , sep='::'
                         , header=None
                         , names=["UserID", "MovieID", "Rating", "Timestamp"])
ratings_df['rating_dt'] = pd.to_datetime(ratings_df['Timestamp'],unit='s')

