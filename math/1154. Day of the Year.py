"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41

Example 3:
Input: date = "2003-03-01"
Output: 60

Example 4:
Input: date = "2004-03-01"
Output: 61 

Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""

class Solution:
    def dayOfYear(self, date: str) -> int:
        #maps =  {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        year,month,day = date.split('-')
        if month == '01':
            return int(day)
        elif month == '02':
            return months[0] + int(day)
        else:
            days = int(day) 
            for i in range(int(month)-1):
                days += months[i]
            if (int(year) % 400 == 0) or ((int(year) % 4 == 0) and (int(year) % 100 != 0)):
                days += 1
            return days