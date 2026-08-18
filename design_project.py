# design_project.py
# ENDG 233 F24
# STUDENT NAME(S) Laura Best(30294071) and Maya Wadhera(30283628)
# GROUP NAME: block 4 group # 11
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.




#design_project.py\

#-----------------------------

import data_files

import user_csv

import numpy as np

import matplotlib.pyplot as plt

import np_functions


def country_choice_menu():  

  '''Function: displays a menu asking user to pick a country or select '0' to quit
  returns the chosen country normalized(ei 'South Korea' turns into 'southkorea') or '0' '''

  countries = user_csv.read_csv('/usercode/data_files/Country_Data.csv', False) 
  country_names = []
  for row in countries:  #create a list of all valid country names
    country_names.append(row[0].strip().lower()) #normalizes the country namees

  while True:

    choice = input('Pick a country or select 0 to quit: \n')
    choice = choice.strip().lower() #normalize user input
    if choice == '0':
      print('Thank you and goodbye!')
      return choice #they quit the program 

        
    elif choice in country_names:  #if the country is a valid option return the country
      return choice

    else:  #if the input is not valid, ask again until they pick a valid choice
      print('please try again')
              

def data_choice_menu():  

  '''Function: displays a menu of the options the user has to choose from for manipulatiing the data. Continues to ask user for input until
  valid input is given, and then it returns that input'''

  valid_options = ['1', '2', '3', '4', '5', '0']

  while True:
    choice = input('Select an Option:\n\t1) Population Percent Change\n\t2) Threatened Species per 1000 KM\n\t3) Threatened Species Per Million People\n\t4) Average # of Threatened Species Type\n\t5) Max & Min # of Threatened Species Type\n\t0) Return to Main Menu\n')
    choice = choice.strip()
    if choice in valid_options:  #if choice = 1,2,3,4,5 or 0
      return choice #return number choice

    else:
      print('Please Try Again')
      continue  #if not ask again until they pick valid choice


def year_choice_menu(): 

  '''Function: displays the prompt asking the user to pick a year and continues to ask for a valid year input until one is given. 
  Then it returns that year as an integer'''

  while True:
    year = (input('Choose a Year Between 2000 and 2020: \n'))
    year = user_csv.is_float(year)  #check that the user entered a number and not a word
    if type(year) == float and year >=2000 and year <= 2020:  #if the year is a number between 2000 and 2020
      return int(year) #return the year as integer
    else:
      print('Please Try Again') #try again until valid input is given
      continue


def calc_pop_change(country): 

  '''Function: takes the chosen country and returns the percent change difference in population from 2000 to 2020
  Parameters: valid country name'''

  pop_data = user_csv.read_csv('/usercode/data_files/Population_Data.csv', False)
  pop_values = []
    

  for row in range(len(pop_data)): #iterate through rows of population data
    if pop_data[row][0].strip().lower() == country: #if the first value of the row is the country
        pop_values.append(pop_data[row][1]) #append the second column to population data variable
        pop_values.append(pop_data[row][-1])      #pop_values = [2020 pop, 2000 pop]  #append last column

  pop_change_percent = ((pop_values[0] - pop_values[1]) / pop_values[1]) * 100

  return pop_change_percent

def print_pop_change(value): 
  '''Function: takes the previously calculated population change percent and prints a statement'''
  if value > 0 :
    print(f'The population grew by {value:.2f}% between the years 2000 and 2020.')
  else:
    print(f'The population shrunk by {value*(-1):.2f}')
    


def calc_threatened_species_per_1000sqkm(country): 

  '''Function: takes a country and returns the number of threatened species for 1000 square km'''

  species_data = user_csv.read_csv('/usercode/data_files/Threatened_Species.csv', False)
  country_data = user_csv.read_csv('/usercode/data_files/Country_Data.csv', False)
  total_threatened = 0


  for row in species_data:   #iterate through species data to find row for certain country 
    if row[0].strip().lower() == country:

      for value in row[1:]: #add each value except for first to total threatened
        total_threatened += value

  for row in country_data:
    if row[0].strip().lower() == country: #for the row for the certain country
      sq_km = row[-1] #the km squared is the last column
    
  species_per_1000_sqkm = (total_threatened / sq_km) * 1000
  
  return species_per_1000_sqkm

def print_threatened_species(value): 

  '''Function : Takes the previously calculated amount of threatened species per 1000 square kilometers in selected country and prints a statement
  Parameters: value = # of threatened species per 1000 square kilometers'''

  print(f'There is roughly {value:.4f} threatened species for every 1000 square km')

def calc_threatened_species_per_mil(country, year): 

  '''Function : this function goes through the threatened_species.csv and finds the amount of threatened species in selected country. Then it finds the population
  of the selected country for the selected year in the population_data.csv. 
  Parameters: this function takes the country and year (b/t 2000 and 2020) and returns the amount of threatened species for each million people as float. '''

  species_data = user_csv.read_csv('/usercode/data_files/Threatened_Species.csv', False)
  pop_data = user_csv.read_csv('/usercode/data_files/Population_Data.csv', True)
  total_threatened = 0 

  for row in species_data: #iterate through each row in the species_data
    if row[0].strip().lower() == country:  #and when it finds the row for selected country
      for value in row[1:]:
        total_threatened += float(value) #it will add each column containing an amount of threatened species to the total threatened variable

  header = pop_data[0] #the header contains the years that population data was gathered, we only need to find which index the selected year is in

  for lists in range(len(pop_data)): #iterate through the population data
    if pop_data[lists][0].strip().lower() == country:  #find the row that has the selected country
        for column in range(len(pop_data[lists])):  #go through each item in that row
            if header[column] == f'{year} Pop':  #if the header for that row is for selected year
              pop = float(pop_data[lists][column]) #the population is the row index of selected country and column index of the selected year


  species_per_mil = (total_threatened / pop) * 1000000 

  return species_per_mil


