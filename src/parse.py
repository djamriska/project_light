__author__ = 'Nick Hirakawa'

import re
from ast import literal_eval
import metapy


class CorpusParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')
		self.corpus = dict()

	def parse(self):
		with open(self.filename) as f:
			s = ''.join(f.readlines())
		blobs = s.split('#')[1:]


		for x in blobs:
			text = x.split()
			# todo: add stop word removal
			# todo: perform stemming
			# todo: add in min / max word sizes

			# print('text: {0}'.format(text))
			docid = text.pop(0)
			# print('docid: {0}'.format(docid))
			self.corpus[docid] = text

	def get_corpus(self):
		return self.corpus


class QueryParser:

	def __init__(self, filename):
		self.filename = filename
		self.queries = []

	def parse(self):
		with open(self.filename) as f:
			lines = ''.join(f.readlines())
		self.queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]

	def get_queries(self):
		return self.queries


class KeywordParser:

	def __init__(self, filename):
		self.filename = filename
		self.keywords = []

	def parse(self):
		with open(self.filename) as f:
			lines = ''.join(f.readlines())
		kw = literal_eval(lines)
		print("==keywords weights ===")

		for key, value in kw.items():
			value = round(value/100, 3)
			print(key, value)
		print('')
		self.keywords = kw

	def get_keywords(self):
		return self.keywords

class ArticleParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')
		self.articles = dict()

	def parse(self):
		with open(self.filename) as f:
			s = ''.join(f.readlines())
		blobs = s.split('##')[1:]

		for x in blobs:
			text = x.split(',')
			text = [x.strip(' ') for x in text]
			#print('text: {0}'.format(text))
			docid = text.pop(0)
			title = text.pop(0)
			source = text.pop(0)
			pub_date = text.pop(0)
			pub_url = text.pop(0)
			text_out = {'docid': docid, 'title': title, 'source': source, "pub_date": pub_date, "pub_url": pub_url}
			self.articles.append(text_out)

	def get_articles(self):
		return self.articles


if __name__ == '__main__':
	qp = QueryParser('text/queries.txt')
	print(qp.get_queries())
