#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import datetime
import pandas as pd
import numpy as np

# CITY_DATA DICTIONARY VALUES DEPEND ON THE CSV FILE LOCATION OR ADDRESS
# PLEASE CHECK YOUR CSV FILE LOCATION FIRST

CITY_DATA = { 'chicago': 'C:/Users/p&p/Desktop/chicago.csv',
              'new york city': 'C:/Users/p&p/Desktop/new_york_city.csv',
              'washington': 'C:/Users/p&p/Desktop/washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.
    
    Args:
        None.
        
    Returns:
        str (city): name of the city to analyze
        str (month): name of the month to filter by, or "all" to apply no month filter
        str (day): name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # welcome messege
    
    print('Hello! Let\'s explore some US bikeshare data! \n')
    
    # get user input for city (chicago, new york city, washington). 
    
    city = input('Please enter a city name ( chicago, new york city, washington) : ').lower()
    while city :
        if city == 'chicago' or city == 'new york city' or city == 'washington' :
            print('\n## Thanks, Your choosen city is {}. ##\n'.format(city)) 
            break
        else: 
            print('\n ## Sorry, You entered wrong city. ##\n\n## Please try cities specified between brackets only. ##\n')
            city = input('\n Please enter city name ( chicago, new york city, washington) : ').lower()

    # get user input for month (all, january, february, ... , june)
    
    month = input('\n Please enter month (all, january, february, march, ...., june) : ').lower()
    while month :
        if month == 'all' :
            print('\n## You choosed to see data of all months. ##\n')
            break
        elif month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' :
            print('\n## You choosed to see data of {} month. ##\n'.format(month))
            break
        else :
            print('\n ## Sorry, we don\'t have any data at this month. ##\n\n## Please try months specified between brackets only. ##\n')
            month = input('\n Please enter month (all, january, february, march, ...., june) :').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input('\n Please enter a day (all, monday, tuesday, ...., sundnay) : ').lower()
    while day :
        if day == 'all' :
            print('\n## You choosed to see data of all day(s) and {} month(s). ##\n'.format(month))
            break
        elif day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' :
            print('\n## You choosed to see data of {} and {} month(s). ##\n'.format(day,month))
            break
        else :
            print('\n## You enterd an invalid value. ##\n\n## Please try again. ##\n')
            day = input('\n Please enter a day (all, monday, tuesday, ...., sundnay) : ').lower()

    print('-'*100)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data to dataframe
    
    df = pd.read_csv(CITY_DATA[city])
    
    #convert columns to datetime
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    
    # create month column
    
    df['Month'] = df['Start Time'].dt.month_name()
    
    # create week day column
    
    df['Week day'] = df['Start Time'].dt.day_name()
    
    # create hour column
    
    df['Hour'] = df['Start Time'].dt.hour
    
    # filter by month
    
    if month != 'all' :
        df= df[df['Month'] == month.title()]

    #filter by day
    
    if day != 'all' :
        df= df[df['Week day'] == day.title()]

    return df

def time_stats(df):
    
    """ 
    Displays statistics on the most frequent times of travel.
    
    Args:
        (df): The data frame you wish to work with.
        
    Returns:
        None.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    popular_month = df['Month'].mode()[0]
    print('The most popular month is {}.\n '.format(popular_month))

    # display the most common day of week
    
    popular_day = df['Week day'].mode()[0]
    print('The most popular day is {}.\n'.format(popular_day))
  
    # display the most common start hour
    
    popular_hour = df['Hour'].mode()[0]
    print('The most popular start hour is {}.\n '.format(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    
    """ 
    Displays statistics on the most popular stations and trip.
    
    Args:
       (df): The data frame you wish to work with.
       
    Returns:
        None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is {} station(S).\n'.format(common_start_station))

    # display most commonly used end station
    
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is {} station(S).\n'.format(common_end_station))
  
    # display most frequent combination of start station and end station trip
    
    df['start_and_end_stations'] = df['Start Station'].astype(str) +' with ' + df['End Station'].astype(str)
    common_start_and_end =  df['start_and_end_stations'].mode()[0]
    print('The most frequent combination of trips are {} station(S).\n'.format(common_start_and_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        (df): The data frame you wish to work with.
        
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    total_duration = round(df['Trip Duration'].sum())
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trips duration is {} hours, {} minutes and {} seconds.\n'.format(hour, minute, second))

    # display mean travel time
    
    average_duration = round(df['Trip Duration'].mean())
    minute, second = divmod(average_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The average trips duration is {} hours, {} minutes and {} seconds.\n'.format(hour, minute, second))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    
    """
    Displays statistics on bikeshare users.
    
    Args:
       (df): The data frame you wish to work with.
       
    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_type = df['User Type'].value_counts()
    print('The number of different users type :\n\n{}\n'.format(user_type))

    # Display counts of gender
    
    try:
        gender = df['Gender'].value_counts()
        print('The number of different users gender :\n\n{}\n'.format(gender))
    except:
        print('\n## We have no users gender data for this city. ##\n')
        
    # Display earliest, most recent, and most common year of birth
    
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nThe earliest year of birth is {}.\n\nThe most recent year of birth is {}.\n\nThe most common year of birth is {}.\n'.format(earliest, recent, common_year))
    except:
        print('\n## We have no users birth year data for this city. ##\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
    
def display_data(df):
    
    """
    Displays 5 rows of data from the csv file for the selected city.
    
    Args:
        (df): The data frame you wish to work with.
        
    Returns:
        None.
    """
    
    user_ans = ['yes', 'no']
    row_data = ''
    counter = 0
    #get user input to view data
    while row_data not in user_ans :
        print('\nDo you wish to view the raw data? (yes or no)\n')
       
        row_data = input().lower()
    
        if row_data == "yes":
            print(df.head())
        elif row_data not in (user_ans):
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #create loop to continue viewing data
    
    while row_data == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        row_data = input().lower()
        
        if row_data == "yes":
             print(df[counter:counter+5])
        elif row_data != "yes":
             break

    print('-'*100)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




