__author__ = 'Nick Hirakawa'

from invdx import build_data_structures
from rank import score_BM25


class QueryProcessor:
	def __init__(self, queries, corpus, keywords):
		self.queries = queries
		self.index, self.dlt = build_data_structures(corpus)
		self.keywords = keywords

	def run(self):
		results = []
		for query in self.queries:
			results.append(self.run_query(query))
		return results

	def run_query(self, query):
		query_result = dict()
		term_count = dict()
		for term in query:
			# look for term weights, if we don't find one assign a 1
			if self.keywords.get(term):
				weight = self.keywords.get(term)/100
			else:
				weight = 1
			print('Term: {0} Weight:{1}'.format(term, weight))
			if term in self.index:
				doc_dict = self.index[term]  # retrieve index entry
				for docid, freq in doc_dict.items():  # for each document and its word frequency
					print('\t docID: {0} Freq: {1}'.format(docid, freq))
					# print('doc ID: {0}'.format(docid))
					print('term freq in this.doc: {0}'.format(freq))
					score = score_BM25(weight=weight, n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
									   dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length()) # calculate score
					if docid in query_result:  # this document has already been scored once
						query_result[docid] += score
					else:
						query_result[docid] = score
					print('\t docID: {0} Freq: {1} Score:  {2}'.format(docid, freq, score))
		return query_result
