import json
import metapy
import pandas as pd
from pandas.io.json import json_normalize

metapy.log_to_stderr()


def split_title(title):
    print(title.split())


def test_article_filter(string_in, filter_list):
    # This function compares the article title against a list of currently active filters and indicates if the article
    # is of interest
    # This should return back the ID of the record to be updated (or figure out if I can update the database as interest
    if any(s in string_in for s in filter_list):
        print("Article of Interest Found: {}".format(string_in))


def normalize_json_data():
    # This is a function to read in the file that was loaded and return a pandas data frame that has been normalized
    # Need to verify that this will work
    # Todo: build doc strings
    pass


def read_article_files():
    # This should read from the file / database a list of all currently active article filters
    # Return back a tuple of the active terms
    # todo:build docs string
    pass


def set_article_filters():
    # This should read from the file / database a list of all currently active comment keywords
    # Return back a tuple of active keywords
    # todo:build doc string
    pass


def set_comment_keywords():
    keywords = ('Race', 'arrest', 'illegal', 'alien', 'white people', 'police', 'black', 'criminal', 'gay', 'kill', 'murder')
    return keywords


def test_comment_keywords(string_in, test_keywords, doc_in):
    if any(s in string_in for s in test_keywords):
        print("Comment of Interest Found: {}".format(string_in))
        tokenize_comment(string_in, doc_in)


def sorted_dict_values1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]


def tokenize_comment(string_in, work_doc):
    tok = metapy.analyzers.ICUTokenizer()
    tok = metapy.analyzers.LengthFilter(tok, min=3, max=30)  # remove small words
    tok = metapy.analyzers.LowercaseFilter(tok)
    tok = metapy.analyzers.ListFilter(tok, "c:\lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
    tok = metapy.analyzers.Porter2Filter(tok)

    work_doc.content(string_in)
    tok.set_content(doc.content())  # this could be any string
    tokens = [token for token in tok]
    print(tokens)
    ana = metapy.analyzers.NGramWordAnalyzer(1, tok)
    print(doc.content())
    unigrams = ana.analyze(doc)
    print(unigrams)


# Start program
# Load Article Files
with open('test2.json') as f:
    d = json.load(f)

# Normalize the JSON Data
articleSet = json_normalize(d['programs'])

# setup filters and keywords - these should be function calls
# todo: load function calls for articles
NotOkList = ('inmate', 'victim')
ArticleFilter = ('inmate', 'victim')
CommentKeywords = set_comment_keywords()

# Check the data
print(articleSet.head(5))

# Set an Index
# We should setup the article scraper to have a unique ID when loaded, for now use Title
# Todo: Change this to include a GUID

df2 = articleSet.set_index("Title", drop=False)

#  send each article to the tester and figure out if of interest(we may not want to make a function call, lamba??)
for index, row in df2.iterrows():
    # print(row['Title'], row['Author'])
    # splitTitle(row['Title'])
    # print(row['Title'])
    print(test_article_filter(row['Title'], ArticleFilter))

# Loading Comments for articles of interest
with open('comments.json') as f:
    d = json.load(f)

articleSet = json_normalize(d['Comments'])

df3 = articleSet.set_index("Comment_Id", drop=False)
doc = metapy.index.Document()

for index, row in df3.iterrows():
    # print(row['Title'], row['Author'])
    # splitTitle(row['Title'])
    # print(row["Comment_Id"],row['Comment'])
    test_comment_keywords(row['Comment'], CommentKeywords, doc)


