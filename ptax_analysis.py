#This will download PTAX data from 2006 to 2016 for Englewood
import sys
import codecs
import pandas as pd
import csv
import pickle

#Filepath for 2016
basepath = '/Users/amy/Code/chi-city/Delivery Files/Data Files/'
endpath = 'PTAX203.txt'
#TRED2016 = '/Users/amy/Code/chi-city/Delivery Files/Data Files/2016/TRED2016PTAX203.txt'
#TRED2015 = '/Users/amy/Code/chi-city/Delivery Files/Data Files/2015/TRED2015PTAX203.txt'
englewood_zip1 = "60636"
englewood_zip2 = "60621"
woodlawn_zip = "60637"

def get_all_data(woodlawn=False):
	'''
	Creates pandas dataframe for data from 2006 to 2016 and loads into a pickle file
	If woodlawn == True, creates one 2016 df for woodlawn
	'''
	year_list = ['2016','2015','2014','2013','2012','2011','2010','2009',
	'2008','2007','2006']
	for year in year_list:
		filepath = create_filepath(year)
		df = read_df(filepath)
		rename_df_columns(df)
		print("finished renaming columns")
		#save full dataset to pickle file
		filename = 'ptax_' + year + '.pickle'
		df.to_pickle(filename)
		englewood_df = create_englewood_df(df)
		#save englewood data to pickle file
		filename = 'englewood_' + year + '.pickle'
		englewood_df.to_pickle(filename)
		print("finished pickling", filename)

def create_filepath(year):
	'''
	Creates string filepath where PTAX data is located from 2006 to 2016
	Input:
		year: (string)

	Returns:
		filepath: (string)
	'''
	filepath = basepath + year + '/TRED' + year + endpath
	return filepath

def read_df(filepath):
	'''
	Reads a .txt file to a pandas dataframe 
	Inputs:
		filepath: (string) points to the PTAX data

	Returns:
		df: (pandas df) full PTAX
	'''
	with open(filepath, 'rb') as f:
		contents = f.read()

	c = codecs.open(filepath, 'r', encoding='ascii', errors='ignore')
	df = pd.read_csv(c, header=None, dtype='object')

	return df

def rename_df_columns(df):
	'''
	Renames all the columns in PTAX dataframe and modifies dataframe in place
	'''
	df.columns = ['county', 'recording_year', 'document_number', 'recording_month', 'recording_day',
	'volume', 'page', 'tab_number', 'street_address', 'city', 'township', 'parcel_count',
	'deed_year', 'deed_month', 'deed_type', 'other_deed_type', 'principal_residence',
	'advertised', 'current_use_code', 'intended_use_code', 'current_units',
	'intended_units', 'current_comm_use_dsc', 'intended_comm_use_dsc',
	'current_other_use_dsc', 'intended_other_use_dsc', 'demolition_indicator',
	'additions_indicator', 'remodel_indicator', 'new_construction_indicator',
	'other_change_indicator', 'expl_other_change', 'change_month', 'change_year',
	'full_contract_indicator', 'yr_contract_initiated', 'sale_btwn_relatives',
	'sale_less_100', 'court_ordered_sale', 'foreclosure', 'condemnation', 'auction_sale',
	'relocation_company', 'financial_inst', 'reit', 'pension_fund', 'adjacent_property',
	'option_to_purchase', 'trade_of_property', 'sale_leaseback', 'other_items_indicator',
	'expl_other_items', 'full_consideration', 'personal_property', 'mobile_home', 
	'net_consideration', 'other_real_property', 'outstanding_mortgage', 'exempt_transfer',
	'net_consideration_tax', 'line_18', 'il_tax', 'county_tax', 'total_tax', 'seller_name',
	'seller_signature', 'buyer_name', 'buyer_signature', 'tax_bill_name', 'tax_bill_address',
	'tax_bill_city', 'tax_bill_state', 'tax_bill_zip', 'tax_bill_zip4', 'preparer_name',
	'preparer_file_num', 'preparer_address', 'preparer_city', 'preparer_zip', 'preparer_state',
	'preparer_zip','preparer_zip4',
	'ext_legal_attached', 'ptax_attached', 'personal_prop_attached', 'ccao_township',
	'property_class', 'minor_property_class', 'land_assessment', 'building_assessment',
	'total_assessment', 'year_prior', 'mobile_home_assessed', 'zipcode',
	'homestead_exemption', 'homestead_amt', 'senior_homestead_amt', 'senior_homestead_freeze_amt',
	'ptax_b', 'short_sale', 'bank_reo']

def create_englewood_df(df):
	'''
	Takes the full pandas dataframe and returns a new dataframe with just 
	Englewood properties

	Returns:
		englewood_df: (pandas dataframe)
	'''
	englewood_df = df[(df.zipcode == englewood_zip1) | (df.zipcode == englewood_zip2)]
	return englewood_df

def create_woodlawn_df(df):
	woodlawn_df = df[df.zipcode == woodlawn_zip]
	return woodlawn_df

#the whole dataframe
#df[df.foreclosure == '1'].shape

#Just Englewood

# englewood_df[englewood_df.tax_bill_state != "IL"].shape
# englewood_df[englewood_df.tax_bill_state != "IL"].tax_bill_state
# englewood_df[englewood_df.tax_bill_state != "IL"].tax_bill_name
# englewood_df[englewood_df.tax_bill_state != "IL"].tax_bill_city
# englewood_df[englewood_df.tax_bill_name == "NATIONSTAR MORTGAGE LLC"]
# englewood_df['buyer_name']


# woodlawn_df['buyer_name'].astype('|S') 
# woodlawn_df[woodlawn_df['buyer_name'].str.contains('GGC VENTURES LLC')]


# englewood_df_2006 = pd.read_pickle('englewood_2006.pickle')

def main():
	'''
	Main function - TBD
	'''
	# df = read_df(TRED2016PTAX203)
	# rename_df_columns(df)
	# englewood_df = create_englewood_df(df)


if __name__ == "__main__":
    sys.exit(main())
