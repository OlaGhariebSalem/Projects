
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    def load_data(city,month,day):

    Returns:
        (str) User_city - name of the city to analyze
        (str) User_month - name of the month to filter by, or "all" to apply no month filter
        (str) User_day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    User_city = ''
    while User_city not in CITY_DATA.keys():
        print("\n Please choose your city: Chicago, New York City or Washington")
        User_city = input().casefold()
        if User_city not in CITY_DATA.keys():
            print("\nCity not found , please enter the correct city")
            User_city = input().casefold()
                
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    User_month = ''
    while User_month not in MONTH_DATA.keys():
        print("\nEnter the month : january, february, ... , june or all")
        User_month = input().lower()
        
        if User_month  not in MONTH_DATA.keys():
            print("\nInvalid input. Please enter month between january, ..........,june .")
            User_month = input().lower()
            
                

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    User_day = ''
    while User_day not in DAY_LIST:
        print("\nPlease enter a spicific day in the week or all:")
        User_day =input().lower()
        if User_day not in DAY_LIST:
            print("\nInvalid input. Please enter the correct day .")
            User_day = input().lower()
            
    print("\nYou have chosen to view data for city:{}".format (User_city) ," month/s:{}" .format (User_month) ,"and day/s:{}".format (User_day ))

    print('-'*40)
    return User_city, User_month, User_day


def load_data(User_city, User_month, User_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nRequesting data...")
    df = pd.read_csv(CITY_DATA[User_city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if User_month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       User_month = months.index(User_month) + 1
       
       df = df[df['month'] == User_month]
    
    if User_day != 'all':
        df = df[df['day_of_week'] == User_day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nThe Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    
    print("the most popular month is{}:" .format(popular_month))
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    
    print("the most popular day is:{}:" .format(popular_day))
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print("the most popular hour is{}:" .format(popular_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("the most common start station{}:" .format(common_start_station))
    

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("the most common end station:{}:" .format(common_end_station))
    

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print("\nThe most frequent combination of trips{}:" .format(combo))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """ Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
   
    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print("the total duration is:{}".format(total_duration))

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("the type of users are {}:".format(user_type))

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("the gender of users {}: ".format(gender))
    except:
        print("\nThere is no 'Gender' column in this city.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("the earliest birth year is {}:" .format(earliest),"\n the recent birth year is:{}".format(recent),"\n the common year is :{}".format(common_year))
    except:
        print("There are no birth year details in this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)
def disply_row_data(df) :
        # ask the user to display the data and prints 5 rows eachtime 
        print("Display row data :")
        row_data =input("Do you want to dislpay row data? Yes or No \n")
        if row_data.lower() =="yes":
            data_count = 0
            while True :
                print(df.iloc[data_count:data_count+5])
                data_count= data_count + 5
                ask = input("Load more 5 raws? Yes or No ")
                if ask.lower() != "yes" :
                    break
                       
def main():
        while True:
            User_city, User_month, User_day = get_filters()
            df = load_data(User_city, User_month, User_day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            disply_row_data(df)
            restart = input("\nWould you like to restart? Enter Yes or No.\n")
            if restart.lower() != "yes":
                break


if __name__ == "__main__":
                main()