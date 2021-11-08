# Learning from Data final project
Final project Learning from Data by Gijs Danoe (s3494888), Ate Jordaan (s3492338) and Jan Harms (s2350904).

## Needed:
- COP climate change data
- Kaggle all the news dataset. Download: https://www.kaggle.com/snapcrack/all-the-news
- GloVe pre-trained word embeddings. Download: https://nlp.stanford.edu/projects/glove/

## Data preparation:
  Climate change:
  
    1. Run train.py (OD stands for out-of-domain and refers to climate change news). This produces a training file (trainOD.csv).

  Non-climate change:
  
    1. Run filter.py with command line argument 'all'. This combines the Kaggle folds (combined_csv.csv) and produces a test file (test.csv) which does not contain        any climate change data using wordlist.txt.
    2. Run testsplit.py. This produces three files: trainID.csv, devID.csv and testID.csv. (ID stand for in domain and refers to non-climate change news).
    3. For subdomain data, run filter.py with command line argument 'trump', 'police', 'education, 'immigration' or 'economy'. This will produce the corresponding          test files.
    
  Finally, put all files into a Drive map. To skip this, you can access our data Drive map at: https://drive.google.com/drive/folders/1UCkRpxcXYOWS2WNMYVWetVSg9TwHIkNb?usp=sharing
    
## Models:

- SVM: mount the data map, adjust the paths and run all cells of svm.ipynb.
- LSTM: mount the data map, adjust the paths and run all cells of lstm.ipynb.
- BERT: mount the data map, adjust the paths and run all cells of bert.ipynb.
