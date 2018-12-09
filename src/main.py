__author__ = 'Nick Hirakawa'

# todo: figure out how to credit original program to the author
# todo: figure out all required modules and build a requirements.txt
#
from parse import *
from query import QueryProcessor
import operator
import json
import csv


def main():
    # todo: change this to read in from a database
    # todo: design new database structure to store this information
    qp = QueryParser(filename='../text/queries.txt')
    cp = CorpusParser(filename='../text/corpus.txt')
    cp = CorpusParser(filename='../text/comments.txt')
    kw = KeywordParser(filename='../text/weights.txt')
    ar = ArticleParser(filename='../text/articles.txt')
    qp.parse()
    queries = qp.get_queries()
    cp.parse()
    corpus = cp.get_corpus()
    kw.parse()
    keywords = kw.get_keywords()
    ar.parse()
    articles = ar.get_articles()
    proc = QueryProcessor(queries, corpus, keywords)
    results = proc.run()
    qid = 0
    data = {}
    csv_columns = 'docid, rank_score, bm25_custom, title, source, pub_date, pub_url\n'
    with open('../text/rankings.csv', 'w') as f:
        f.write(csv_columns)
    for result in results:
        sorted_x = sorted(result.items(), key=operator.itemgetter(1))
        sorted_x.reverse()
        index = 0
        j = 0
        for i in sorted_x[:100]:
            tmp = (qid, i[0], index, i[1])
            # todo: add lookup to the original article and add to output
            # print('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp))
            j += 1
            score = i[1]
            docid = i[0]
            title = articles[int(i[0])]['title'].rstrip()
            pub_url = articles[int(i[0])]['pub_url'].rstrip()
            pub_date = articles[int(i[0])]['pub_date'].rstrip()
            source = articles[int(i[0])]['source'].rstrip()
            data.update({'docId': i[0], 'rank_score': j, 'Score': score, 'source': source, 'title': title,
            						'pub_date': pub_date})
            out_string = docid + ', ' + str(j) + ', '+str(round(score,4))+', "' + title + '", "' + source + '", "'+pub_date + '", "' + pub_url + '"\n'
            with open('../text/rankings.csv', 'a') as f:
                f.write(out_string)
            # todo: create process to read in file and display on website
            index += 1
        qid += 1
    # todo: setup the ability to pass K and b in as paramters



if __name__ == '__main__':
    main()
