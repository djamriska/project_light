__author__ = 'Nick Hirakawa'

# todo: figure out how to credit original program to the author
# todo: figure out all required modules and build a requirements.txt
#
from parse import *
from query import QueryProcessor
import operator
import json


def main():
	# todo: change this to read in from a database
	# todo: design new database structure to store this information
	qp = QueryParser(filename='../text/queries.txt')
	cp = CorpusParser(filename='../text/corpus.txt')
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
	#for article in articles:
	#	print(articles[article])

	print(articles[1][1]['title'])
	print(articles[2][2]['title'])

	#print(articles)

	proc = QueryProcessor(queries, corpus, keywords)
	results = proc.run()
	qid = 0
	data = {}
	data['Rankings'] = []
	for result in results:
		sorted_x = sorted(result.items(), key=operator.itemgetter(1))
		sorted_x.reverse()
		index = 0
		for i in sorted_x[:100]:
			tmp = (qid, i[0], index, i[1])
			# todo: add lookup to the original article and add to output
			# print('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp))
			# todo: change this to CSV out
			# todo: add title, both ranking scores, url, date, # of comments
			data['Rankings'].append({'docId': i[0], 'Score': i[1]})
			# print(articles.get('78'))
			# todo: add ability to write this information out to a data file
			# todo: create process to read in file and display on website
			# todo: we may want to set this up as a panda's data frame to merge with files
			index += 1
		qid += 1
	# todo: change this to CSV out
	# with open('../text/rankings.txt', 'w') as outfile:
	#	json.dump(data, outfile)
# todo: setup the ability to pass K and b in as paramters


if __name__ == '__main__':
	main()
