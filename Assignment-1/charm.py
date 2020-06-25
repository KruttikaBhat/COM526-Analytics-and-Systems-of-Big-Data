import os
import time
import argparse
from copy import copy
import pandas as pd
import numpy as np


class DataPreparation:
    transactional = []
    tid_count = 0

    def import_data(self, filename):
        with open(filename, 'r') as file:
            tid = 1
            count=0
            for line in file:

                if count>0:
                    line = list(line.strip().split(','))
                    print(line)
                    if line[2]=='':
                        del line[2]
                    line=np.array(line)[1:].tolist()
                    #print(line)
                    line=','.join(line)
                    print(line)
                    #for element in line:
                    self.transactional.append({'tid': tid, 'item': line})
                    tid += 1
                count=count+1
        self.tid_count = tid - 1

    def transform_data(self):
        df = pd.DataFrame(self.transactional)
        print(df)
        self.itemsGrouped = df.groupby(['item'])['tid'].apply(list)
        self.itemsGrouped = pd.DataFrame({'item': self.itemsGrouped.index, 'tid': self.itemsGrouped.values})
        self.itemsGrouped['item'] = self.itemsGrouped['item'].apply(lambda x: {x})

    def get_frequent_items(self, min_sup):

        return self.itemsGrouped[self.itemsGrouped['tid'].map(len) >= min_sup * self.tid_count]


class CharmAlgorithm:
    def __init__(self, min_sup_config, tid_count):
        self.result = pd.DataFrame(columns=['item', 'tid', 'support'])
        self.min_sup = min_sup_config * tid_count

    @staticmethod
    def replace_values(df, column, find, replace):
        for row in df.itertuples():
            if find <= row[column]:
                row[column].update(replace)

    def charm_property(self, row1, row2, items, new_item, new_tid):
        if len(new_tid) >= self.min_sup:
            if set(row1[2]) == set(row2[2]):
                # remove row2[1] from items
                items = items[items['item'] != row2[1]]
                # replace all row1[1] with new_item
                find = copy(row1[1])
                self.replace_values(items, 1, find, new_item)
                self.replace_values(self.items_tmp, 1, find, new_item)
            elif set(row1[2]).issubset(set(row2[2])):
                # replace all row1[1] with new_item
                find = copy(row1[1])
                self.replace_values(items, 1, find, new_item)
                self.replace_values(self.items_tmp, 1, find, new_item)
            elif set(row2[2]).issubset(set(row1[2])):
                # remove row2[1] from items
                items = items[items['item'] != row2[1]]
                # add {item, tid} to self.items_tmp
                self.items_tmp = self.items_tmp.append({'item': new_item, 'tid': new_tid}, ignore_index=True)
                # sort items by ascending support
                # s = self.items_tmp.tid.str.len().sort_values().index
                # self.items_tmp = self.items_tmp.reindex(s).reset_index(drop=True)
            elif set(row1[2]) != set(row2[2]):
                # add {item, tid} to self.items_tmp
                self.items_tmp = self.items_tmp.append({'item': new_item, 'tid': new_tid}, ignore_index=True)
                # sort items by ascending support
                # s = self.items_tmp.tid.str.len().sort_values().index
                # self.items_tmp = self.items_tmp.reindex(s).reset_index(drop=True)

    def charm_extend(self, items_grouped):
        # sort items by ascending support
        s = items_grouped.tid.str.len().sort_values().index
        items_grouped = items_grouped.reindex(s).reset_index(drop=True)

        for row1 in items_grouped.itertuples():
            self.items_tmp = pd.DataFrame(columns=['item', 'tid'])
            for row2 in items_grouped.itertuples():
                if row2[0] >= row1[0]:
                    item = set()
                    item.update(row1[1])
                    item.update(row2[1])
                    tid = list(set(row1[2]) & set(row2[2]))
                    self.charm_property(row1, row2, items_grouped, item, tid)
            if not self.items_tmp.empty:
                self.charm_extend(self.items_tmp)
            # check if item subsumed
            is_subsumption = False
            for row in self.result.itertuples():
                if row1[1].issubset(row[1]) and set(row[2]) == set(row1[2]):
                    is_subsumption = True
                    break
            # append to result if element not subsumed
            if not is_subsumption:
                self.result = self.result.append({'item': row1[1], 'tid': row1[2], 'support': len(row1[2])}, ignore_index=True)

    def write_result_to_file(self, result_file):
        self.result.to_csv(result_file, sep='\t', columns=['item', 'support'], index=False)
        type(self.result)

# Variables:


#replace data_1 with data_2
input_filname='data_1.csv'
data=pd.read_csv('data_1.csv')

#change support as required
support = 20/len(data.index)
output_filename = '4'

# Data preparation:
data = DataPreparation()
data.import_data(input_filname)

for i in data.transactional:
    print(i)


data.transform_data()

print(data.itemsGrouped)
print(data.tid_count)
freq = data.get_frequent_items(support)
print(freq)
# Algorithm:

algorithm = CharmAlgorithm(support, data.tid_count)
algorithm.charm_extend(freq)


# write to file
algorithm.write_result_to_file(output_filename)

cwd = os.getcwd()
dirname = os.path.dirname(cwd+'/'+output_filename)
if not os.path.exists(dirname):
    os.makedirs(dirname)

f=open(cwd+'/'+output_filename, "r")
contents = f.read()
print(contents)
