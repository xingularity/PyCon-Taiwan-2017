# PyConTW2017_Talk

## Requirement
* pandas >= 0.20
* ipython >= 5.0.0
* jupytertheme >= 0.16

## Errata from PyCon Taiwan 2017 Talk
* Incorrect code for changing column orders
  Original code 
  ```
  df.columns = ['UserID', 'MovieID', 'Rating', 'rating_dt', 'Timestamp']
  ```
  should be changed to 
  ```
  df = df[['UserID', 'MovieID', 'Rating', 'rating_dt', 'Timestamp']]
  ```
* Inter-Quantile Range should be Interquartile range

