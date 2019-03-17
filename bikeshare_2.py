## path for this file: /Users/engin/Documents/COURSES/UDACITY PFDS/PYTHON/Projecti

import time
import pandas as pd
import numpy as np
import sys

#dictionary to file names for each city
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


LIST_OF_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print()
    print()
    print('Great! Let\'s explore some US bikeshare data!')
    print()
    print('-'*40)
    print()
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        #entries to accept:
        input_check_dict = {'c':'chicago', 'chi': 'chicago', 'chicago': 'chicago',
        'new york': 'new york', 'ny': 'new york', 'nyc': 'new york', 'new york city': 'new york',
        'n': 'new york', 'w': 'washington', 'washington': 'washington',
        'dc': 'washington', 'washington dc': 'washington'}
        user_input = input('Pick a city to analyze. Please enter "c" for Chicago, "n" for New York City, or "w" for Washington?').lower()
        print()
        #verify acceptable input, otherwise loop to question
        try:
            city = input_check_dict[user_input]
            break
        except KeyError:
            print()
            print('I didn\'t understand you.')
            print()


    # get user input for month type of filter or no filter
    while True:
        user_input = input('Would you like to filter the data by month, day, or '
        'not at all? Type "none" for no time filter.').lower()

        #check user's input against acceptable inputs, assign return variables
        if user_input in ['none', 'no', 'n']:
            month = 'all'
            day = 'all'
            break

        elif user_input.lower() in ['month', 'mo', 'm']:
            day = 'all'

            # get user input for month (all, january, february, ... , june)
            while True:
                #check if input acceptable, if not loop to question
                try:
                    month_input = input('''Pick a month. Enter "ja" for January,
                    "f" for February, "mr" for March, "a" for April, "my" for May,
                    or "ju" for June?''')

                    month_input_check_dict = {'january': 'January', 'jan': 'January', 'ja': 'January',
                    'february': 'February', 'feb': 'February', 'f': 'February', 'march': 'March',
                    'mar': 'March', 'mr': 'March', 'april': 'April', 'a': 'April', 'apr': 'April',
                    'may': 'May', 'my': 'May', 'jun': 'June', 'ju': 'June', 'june': 'June'}
                    month = month_input_check_dict[month_input.lower()]
                    break
                except KeyError:
                    print()
                    print('I did not understand what you entered.')
                    print()
            break

        elif user_input.lower() in ['day', 'd']:
            month = 'All'

            #get user input for day of the week
            while True:
                #check if input acceptable, if not loop to question
                try:
                    day_input = input('Pick a day. Enter "su" for Sunday, '
                    '"m" for Monday, "tu" for Tuesday, "w" for Wednesday, "th" for Thrusday',
                    '"f" for Friday, "sa" for Saturday').lower()

                    day_input_check_dict = {'su': 'Sunday', 'sunday': 'Sunday',
                    'monday': 'Monday', 'm': 'Monday', 'tuesday': 'Tuesday',
                    'tu': 'Tuesday', 'wednesday': 'Wednesday', 'w': 'Wednesday',
                    'thursday': 'Thursday', 'th': 'Thursday', 'friday': 'Friday', 'f': 'Friday',
                    'saturday': 'Saturday', 'sa':'Saturday'}
                    day = day_input_check_dict[day_input]
                    break
                except KeyError:
                    print()
                    print('I did not understand what you entered')
                    print()
            break

    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]


    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # check if the dataframe has more than a single month. if it does display the most common month
    if len(df['month'].unique()) > 1:
        most_common_month = LIST_OF_MONTHS[df['month'].mode()[0] - 1]
        print ('The month with the most travels is: {}'.format(most_common_month))

    # check if the dataframe has more than a single day. if it does display the most common day
    if len(df['day_of_week'].unique()) > 1:
        most_common_day = df['day_of_week'].mode()[0]
        print ('The day of the week with the most travels is: {}'.format(most_common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print ('The hour that is most popular to start a bike ride is: {}'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is ' + most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most popular end station is ' + most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['start and end station combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_start_end_combination = df['start and end station combination'].mode()[0]
    print('The most popular trip is ' +
    most_frequent_start_end_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = int(round(df['Trip Duration'].sum()/3600,0))
    print('Total travel time is approximatly ' + str(total_travel_time) + ' hours')


    # display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean()/60)
    print('Average travel time is approximately ' + str(mean_travel_time) + ' minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df.groupby(['User Type'])['User Type'].count()
    print('Breakdown of travles by the types of users is as follows:')
    print(user_type_counts)
    print()

    # Display counts of gender. Skip if city is washington
    if city != 'washington':
        gender_counts = df.groupby(['Gender'])['Gender'].count()
        print('Breakdown of travels by gender is as follows:')
        print(gender_counts)
        gender_null_counts =  df['Gender'].isnull().sum()
        print('We did not have gender information for ' + str(gender_null_counts) + ' travels')
        print()

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = int(df['Birth Year'].min())
        print('Earliest birth year for the users is ' + str(earliest_birth_year))
        print()
        most_common_birth_year = int(df['Birth Year'].mode())
        print('The most common birth year for users is ' + str(most_common_birth_year))
        print()
        most_recent_birth_year = int(df['Birth Year'].max())
        print('Most recent birth year for the users is ' + str(most_recent_birth_year))
        print()

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def restart():
    '''Asks the user if she would like to restart the program. Run main function if yes, exit if not yes'''
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart in ['no', 'n']:
            sys.exit()
        elif restart in ['yes', 'y']:
            main()
        else:
            print()
            print('I did not understand what you entered')
            print()


def main():
    #introduce program then confirm the user wants to proceed.
    while True:
        print('-'*40)
        print()
        print('Hello! I am excited to show you some interesting statistics on '
        'bike sharing!')
        print()
        print('I can show you statistics for three cities. And, you can pick a month or a '
        'day of the week to analyze.')
        print('If you would like to see statistics from all months and all days instead, you can do that too.')
        print()
        variable = input('Would you like to begin? Please enter "y" for yes, or "n" for no.')
        #if user does not want to begin, run restart function to give an opportunity to restart the program
        if variable.lower() in ['n', 'no']:
            print('-'*40)
            print('You selected to not continue.')
            print('-'*40)
            restart()
        #if user wants to begin, run the modules in order.
        elif variable.lower() in ['y', 'yes']:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city)
            break
        else:
            print('I did not understand what you entered.')


    #Notify end of statistics. Offer to show data 5 rows at a time.
    print()
    print('This is all the statistics I have to show you at this time.')
    start_index = 0
    while True:
        raw_data_request = input('Enter "yes" to see 5 rows from the data.')
        if raw_data_request.lower() in ['y', 'yes']:
            try:
                print(df.iloc[start_index: start_index + 5])
                start_index += 5
            except:
                print('End of data')
                break
        else:
            break

    #ask the user to restart program by running restart function
    restart()



if __name__ == "__main__":
	main()
