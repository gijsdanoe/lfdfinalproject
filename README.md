# lfdfinalproject
Final project Learning from Data by Gijs Danoe, Ate Jordaan and Jan Harms.

Needed:
- COP climate change data
- Kaggle all the news dataset. Download: https://www.kaggle.com/snapcrack/all-the-news

Data preparation:
  Climate change:
    1. Run train.py (OD stands for out-of-domain and refers to climate change news). This produces a training file (trainOD.csv).

  Non-climate change:
    1. Run testcombine.py. This combines the three Kaggle folds into combined_csv.csv.
    2. Run filter.py with command line argument 'all'. This produces a test file (test.csv) which does not contain any climate change data using wordlist.txt.
    3. Run testsplit.py. This produces three files: trainID.csv, devID.csv and testID.csv. (ID stand for in domain and refers to non-climate change news).
    4. For subdomain data, run filter.py with command line argument 'trump', 'police', 'education, 'immigration' or 'economy'. This will produce the corresponding          test files.
    
  Finally, put all files into a Drive map. To skip this, you can access the data Drive map at:             https://drive.google.com/drive/folders/1UCkRpxcXYOWS2WNMYVWetVSg9TwHIkNb?usp=sharing
    
Models:
- SVM:
- LSTM:
- BERT: connect the data map and run all cells of bert.ipynb.


