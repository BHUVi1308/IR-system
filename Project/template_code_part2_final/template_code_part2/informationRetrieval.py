from util import *

# Add your import statements here
import numpy as np
from textblob import TextBlob
from spellchecker import SpellChecker
from numpy.linalg import svd
import enchant
import sys
movies_dict = enchant.PyPWL("word.txt")

class InformationRetrieval():

	def __init__(self):
		self.index = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = None

		#Fill in code here
		
		n = 0
		
		doc_inverted_list = {}
		for i in range(0,len(docs)):
			for j in range(0,len(docs[i])):
				for k in range(0,len(docs[i][j])):
					if docs[i][j][k] not in doc_inverted_list:
						doc_inverted_list[docs[i][j][k]] = [docIDs[i]]
					elif docIDs[i] not in doc_inverted_list[docs[i][j][k]] :
						doc_inverted_list[docs[i][j][k]].append(docIDs[i])
		


		self.index = (doc_inverted_list,docIDs,docs)


	def rank(self, queries, K =400, w = 1.0):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""
		
		
		doc_IDs_ordered = []
		
		#Fill in code here

		spell = SpellChecker()
		
		
		doc_inverted_list,doc_no,docs = self.index
		No = len(docs)	
		Query = queries
		
		
		for i in range(0,len(Query)):
			for j in range(0,len(Query[i])):
				misspelled = spell.unknown(Query[i][j])
				for k in range(0,len(Query[i][j])):
					if Query[i][j][k] not in doc_inverted_list:
						b = TextBlob(Query[i][j][k])
						b1 = Query[i][j][k]
						Query[i][j][k] = str(b.correct())
						b = str(b.correct())
						if b == b1 and b in misspelled:
							suggestions = movies_dict.suggest(b1)
							if len(suggestions) == 0:
								Query[i][j][k] = b1
							else:
								b = suggestions[0]
								Query[i][j][k] = suggestions[0]
						if b != b1:
							print("Showing results for" + " " + Query[i][j][k])
					if Query[i][j][k] not in doc_inverted_list :
						doc_inverted_list[Query[i][j][k]] = [0]


		docvector = np.zeros((No, len(doc_inverted_list.keys())))
		key = list(doc_inverted_list.keys())

		idf = np.zeros((len(key), 1))
		for i in range(len(key)):
			idf[i] = np.log2(No/ (len(doc_inverted_list[key[i]])))


		for i in range(0,len(docs)):
			for j in range(0,len(docs[i])):
				for k in range(0,len(docs[i][j])):
					if docs[i][j][k] in doc_inverted_list:
						ind = list(doc_inverted_list.keys()).index(docs[i][j][k])
						if j == len(docs[i])-1:
							docvector[i][ind] += w
						else:
							docvector[i][ind] += 1 


		for i in range(docvector.shape[0]):
			docvector[i, :] = docvector[i, :] * idf.T	


		Queryvector = np.zeros((len(Query),len(doc_inverted_list.keys())))

		for i in range(0,len(Query)):
			for j in range(0,len(Query[i])):
				for k in range(0,len(Query[i][j])):
					if Query[i][j][k] in doc_inverted_list:
						ind = list(doc_inverted_list.keys()).index(Query[i][j][k])
						Queryvector[i][ind] += 1

		for i in range(Queryvector.shape[0]):
			Queryvector[i, :] = Queryvector[i, :] * idf.T


		U, S, V_T = svd(docvector.T, full_matrices=False)

		Uk = U[:,:K]
		Sk = np.diag(S[:K])
		Vk_T = V_T[:K]

		docvector = Vk_T.T@Sk
		Queryvector= Queryvector@Uk


		for i in range(len(Queryvector)):
			temp = []
			for j in  range(len(docvector)):
				cossim = np.dot(Queryvector[i, :], docvector[j, :])/((np.linalg.norm(Queryvector[i, :]) + 1e-4)*(np.linalg.norm(docvector[j, :]) + 1e-4))
				temp.append(cossim)
			doc_IDs_ordered .append([x for _, x in sorted(zip(temp, doc_no), reverse=True)])
   
	
		return doc_IDs_ordered




