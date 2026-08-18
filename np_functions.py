

import numpy as np
import data_files
import user_csv

def calc_mean_num_threatened_species_in_country(country):
    """ function: calculates the mean number of threatened species in a country
    parameters: country represents a user entered country as a string.
    returns: float number of mean threatened species in the country
     """
    # find country
    species_data = user_csv.read_csv('/usercode/data_files/Threatened_Species.csv', False) # reads file 
    species_array_w_country = np.array(species_data) # change the list from csv to an array
    country_norm = country.strip().lower()


    for lists in species_array_w_country:             # for the lists in the array
        if lists[0].strip().lower() == country_norm:        # if the country is in the right row
            species_array = lists[1:].astype(float)
            mean_threatened = np.mean(species_array) # calc avg threatened species
    return(mean_threatened)

def max_threatened_species(country):
    """ function: calculates the max number of threatened species for the
    same subregions the country is in.
    parameters: country represents the user entered country as a string
    returns: list of countries and max float number of threatened species for each subregion that the country is in, along with the subregion title and the subregion itself"""

    # find country and subregion.

    species_data = user_csv.read_csv('/usercode/data_files/Threatened_Species.csv', False)
    country_data = user_csv.read_csv('/usercode/data_files/Country_Data.csv', True)

    headers = country_data[0]
    subregion_title = headers[2]
    country_title = headers[0]

    countries = []
    species_info = []


    for lists in country_data:# find the country and identify subregion in country data.
        if lists[0].strip().lower() == country:
            subregion = lists[2]

    for lists in country_data:                  # find all countries with same subregion
        if subregion == lists[2]:
            countries += [lists[0]]

    for rows in species_data:                   # takes the numbers of threatened species for each country and turns it into one big array.
        for value in countries:
            if value in rows[0]:
                species_info += [rows[1:]]
    species_array = np.array(species_info)

    max_num = np.max(species_array, 1)

    

    top_list = [subregion_title, country_title, 'Max Endangered Species']
    final_list = [top_list] #the first list is going to be the titles 
    empty_list=[] 
    for i in range (len(countries)):   #for each country in specific subregion
        empty_list.append(subregion)   #subregion goes first in the list
        empty_list.append(countries[i]) #then the country
        empty_list.append(max_num[i]) #then the max number of endangered species
        final_list.append(empty_list) #and then we append this list to the 2D list
        empty_list = []
        


    user_csv.write_csv('/usercode/data_files/Data.csv', final_list, True)  #we save this data to a separate csv
    

    return final_list 

def min_threatened_species(country):
    """ function: calculates the min number of threatened species for the
    same subregions the country is in.
    parameters: country represents the user entered country as a string
    returns: list of countries and max float number of threatened species for each subregion that the country is in, along with the subregion title and the subregion itself"""


    # find country and subregion.
    species_data = user_csv.read_csv('/usercode/data_files/Threatened_Species.csv', False)
    country_data = user_csv.read_csv('/usercode/data_files/Country_Data.csv', True)


    headers = country_data[0]
    subregion_title = headers[2]
    country_title = headers[0]


    countries = []
    species_info = []


    for lists in country_data:# find the country and identify subregion in country data.
        if lists[0].strip().lower() == country:
            subregion = lists[2]


    for lists in country_data:                  # find all countries with same subregion
        if subregion == lists[2]:
            countries += [lists[0]]


    for rows in species_data:                   # takes the numbers of threatened species for each country and turns it into one big array.
        for value in countries:
            if value in rows[0]:
                species_info += [rows[1:]]
    species_array = np.array(species_info)


    min_num = np.min(species_array, 1)




    top_list = [subregion_title, country_title , 'Min Endangered Species']
    final_list = [top_list]  #the first list in the 2D list is going to be the titles
    empty_list=[]
    for i in range (len(countries)): #go through countries in subregion
        empty_list.append(subregion)  #first item in list is subregion
        empty_list.append(countries[i])  # second item is the country
        empty_list.append(min_num[i]) #third item is the min number of endangered species
        final_list.append(empty_list) #append this list to the 2D list
        empty_list = [] #empty and repeat


    return final_list


