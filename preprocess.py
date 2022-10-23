import util
from datetime import datetime

lines = util.load_csv('rawdata.csv')
code = util.load_csv('taxonomy-code.csv')
data = []
for line in lines:
    title = line[0]
    tag = line[1]
    if 'tensorflow' in tag:
        tag = 0
    elif 'pytorch' in tag:
        tag = 1
    elif 'theano' in tag:
        tag = 2
    id = int(line[2])
    viewcount = int(line[3])
    score = int(line[4])

    question_creation_data = datetime.strptime(line[5], '%Y-%m-%dT%H:%M:%S.%f')
    answer_creation_data = datetime.strptime(line[6], '%Y-%m-%dT%H:%M:%S.%f')
    year = question_creation_data.year
    delta = answer_creation_data - question_creation_data
    response = round(delta.total_seconds() / 60 / 60 / 24, 2)

    label = line[7] + ','
    level1 = -1
    level2 = -1
    for c in code:
        key = c[0] + ','
        if key in label:
            level1 = int(c[1])
            level2 = int(c[2])
            break

    d = [id, tag, viewcount, score, year, response, level1, level2]
    data.append(d)

util.save_csv('rawdata-preprocess.csv', data)
