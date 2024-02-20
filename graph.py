# Importing our libaries for our system 
# Each libary has been renamed to a two letter str for ease of use
import pandas as pd
import matplotlib.pyplot as mp
import datetime as dt



# Displays ALL data from the CSV
df = pd.read_csv("data.csv")

#Displays the main menu and collects choice of menu item
def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show total sales for all items")

        main_menu_choice = input("Please enter the number of your choice (1-2): ")
        print("###############################################")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")
    # Checks if the user has selected a valid menu item
        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):#
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]
    # Creating our graph in order to graphically show our data to our user
    result = pd.concat([df1, df2], axis=1, join='inner').where(df1["Menu Item"] == item)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    # Calculating the average number of food items sold and plotting them on Matplotlib
    average = df3.mean()
    average.plot()
    # Creating labels for our graph
    mp.title("Sales data for Gurrebs BBQ")
    mp.ylabel(f"Average Number of {item} sold")
    mp.xlabel(f"Dates selected for Sales data")
    # Showing our graph on a UI alongside a grid to see where data is
    mp.grid()
    mp.show()
    return result
 #   return df3
# Imports CSV file and returns all data to user
def show_all_data():
    startdate = "03/03/2023"
    enddate = "31/05/2023"
    item = "All Items"
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[:,startdate:enddate]
    df3 = df1.loc[df1['Menu Item'] == item]
    # Creating our graph in order to graphically show our data to our user
    result = pd.concat([df1, df2], axis=1, join='inner').where(df1["Menu Item"] == item)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    # Calculating the average number of food items sold and plotting them on Matplotlib
    average = df2.mean()
    average.plot()
    # Creating labels for our graph
    mp.title("Sales data for Gurrebs BBQ")
    mp.ylabel(f"Average Number of {item} sold")
    mp.xlabel(f"Dates selected for Sales data")
    # Showing our graph on a UI alongside a grid to see where data is
    mp.grid()
    mp.show()
# Main menu choice 1
main_menu = menu()
if main_menu == 1:
    # Getting variables for pandas CSV file
    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    extract_no_index = extracted_data.to_string(index=False)

# Main menu choice 2
elif main_menu == 2:
    show_all_data()

# Checks if choice is not 1 or 2 and then will tell user to pick from 1 or 2 again.
else:
    print('This is not a choice inside the program. Please select from 1 or 2')
    main_menu()
