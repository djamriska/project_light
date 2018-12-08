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
	# cp = CorpusParser(filename='../text/corpus.txt')
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
	data['Rankings'] = []
	for result in results:
		sorted_x = sorted(result.items(), key=operator.itemgetter(1))
		sorted_x.reverse()
		index = 0
		j = 0
		for i in sorted_x[:100]:
			tmp = (qid, i[0], index, i[1])
			# todo: add lookup to the original article and add to output
			# print('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp))
			# art_dict = articles[1][int(i[0])]

			print('docid: {0}, rank:{1}, score: {2}, title: {3}'.format(int(i[0]), j, round(i[1],2), articles[int(i[0])]['title']))
			# work_dict[docid]['pub_url'] = pub_url
			# work_dict[docid]['pub_date'] = pub_date
			j += 1
			# print(art_dict['title'], art_dict['source'], art_dict['pub_date'], art_dict['pub_url'])
			# todo: change this to CSV out
			# todo: add title, both ranking scores, url, date, # of comments
			#data['Rankings'].append({'docId': i[0], 'rank_score': j, 'Score': i[1], 'source': art_dict['source'], 'title': art_dict['title'],
			#						'pub_date': art_dict['pub_date']})
			#print(data)
			# todo: add ability to write this information out to a data file
			# todo: create process to read in file and display on website
			# todo: we may want to set this up as a panda's data frame to merge with files
			index += 1
		qid += 1
	# todo: change this to CSV out
	#with open('../text/rankings.txt', 'w') as outfile:
	#	json.dump(data, outfile)
	#csv_columns = ['docid', 'rank_score', 'score', 'source', 'title', 'pub_date']
	#with open('../text/rankings.csv', 'w') as csv_out_file:
	#	writer = csv.DictWriter(csv_out_file, fieldnames=csv_columns)
	#	for d in data:
	#		writer.writerow(d)
# todo: setup the ability to pass K and b in as paramters


if __name__ == '__main__':
	main()
