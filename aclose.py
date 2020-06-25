from itertools import combinations
import pandas as pd

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


def generateClosures(transactions, generators):
        """ Generate the closures of the generators
        transactions : list of sets
                The list of transactions
        generators : lists of lists
                The list of generator itemsets whose closures need to be computed
        Returns
        -------
        list of sets
                The list of closures mapped from the generators
        """

        # The indices of transactions where generators occur
        generators_trans_indices = [[] for _ in range(len(generators))]

        for trans_index, transaction in enumerate(transactions):
                for generator_index, generator in enumerate(generators):
                        if all(_item in transaction for _item in generator):
                                generators_trans_indices[generator_index].append(trans_index)

        generators_closures = []
        for generator_trans_indices in generators_trans_indices:

                if generator_trans_indices:
                        closure = transactions[generator_trans_indices[0]].copy()

                else:
                        closure = set()

                for trans_index in generator_trans_indices[1:]:
                        closure.intersection_update(transactions[trans_index])
                generators_closures.append(closure)

        return generators_closures


def AClose(transactions, min_support, return_support_counts=False):
        """ Extract the closed frequent itemsets from the transactions
        Returns the closed closed frequent itemsets mined from the transactions that have a support greater than the minimum
        threshold. There is one optional output in addition to the closed frequent itemsets: The support counts of the
        closed frequent itemsets mined.
        Parameters
        ----------
        transactions : list of sets
                The list of transactions
        min_support : int
                The minimum support threshold
        return_support_counts : bool, optional
                If true, also return the support count of each itemset
        Returns
        -------
        closed_frequent_itemsets : list of sets
                closed frequent itemsets mined from the transactions that have support greater than the minimum threshold
        support_counts : list of integers, optional
                The support count of the closed frequent itemsets mined. Only provided if `return_support_counts` is True.
        """

        items = set()
        for transaction in transactions:
                items.update(transaction)
        items = sorted(list(items))

        # The list of all generator from whose closure we can derive all CFIs
        generators = []

        level_k = 1

        prev_level_freq_itemsets_cnts = [] # Level 0: Frequent Itemsets and its support counts
        candidate_frequent_itemsets = [[item] for item in items] # Level 1: Candidate Itemsets

        while candidate_frequent_itemsets:

                print("LEVEL {}:".format(level_k))

                # Count the support of all candidate frequent itemsets
                candidate_freq_itemsets_cnts = [0]*len(candidate_frequent_itemsets)

                for transaction in transactions:
                        for i, itemset in enumerate(candidate_frequent_itemsets):
                                if all(_item in transaction for _item in itemset):
                                        candidate_freq_itemsets_cnts[i] += 1

                print("C{}: ".format(level_k), end='')
                for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_cnts):
                        print("{} -> {}".format(itemset, support), end=', ')
                print()

                # Generate the frequent itemsets of level k by pruning infrequent itemsets
                level_frequent_itemsets_cnts = [(itemset,support) for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_cnts) if support >= min_support]

                print("L{}: ".format(level_k), end='')
                for itemset, support in level_frequent_itemsets_cnts:
                        print("{} -> {}".format(itemset, support), end=', ')
                print()

                # Prune the frequent itemsets of level k which have same support as some frequent subset in level k-1
                print("Itemsets Pruned from L{}: ".format(level_k), end='')
                for level_freq_itemset, level_freq_itemset_sup in level_frequent_itemsets_cnts.copy():
                        for prev_level_freq_itemset, prev_level_freq_itemset_sup in prev_level_freq_itemsets_cnts:

                                # If the previous level itemset is a subset of current level itemset and both have same support
                                if all(_item in level_freq_itemset for _item in prev_level_freq_itemset) and prev_level_freq_itemset_sup == level_freq_itemset_sup:
                                        print(level_freq_itemset, end=', ')
                                        level_frequent_itemsets_cnts.remove((level_freq_itemset, level_freq_itemset_sup))
                                        break
                print()

                print("L{} After Pruning: ".format(level_k), end='')
                for itemset, support in level_frequent_itemsets_cnts:
                        print("{} -> {}".format(itemset, support), end=', ')
                print()

                # Generate candidate sets of level k+1 using frequent itemsets of level k
                level_frequent_itemsets = [itemset for itemset,support in level_frequent_itemsets_cnts]
                candidate_frequent_itemsets = generateCandidateItemsets(level_k, level_frequent_itemsets)
                generators.extend(level_frequent_itemsets)

                level_k += 1

                prev_level_freq_itemsets_cnts = level_frequent_itemsets_cnts
                print()

        # Generate the closure of the generators
        generators_closures = generateClosures(transactions, generators)

        closed_frequent_itemsets = []

        # Remove the duplicates from the list of closures
        for generator_closure in generators_closures:
                if generator_closure not in closed_frequent_itemsets:
                        closed_frequent_itemsets.append(generator_closure)

        if return_support_counts == True:
            # Generate count of cfi's
            closed_frequent_itemsets_cnts = [0]*len(closed_frequent_itemsets)
            for transaction in transactions:
                    for i, itemset in enumerate(closed_frequent_itemsets):
                            if all(_item in transaction for _item in itemset):
                                closed_frequent_itemsets_cnts[i] += 1
            return closed_frequent_itemsets, closed_frequent_itemsets_cnts
        else:
            return closed_frequent_itemsets





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

#replace with data_1 or data_2 as desired
df=data_1
for row in range(df.shape[0]):
  dict_ = set()
  for col in range(df.shape[1]):
      if ~(df.isnull().iloc[row][col]):
          x = df.iloc[row][col]
          dict_.add(x)
  transaction.append(dict_)
#change support as required
support=20

CFIs, CFI_cnts = AClose(transaction, support, return_support_counts=True)

f=open('ARM/AClose/Asteraceae/4.txt','w+')
count=1

print("Closed Frequent Itemsets (CFIs)")
print("-------------------------------")

for itemset, cnt in zip(CFIs, CFI_cnts):
    f.write("\n\nItemset: "+str(count)+"\n")
    for i in itemset:
        f.write(str(i)+" ")
    count=count+1
    f.write("\nSupport: "+str(cnt))

    print("Itemset: {} Support count: {}".format(itemset, cnt))
