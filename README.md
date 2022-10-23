### *** Dataset ***

- 1. rawdata.csv: the collected dataset (title, tags, id, viewcount, score, creation date of post, creation date of answer, tokens).

- 2. rawdata-preprocess.csv: preprocessed rawdata.csv (id, framework type (0: tensorflow, 1: pytorch, 2: theano), viewcount, score, year, response time, level-I token, level-II token).

- 3. rawdata-table.xlsx: tables of taxonomy, popularity, and difficulty.

- 4. rawdata-summary.xlsx: tables of taxonomy subcategories.

### *** Scripts ***

- 1. preprocess.py: taking rawdata.csv as input, and generating the rawdata-preprocess.csv with all digits.

- 2. stat_analysis.py: analyzing post popularity and difficulty.

- 3. util.py: tools to support the above two scripts.