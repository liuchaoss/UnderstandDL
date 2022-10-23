# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
import random
import csv
import pickle as pk
import os
import shutil

csv.field_size_limit(500 * 1024 * 1024)

# from nltk import pos_tag, word_tokenize, RegexpParser
# from nltk.stem import PorterStemmer

# ps = PorterStemmer()


# def get_tags_from_sentence(sent):
#     return pos_tag(word_tokenize(sent))


def sort_dict_by_values(stat):
    return dict(sorted(stat.items(), key=lambda item: item[1], reverse=True))


def dict2list(stat):
    return [[k, v] for k, v in stat.items()]


def cp(pin, pout):
    shutil.copyfile(pin, pout)


def load_csv(path):
    reader = csv.reader(open(path, 'r', encoding='latin1'), delimiter=',')
    lines = []
    for r in reader:
        lines.append(r)
    return lines


def save_csv(path, lines):
    writer = csv.writer(open(path, 'w', encoding='utf-8', newline=''), delimiter=',')
    writer.writerows(lines)


def append_file(path, line):
    with open(path, 'a') as file:
        file.write(line + '\n')
        file.flush()


def load_txt(path):
    lines = open(path, 'r', encoding='latin1').readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    return lines


def save_txt(path, lines):
    with open(path, 'w', encoding='latin1') as file:
        for line in lines:
            file.write(line + '\n')


def save_pkl(path, data):
    pk.dump(data, open(path, 'wb'))


def load_pkl(path):
    return pk.load(open(path, 'rb'))


def load_html(path):
    return open(path, 'r', encoding='utf-8').read()


def get_random_header():
    agents = load_txt('data/crawl_user_agents.txt')
    ips = load_txt('data/crawl_user_agents.txt')

    ip = random.choice(ips)
    agent = random.choice(agents)
    header = {'User-Agent': agent,
              'proxies': ip,
              'ue': 'utf-8'}
    return header


# def get_ip_list():
#     urlip = 'http://www.xicidaili.com/wt/'
#     req = Request(urlip, headers={'User-Agent': 'Mozilla/5.0'})
#     html = urlopen(req).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     ips = soup.find_all('tr')
#     ip_list = []
#     for i in range(1, len(ips)):
#         ip_info = ips[i]
#         tds = ip_info.find_all('td')
#         ip_list.append(tds[1].text + ':' + tds[2].text)
#     with open('data/proxy_ips.txt', 'a', encoding='utf-8') as file:
#         for line in ip_list:
#             file.write(line + '\n')


# def test_random_header():
#     for i in range(1000):
#         header = get_random_header()
#         req = Request('https://www.baidu.com', headers=header)
#         html = urlopen(req).read()
#         print(header)
#         print(html)


# def get_html(url):
#     header = get_random_header()
#     req = Request(url, headers=header)
#     html = urlopen(req).read()
#     parsed_html = BeautifulSoup(html, 'html.parser')
#     return html


def split_file(path, size):
    data = []
    lines = load_csv(path)
    idx = 1
    for line in lines:
        data.append(line)
        if len(data) == size:
            save_csv(path[:-4] + str(idx) + '.csv', data)
            data = []
            idx = idx + 1
    if len(data) > 0:
        save_csv(path[:-4] + str(idx) + '.csv', data)


def deldir(dir):
    if not os.path.exists(dir):
        return False
    if os.path.isfile(dir):
        os.remove(dir)
        return
    for i in os.listdir(dir):
        t = os.path.join(dir, i)
        if os.path.isdir(t):
            deldir(t)
        else:
            os.unlink(t)
    os.removedirs(dir)


if __name__ == '__main__':
    # get_ip_list()
    # deldir('../github_clone_repos/0')
    append_file('clone.csv', 'a,s,s,s')
