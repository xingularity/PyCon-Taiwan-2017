# PyConTW2017_Talk

## Requirement
* pandas >= 0.20
* ipython >= 5.0.0
* jupytertheme >= 0.16

## Usage
1. git clone this reporitory
2. Make sure pandas, jupyter notebook and jupyterthem are installed with proper versions.
3. Travel to repository directory
4. Run all cells within "Talk Slide.ipynb"
5. ipython nbconvert Talk\ Slides.ipynb --to slides --post serve
## Errata from PyCon Taiwan 2017 Talk
* Incorrect code for changing column orders 

  Original Code:  
  ```
  df.columns = ['UserID', 'MovieID', 'Rating', 'rating_dt', 'Timestamp']
  ```
  should be changed to 
  ```
  df = df[['UserID', 'MovieID', 'Rating', 'rating_dt', 'Timestamp']]
  ```
* "Inter-Quantile Range" should be Interquartile range