def print_species_per_mil(value): 

  '''Function: takes the previously calculated value of threatened species for each million people in selected country and returns a statement
  Parameters: value = # of threatened species for each million people in selected country '''

  print(f'There is roughly {value:.1f} threatened species per million people.')

def print_max_threatened_species(value):

  '''Function: prints the maximum number of the type of threatened species in a country in a nice table
  Takes the 2D list created by the max_threatened_species function and returns nothing'''
  sub_region = value[1][0] # sets table headers for the subregion, and country
  sub_region_title = value[0][0]
  country = value[0][1]


  header = f'{sub_region_title:<30}' # creates a header for the table with 30 units of space afterwards
  print(header) 
  sub_header = f'{sub_region:<30}{country:<30}Max Threatened Species' # creates a subheader with the subregion and country
  print(sub_header)
  for i in range(len(value)-1):         # for the length of the list -1 
    print(f'{"":<30}{value[i+1][1]:<30}{value[i+1][2]:<30}') # create a tab, print the value of the country, print the value of the max threatened species
  # the table columns are separated by 30 units of space

def print_min_threatened_species(value):
  '''Function: prints the minimum number of the type of threatened species in a country in a nice table
  Takes the 2D list created by the min_threatened_species function and returns nothing'''
  sub_region = value[1][0] # sets headers for the table based on values from the input
  sub_region_title = value[0][0]
  country = value[0][1]


  header = f'{sub_region_title:<30}' # creates a header for the table with 30 units of space afterwards
  print(header)
  sub_header = f'{sub_region:<30}{country:<30}Min Threatened Species' # creates a subheader with the subregion and country
  print(sub_header)
  for i in range(len(value)-1):        # for the length of the list -1
    print(f'{"":<30}{value[i+1][1]:<30}{value[i+1][2]:<30}') # create a tab, print the value of the country, print the value of the min threatened species
  # the table columns are separated by 30 units of space


   
while True:  # runs the main program


  country = country_choice_menu() # runs the country choice menu function


  if country == '0': # if the function returns 0, end the program.
    break


  choice = data_choice_menu() # run data choice menu function


  if choice == '0':                             # if the choice is 0 run the program again
    continue


  elif choice == '1':                           # if the choice is 1
    pop_change = calc_pop_change(country)       # calculate the population change of a country
    print_pop_change(pop_change)                # print the change in population message




  elif choice == '2':                           # if the choice is 2
    threatened_species = calc_threatened_species_per_1000sqkm(country) # calculate the number of threatened species per 1000sqkm for a country
    print_threatened_species(threatened_species) # print the threatened species message


  elif choice == '3':                           # if the choice is 3
    year = year_choice_menu()                   # run the year choice function
    species_per_mil = calc_threatened_species_per_mil(country, year) # calculate the threatened species per million for a country and year
    print_species_per_mil(species_per_mil) # print the species per million message


  elif choice == '4':                           # if the choice is 4
    mean_num_threatened_species = np_functions.calc_mean_num_threatened_species_in_country(country) # calling the mean num threatened species function from np_function for a country
    print(f'The average number of threatened species in {country} is {mean_num_threatened_species:.2f}.') # printing the mean num of threatened species in a country message to 2 decimals


  elif choice == '5': # if the choice is 5
    max_threatened_species = np_functions.max_threatened_species(country) # calling the max threatened species function from np_functions for a country
    print_max_threatened_species(max_threatened_species) # print the max threatened species table
    print('-'*50)                               # print a line of dashes
    min_threatened_species = np_functions.min_threatened_species(country) # calling the min threatened species function from np_functions for a country.
    print_min_threatened_species(min_threatened_species) # print the min threatened species table


    data_file = user_csv.read_csv('/usercode/data_files/Data.csv', True) # read the data csv file


    num_max = np.array(data_file)               # make the data_file and array
    country_names_max = num_max[1:,1]           # store all of the country names in a 1d array by list slicing
    data_max = num_max[1:,2].astype(float).flatten() # store all of the max values as floats in a 1d array




    num_min = np.array(min_threatened_species)  # make the data_file and array
    country_names_min = num_min [1:,1]          # store all of the country names in a 1d array by list slicing
    data_min = num_min[1:,2].astype(float).flatten() # store all of the max values as floats in a 1d array
   
    #graphing
   
    plt.figure(figsize = (15,5))                  # create a figure
    plt.subplot(2,1,1)                            # create a subpolot for the first of 2 rows and 1 column
    plt.bar(country_names_max, data_max, color = '#fc63d8') # plot a bar grapgh with the data and make it a color
    plt.xticks(rotation=45, ha='right')           # rotates the country labels 45 degrees
    plt.ylabel('# of Threatened Species Type')         # creates the y axis label
    plt.title('Maximum Type of Threatened Species by Country') # creates the x axis label
    plt.tight_layout()                            # automatically adjusts the graph to scale.




    plt.pause(0.1)                                # runs a GUI event loop to ensure the while loop will run.




    plt.subplot(2,1,2)                            # creates a subplot for the second row in the figure
    plt.bar(country_names_min, data_min, color='#70eaec') # graphs the data as a bar graph
    plt.xticks(rotation=45, ha='right')           # rotates the country labels 45 degrees
    plt.ylabel('# of Threatened Species Type') # y axis label
    plt.title('Minimum Type of Threatened Species by Country') # x axis label
    plt.tight_layout()                            # autonatically adjusts the graph to scale
    plt.savefig("min_max_species.png")            # saves the figure as a png in the directory


    plt.pause(0.1) # runs a GUI event loop to ensure the while loop will run.




    







