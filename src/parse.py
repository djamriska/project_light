
import re
from ast import literal_eval


# read in comments for analysis
class CorpusParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')
		self.corpus = dict()

	def parse(self):
		with open(self.filename) as f:
			s = ''.join(f.readlines())
		# blobs = s.split('#')[1:]
		blobs = s.split('##')[1:]

		for x in blobs:
			text = x.split()
			# todo: add stop word removal
			# todo: perform stemming
			# todo: add in min / max word sizes

			# print('text: {0}'.format(text))
			docid = text.pop(0)
			self.corpus[docid] = text

	def get_corpus(self):
		return self.corpus

# read in the current terms we want to search for in the comments
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

# pull in keywords and their assigned weight
class KeywordParser:

	def __init__(self, filename):
		self.filename = filename
		self.keywords = []

	def parse(self):
		with open(self.filename) as f:
			lines = ''.join(f.readlines())
		kw = literal_eval(lines)
		#print("==keywords weights ===")

		for key, value in kw.items():
			value = round(value/100, 3)
			# print(key, value)
		# print('')
		self.keywords = kw

	def get_keywords(self):
		return self.keywords

# pull in keywords and their assigned type
class KeywordTypeParser:

	def __init__(self, filename):
		self.filename = filename
		self.keywords = []

	def parse(self):
		with open(self.filename) as f:
			lines = ''.join(f.readlines())
		kwt = literal_eval(lines)
		#print("==keywords types ===")

		#for key, value in kwt.items():
			#print(key, value)
		# print('')
		self.keywords_types = kwt

	def get_keywords(self):
		return self.keywords_types

# pull in source articles that are the parent to the comments
class ArticleParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')
		self.articles = {}

	def parse(self):
		with open(self.filename) as f:
			s = ''.join(f.readlines())
			blobs = s.split('##')[1:]
			work_dict = {}
			for x in blobs:
				text = x.split(',')
				text = [x.strip(' ') for x in text]
				# print('text: {0}'.format(text))
				docid = int(text.pop(0))
				title = text.pop(0)
				source = text.pop(0)
				pub_date = text.pop(0)
				pub_url = text.pop(0)
				# work_dict = {}
				work_dict[docid] = {"title": title, "source": source, "pub_date": pub_date, "pub_url": pub_url}
				self.articles = work_dict

	def get_articles(self):
		return self.articles


if __name__ == '__main__':
	qp = QueryParser('text/queries.txt')
	#print(qp.get_queries())
