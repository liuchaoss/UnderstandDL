### Dataset

- rawdata.csv: the collected dataset (title, tags, id, viewcount, score, creation date of post, creation date of answer, tokens).

- rawdata-preprocess.csv: preprocessed rawdata.csv (id, framework type (0: tensorflow, 1: pytorch, 2: theano), viewcount, score, year, response time, level-I token, level-II token).

- rawdata-table.xlsx: tables of taxonomy, popularity, and difficulty.

- rawdata-summary.xlsx: tables of taxonomy subcategories.

### Scripts

- preprocess.py: taking rawdata.csv as input, and generating the rawdata-preprocess.csv with all digits.

- stat_analysis.py: analyzing post popularity and difficulty.

- util.py: tools to support the above two scripts.
