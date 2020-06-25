from itertools import combinations
import pandas as pd

def generateMFCS(MFCS, infrequent_itemsets):
	""" Generate the updated MFCS by modifing itemsets that have infrequent itemsets as its subset
	Parameters
	----------
	MFCS : list of lists
		The list of Maximal Frequent Candidate Sets
	infrequent_itemsets : list of lists
		The list of infrequent itemsets
	Returns
	-------
	lists of lists
		Updated MFCS
	"""

	MFCS = MFCS.copy()

	for infrequent_itemset in infrequent_itemsets:

		for MFCS_itemset in MFCS.copy():

			# If infrequent itemset is a subset of MFCS itemset
			if all(_item in MFCS_itemset for _item in infrequent_itemset):
				MFCS.remove(MFCS_itemset)

				for item in infrequent_itemset:
					updated_MFCS_itemset = MFCS_itemset.copy()
					updated_MFCS_itemset.remove(item)

					if not any(all(_item in _MFCS_itemset for _item in updated_MFCS_itemset) for _MFCS_itemset in MFCS):
						MFCS.append(updated_MFCS_itemset)

	return MFCS


def pruneCandidatesUsingMFS(candidate_itemsets, MFS):
	""" Prune the candidate itemsets that are subsets of MFS itemsets
	Parameters
	----------
	candidate_itemsets : lists of lists
		The list of candidate itemsets
	MFS : lists of lists
		The list of Maximal Frequent Itemsets
	Returns
	-------
	lists of lists
		The list of candidate itemsets with are not subsets of any itemset in MFS
	"""

	candidate_itemsets = candidate_itemsets.copy()

	for itemset in candidate_itemsets.copy():
		if any(all(_item in _MFS_itemset for _item in itemset) for _MFS_itemset in MFS):
			candidate_itemsets.remove(itemset)

	return candidate_itemsets


def generateCandidateItemsets(level_k, level_frequent_itemsets):
	""" Generate and prune the candidate itemsets for next level using the frequent itemsets of the current level

	Parameters
	----------
	level_k : int
		The current level number
	level_frequent_itemsets : list of lists
		The list of frequent itemsets of current level
	Returns
	-------
	list of lists
		The candidate itemsets of the next level
	"""

	n_frequent_itemsets = len(level_frequent_itemsets)

	candidate_frequent_itemsets = []

	for i in range(n_frequent_itemsets):
		j = i+1
		while (j<n_frequent_itemsets) and (level_frequent_itemsets[i][:level_k-1] == level_frequent_itemsets[j][:level_k-1]):

			candidate_itemset = level_frequent_itemsets[i][:level_k-1] + [level_frequent_itemsets[i][level_k-1]] + [level_frequent_itemsets[j][level_k-1]]
			candidate_itemset_pass = False

			if level_k == 1:
				candidate_itemset_pass = True

			elif (level_k == 2) and (candidate_itemset[-2:] in level_frequent_itemsets):
				candidate_itemset_pass = True

			elif all((list(_)+candidate_itemset[-2:]) in level_frequent_itemsets for _ in combinations(candidate_itemset[:-2], level_k-2)):
				candidate_itemset_pass = True

			if candidate_itemset_pass:
				candidate_frequent_itemsets.append(candidate_itemset)

			j += 1

	return candidate_frequent_itemsets


def pruneCandidatesUsingMFCS(candidate_itemsets, MFCS):
	""" Prune the candidate itemsets that are not subsets of any itemsets in current MFCS
	Parameters
	----------
	candidate_itemsets : lists of lists
		The list of candidate itemsets
	MFCS : lists of lists
		The list of Maximal Frequent Candidate Itemsets
	Returns
	-------
	lists of lists
		The list of candidate itemsets that are subsets of some itemsets in current MFCS
	"""

	candidate_itemsets = candidate_itemsets.copy()

	for itemset in candidate_itemsets.copy():
		if not any(all(_item in _MFCS_itemset for _item in itemset) for _MFCS_itemset in MFCS):
			candidate_itemsets.remove(itemset)

	return candidate_itemsets


