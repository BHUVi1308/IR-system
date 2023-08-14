from util import *

# Add your import statements here




class Evaluation():
	def true_doc_id_list(self, query_id, qrels):
		true_doc_ids = []
		for i in qrels:
			if int(i['query_num']) == query_id:
				true_doc_ids.append(int(i['id']))
		return true_doc_ids
		

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		intersection_size = len(list(set(query_doc_IDs_ordered[:k]).intersection(true_doc_IDs)))
		precision = intersection_size / k

		#Fill in code here

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		count = 0
		for i in range(len(query_ids)):
			count += self.queryPrecision(doc_IDs_ordered[i], query_ids[i], self.true_doc_id_list(query_ids[i],qrels), k)

		meanPrecision = count/len(query_ids)

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		intersection_size = len(list(set(query_doc_IDs_ordered[:k]).intersection(true_doc_IDs)))
		recall = intersection_size/(len(true_doc_IDs))

		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		count = 0 
		for i in range(len(query_ids)):
			count += self.queryRecall(doc_IDs_ordered[i], query_ids[i], self.true_doc_id_list(query_ids[i],qrels), k)

		meanRecall = count/len(query_ids)

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		p = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		r = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)

		if p==0 and r == 0:
			fscore = 0
		else:
			fscore = (2*p*r)/(p+r)

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		count = 0 
		for i in range(len(query_ids)):
			count += self.queryFscore(doc_IDs_ordered[i], query_ids[i], self.true_doc_id_list(query_ids[i],qrels), k)

		meanFscore = count/len(query_ids)

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here

		rel = np.zeros((len(query_doc_IDs_ordered), 1))
		true_doc_IDs["position"] = 5-true_doc_IDs["position"] # doubt here 4- or directly


		true_doc_ids_sorted = true_doc_IDs.sort_values("position", ascending = False)
		iDCG = true_doc_ids_sorted.iloc[0]["position"]

		for i in range(1, min(k,len(true_doc_IDs))):
			iDCG += (true_doc_ids_sorted.iloc[i]["position"]) * (np.log(2)/np.log(i+1))

		t_docs = list(map(int, true_doc_IDs["id"]))
		for i in range(k):
			if query_doc_IDs_ordered[i] in t_docs:
				rel[i] = true_doc_IDs[true_doc_IDs["id"] == str(query_doc_IDs_ordered[i])].iloc[0]["position"]

		for i in range(k):
			nDCG += (rel[i])* np.log(2) / np.log(i + 2)
		
		nDCG = nDCG/iDCG

		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		qrels_df = pd.DataFrame(qrels)
		count = 0 
		for i in range(len(query_ids)):
			query_doc_ids_ordered = doc_IDs_ordered[i]
			query_id = query_ids[i]
			true_doc_ids = qrels_df[["position","id"]][qrels_df["query_num"] == str(query_id)]			
			count += self.queryNDCG(query_doc_ids_ordered, query_id, true_doc_ids, k)
		meanNDCG = count/len(query_ids)

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		count=0
		p_sum=0

		for i in range(k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				count+=1
				p_sum += self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, i+1)

		if count == 0:
			avgPrecision = 0
		else:
			avgPrecision= p_sum / count
		

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		count=0
		for i in range(len(query_ids)):
			count += self.queryAveragePrecision(doc_IDs_ordered[i], query_ids[i],self.true_doc_id_list(query_ids[i],q_rels), k)
		meanAveragePrecision = count/len(query_ids)

		return meanAveragePrecision

