
import pandas as pd
from apyori import apriori
import numpy as np


class ARMInterestMeasures:

    def __init__(self, transactions, antecedent, consequent):
        ''' Compute necessary parameters involving antecedent, consequent from transactions '''

        self.transactions = transactions
        self.antecedent = antecedent
        self.consequent = consequent

        self.n_transactions = len(transactions) # Number of transactions in the database

        self.n_antecedent_present_trans = 0 # Number of transactions that contain antecedent
        self.n_consequent_present_trans = 0 # Number of transactions thar contain consequent
        self.n_consequent_absent_trans = 0 # Number of transactions that oppose the consequent
        self.n_support_trans = 0 # Number of transactions that support rule (A ^ B)
        self.n_oppose_trans = 0 # Number of transactions that oppose the rule (A ^ !B)

        for transaction in transactions:

            antecedent_present = self.antecedent.issubset(transaction) # Check if antecedent is subset of transaction
            consequent_present = self.consequent.issubset(transaction) # Check if consequent is subset of transaction


            if antecedent_present:
                self.n_antecedent_present_trans += 1

            if consequent_present:
                self.n_consequent_present_trans += 1
            else:
                self.n_consequent_absent_trans += 1

            if antecedent_present and consequent_present:
                self.n_support_trans += 1

            if antecedent_present and not consequent_present:
                self.n_oppose_trans += 1


    def computeSupport(self):
        ''' Compute the Support of an association rule A -> B

        Formula: n{A U B}/n
        Range: [0, 1]
        Intreprtation: Measure of popularity of the itemset, as measured by the proportion of transactions in which the
        itemset {AUB} appears.
        '''

        return self.n_support_trans/self.n_transactions

    def computeConfidence(self):
        ''' Compute the confidence of an association rule A->B

        Formula: n{A U B}/n{A}
        Range: [0, 1]
        Intrepretation: How likey B is purchased, when A is purchased, as measured by the proportion of transactions with
        items A in which items B also appears.
        '''

        return self.n_support_trans/self.n_antecedent_present_trans

    def computeLift(self):
        ''' Compute the lift (or interest) of an association rule A->B

        Formula: support{A U B}/(support{A}.support{B})
        Intrepretation: How likely item B is purchased, when item A is purchased, while controlling for how popular B
        already is.

            Lift = 1 => No Association b/w items
            Lift > 1 => Item B is likely to be brought when item A is brought
            Lift < 1 => Item B is unlikely to be brought when item A is brought

        Drawbacks:
            - Rules that hold 100% of time, may not have highest possible lift.
            - Lift is symmetric, i.e., Lift(A->B) = Lift(B->A)
        '''

        return (self.n_support_trans/self.n_transactions)/((self.n_antecedent_present_trans/self.n_transactions)*(self.n_consequent_present_trans/self.n_transactions))

    def computeConviction(self):
        ''' Compute the conviction of the rule A->B or !(A & !B)

        Formula: ( support(A) . support(!B) )/support(A and !B)
        Range: [0, inf)
        Intrepretation: Measure of Implication
        '''
        div = (self.n_oppose_trans/self.n_transactions)

        if div == 0:
          result = 0
        else:
          result = ((self.n_antecedent_present_trans/self.n_transactions)*(self.n_consequent_absent_trans/self.n_transactions))/ div
        return result

    def computeLeverage(self):
        ''' Compute the leverage (or Piatetsky-Shapiro) of the rule A->B

        Formula: Support(A,B) - Support(A).Support(B)
        Intrepretation: Is the 'proportion of additional elements' covered by both the premise and consequence 'above the
        expected' if indepedent.
        '''

        return (self.n_support_trans/self.n_transactions) - (self.n_antecedent_present_trans/self.n_transactions)*(self.n_consequent_present_trans/self.n_transactions)

    def computeCoverage(self):
        ''' Compute the coverage of the rule  A->B

        Formula: support(A)
        Range: [0, 1]
        '''

        return self.n_antecedent_present_trans/self.n_transactions




#assign values and file name as desired
f=open('B/7.txt','w+')

#replace with data_1 or data_2 as desired
data_check=pd.read_csv('data_1.csv')

#modify as required
support=2/len(data_check.index)
confidence=0.5
lift=400

#converts dataframe to list of lists to get transactions
size=len(data_check.index)
transactions=[]
for i in range(size):
    list=[]
    for col in data_check.columns:
        if ~(data_check.isnull().loc[i,col]):
            list.append(str(data_check.loc[i,col]))

    transactions.append(list)
print(len(transactions))

_association_rules = apriori(transactions, min_support=support, min_confidence=confidence, min_lift=lift, min_length=2)

association_rules = []


ng=0
ns=0
gs=0
length=[0]*3

for association_rule in _association_rules:

    pair = association_rule[0]
    items = [x for x in pair]

    length[len(items)-1]=length[len(items)-1]+1

    if(len(items)>1):
        if((items[0][0]=='N' and items[1][0]=='G')or (items[1][0]=='N' and items[0][0]=='G')):
            ng=ng+1
        if((items[0][0]=='N' and items[1][0]=='S')or (items[1][0]=='N' and items[0][0]=='S')):
            ns=ns+1
        if((items[0][0]=='G' and items[1][0]=='S')or (items[1][0]=='G' and items[0][0]=='S')):
            gs=gs+1



    itemset = set([item for item in association_rule[0]])
    support = association_rule[1]

    precedent = set([item for item in association_rule[2][0][0]])
    antecedent = set([item for item in association_rule[2][0][1]])

    confidence = association_rule[2][0][2]
    lift = association_rule[2][0][3]

    association_rules.append((precedent, antecedent))

    print("{} => {}".format(precedent, antecedent))
    print("Support = {}, Confidence = {}, Lift = {}".format(support, confidence, lift), end='\n\n')


count=1
total=0
for precedent, antecedent in association_rules:

    print("{} => {}".format(precedent, antecedent))

    arm_interest_measures = ARMInterestMeasures(transactions, precedent, antecedent)
    print("Support = {}".format(arm_interest_measures.computeSupport()))
    print("Confidence = {}".format(arm_interest_measures.computeConfidence()))
    print("Lift = {}".format(arm_interest_measures.computeLift()))
    print("Conviction = {}".format(arm_interest_measures.computeConviction()))
    print("Leverage = {}".format(arm_interest_measures.computeLeverage()))
    print("Coverage = {}".format(arm_interest_measures.computeCoverage()))

    f.write('\nRule : '+str(count)+"\n")
    f.write(str(precedent)+" => "+str(antecedent))
    f.write("\n\nSupport: " + str(arm_interest_measures.computeSupport()))
    f.write("\nConfidence: " + str(arm_interest_measures.computeConfidence()))
    f.write("\nLift: " + str(arm_interest_measures.computeLift()))
    f.write("\nConviction: " + str(arm_interest_measures.computeConviction()))
    f.write("\nLeverage: " + str(arm_interest_measures.computeLeverage()))
    f.write("\nCoverage: " + str(arm_interest_measures.computeCoverage()))
    f.write("\n=====================================\n")
    count=count+1
    total=total+1
    
    print()

print("Total items:"+str(total))
print("1. Items of size 1:"+str(length[0]))
print("2. Items of size 2:"+str(length[1]))
print('\ti)Symbol and National Common Name: '+str(ns))
print('\tii)National Common Name and Genus : '+str(ng))
print('\tiii)Symbol and Genus : '+str(gs))
print("Items of size 3:"+str(length[2]))