def pincerSearch(transactions, min_support):
	""" Extract the Maximal Frequent Itemsets (MFI) from the transactions

	Parameters
	----------
	transactions : a list of sets
		The list of transactions
	min_support : int
		The minimum support for an itemset to be considered frequent
	Returns
	-------
	list of lists
		The list of MFS which contains all maximal frequent itemsets
	"""

	# Extract the list of items in the transactions
	items = set()
	for transaction in transactions:
		items.update(transaction)
	items = sorted(list(items))

	level_k = 1 # The current level number

	level_frequent_itemsets = [] # Level 0: Frequent itemsets
	candidate_frequent_itemsets = [[item] for item in items] # Level 1: Candidate itemsets
	level_infrequent_itemsets = [] # Level 0: Infrequent itemsets

	MFCS = [items.copy()] # Maximal Frequent Candidate Sets
	MFS = [] # Maximal Frequent Sets

	#print("MFCS = {}".format(MFCS))
	#print("MFS = {}\n".format(MFS))

	while candidate_frequent_itemsets:

		#print("LEVEL {}: ".format(level_k))
		#print("C{} = {}".format(level_k, candidate_frequent_itemsets))

		candidate_freq_itemsets_cnts = [0]*len(candidate_frequent_itemsets)
		MFCS_itemsets_cnts = [0]*len(MFCS)

		# Step 1: Read the database and count supports for Ck and MFCS
		for transaction in transactions:

			for i, itemset in enumerate(candidate_frequent_itemsets):
				if all(_item in transaction for _item in itemset):
					candidate_freq_itemsets_cnts[i] += 1

			for i, itemset in enumerate(MFCS):
				if all(_item in transaction for _item in itemset):
					MFCS_itemsets_cnts[i] += 1

		#for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_cnts):
			#print("{} -> {}".format(itemset, support), end=', ')
		#print()

		#for itemset, support in zip(MFCS, MFCS_itemsets_cnts):
			#print("{} -> {}".format(itemset, support), end=', ')
		#print()

		# Step 2: MFS := MFS U {frequent itemsets in MFCS}
		MFS.extend([itemset for itemset, support in zip(MFCS, MFCS_itemsets_cnts) if ((support >= min_support) and (itemset not in MFS))])
		#print("MFS = {}".format(MFS))

		# Step 3: Sk := {infrequent itemsets in Ck}
		level_frequent_itemsets = [itemset for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_cnts) if support >= min_support]
		level_infrequent_itemsets = [itemset for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_cnts) if support < min_support]

		#print("L{} = {}".format(level_k, level_frequent_itemsets))
		#print("S{} = {}".format(level_k, level_infrequent_itemsets))

		# Step 4: call MFCS-gen algorithm if Sk != NULL
		MFCS = generateMFCS(MFCS, level_infrequent_itemsets)
		#print("MFCS = {}".format(MFCS))

		# Step 5: call MFS-pruning procedure
		level_frequent_itemsets = pruneCandidatesUsingMFS(level_frequent_itemsets, MFS)
		print("After Pruning: L{} = {}\n".format(level_k, level_frequent_itemsets))

		# Step 6: Generate candidates Ck+1 from Ck (using generate and prune)
		candidate_frequent_itemsets = generateCandidateItemsets(level_k, level_frequent_itemsets)

		# Step 7: If any frequents itemsets in Ck is removed in MFS-pruning procedure
		# Call the recovery procedure to recover candidates to Ck+1

		# Step 8: call MFCS-prune procedure to prune candidates in Ck+1
		candidate_frequent_itemsets = pruneCandidatesUsingMFCS(candidate_frequent_itemsets, MFCS)

		# Step 9: k := k+1
		level_k += 1

	return MFS




data=pd.read_csv("stateDownload")
#print(data)
#Add Genus column
data['Genus']=data['Scientific Name with Author'].str.split().str.get(0)

#remove the duplicate row
indexes=data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'].index
data.loc[indexes[0],'Synonym Symbol']=data.loc[indexes[1],'Synonym Symbol']
#print(data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'])
data=data.drop(indexes[1])
#print(data.loc[data['Scientific Name with Author']=='Sarracenia purpurea L. ssp. purpurea var. purpurea'])

#remove 2 columns
data = data.reset_index(drop=True)
del data['Scientific Name with Author']
del data['Synonym Symbol']

#Get the rows of first family
data_1=data[data['Family']=='Asteraceae']
del data_1['Family']
data_1 = data_1.reset_index(drop=True)

#append column heading to beginning of each value
data_1['Symbol']='Symbol_'+data_1['Symbol'].astype('str')
data_1['National Common Name'] = data_1['National Common Name'].str.replace(' ', '_')
data_1['National Common Name'] = data_1['National Common Name'].str.replace(' ', '_')
#Since this column had null values, add extra step
for i in range(len(data_1.index)):
    if ~(data_1.isnull().loc[i,'National Common Name']):
        data_1.loc[i,'National Common Name'] = 'NCN_'+data_1.loc[i,'National Common Name']
#Since this column had null values, add extra step
data_1['Genus']='Genus_'+data_1['Genus'].astype('str')

data_2=data[data['Family']=='Poaceae']
del data_2['Family']
data_2 = data_2.reset_index(drop=True)

#append column heading to beginning of each value
data_2['Symbol']='Symbol_'+data_2['Symbol'].astype('str')
data_2['National Common Name'] = data_2['National Common Name'].str.replace(' ', '_')
for i in range(len(data_2.index)):
    if ~(data_2.isnull().loc[i,'National Common Name']):
        data_2.loc[i,'National Common Name'] = 'NCN_'+data_2.loc[i,'National Common Name']
data_2['Genus']='Genus_'+data_2['Genus'].astype('str')

transaction = []
#change dataset as required
df=data_2
for row in range(df.shape[0]):
  dict_ = set()
  for col in range(df.shape[1]):
      if ~(df.isnull().iloc[row][col]):
          x = df.iloc[row][col]
          dict_.add(x)
  transaction.append(dict_)

#change support as required
min_support_count = 20

MFS = pincerSearch(transaction, min_support_count)

#print("MFS = {}".format(MFS))
