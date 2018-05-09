import sys
import codecs
import pandas as pd
import csv
import pickle
import io
import numpy as np

'''
STEPS:
1. unpickle all ptax 
2. load into woodlawn dataframes
3. check value counts greater than 2 for tax_bill_name
3.5. write to a new pickle file
4. make sure to filter out "DATA NOT CAPUTRED" and "same" for tax_bill_name in 2010-11...data

Where I'm At: running into blanks for 2011/early data, need to fig out how best to export this info
currently having issues with to_excel because i can't install openpyxl
'''

woodlawn_zip = "60637"
year_list = ['2016','2015','2014','2013','2012','2011','2010']

def find():
	for year in year_list:
		print("STARTING YEAR:", year)
		get_top_taxpayers(year)

def get_top_taxpayers(year):
	'''
	Prints out top taxpayers but also checks to see if Lake Park Associates 
	is in the data at all.
	Input: year in string form i.e. '2015'
	Returns: a printed version of the buyer and the 
	counts their name has appeared
	'''
	filepath = 'ptax_' + year + '.pickle'
	#print(filepath)
	df = pd.read_pickle(filepath)
	woodlawn_df = create_woodlawn_df(df)
	print("number of transactions:", woodlawn_df.shape[0])
	woodlawn_df[~woodlawn_df['tax_bill_name'].str.contains('DATA NOT CAPUTRED|same')]
	#print("shape after", woodlawn_df.shape)
	counts = woodlawn_df.tax_bill_name.value_counts()
	#print("counts shape", counts.shape)
	counts.sort_values(ascending=False)
	top = counts[:20]
	print("data for year:", year, "\n", top)
	if woodlawn_df['buyer_name'].str.contains('lake park').any():
		print("buyer name contains Lake Park")
		index = woodlawn_df.loc[woodlawn_df['buyer_name'].str.contains('lake park')].index
		for n in np.nditer(index):
			print(woodlawn_df.loc[[int(n)],['buyer_name','street_address']])
	if woodlawn_df['tax_bill_name'].str.contains('lake park').any():
		print("tax_bill_name name contains Lake Park")
		index = woodlawn_df.loc[woodlawn_df['tax_bill_name'].str.contains('lake park')].index
		for n in np.nditer(index):
			print(woodlawn_df.loc[[int(n)],['tax_bill_name','street_address']])
	if woodlawn_df['tax_bill_name'].str.contains('associates').any():
		print("tax_bill_name name contains associates")
		index = woodlawn_df.loc[woodlawn_df['tax_bill_name'].str.contains('associates')].index
		for n in np.nditer(index):
			print(woodlawn_df.loc[[int(n)],['tax_bill_name','street_address']])
	if (woodlawn_df['street_address'].str.contains('6500 S Woodlawn').any())| (woodlawn_df['street_address'].str.contains('6432 S Kimbark').any()):
		print("GARDENS ARE HERE in Street:")
		print(year)
	if woodlawn_df.apply(lambda row: row.astype(str).str.contains('6500 S Woodlawn').any(), axis=1).any():
		print("GARDENS ARE HERE!", year)
	if woodlawn_df.apply(lambda row: row.astype(str).str.contains('6432 S Kimbark').any(), axis=1).any():
		print("GARDENS ARE HERE TOO!", year)
	print("\n\n")

# mask = np.column_stack([woodlawn_df[col].str.contains(r"6500 S Woodlawn|6432 S Kimbark", na=False) for col in df])
# mask = np.column_stack([woodlawn_df[col].str.contains(r"GGC", na=False) for col in woodlawn_df])
# woodlawn_df.loc[mask.any(axis=1)]


### HELPER FUNCTIONS ###
def create_woodlawn_df(df):
	woodlawn_df = df[df.zipcode == woodlawn_zip]
	return woodlawn_df



