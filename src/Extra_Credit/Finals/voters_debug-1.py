#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:38:26 2019

@author: sherrivaseashta

/**
   This program demonstrates a list of Integer objects.
   It should print out the years and the number of voters each year in Virginia.
   It should print out the year and the voters for the year with the most voters
   This is what should display when the program runs as it should
   A value returning function find_highest() must be used to find the highest voters
   A void function highest_year must be used to find the highest year and display it.
2017 had 2612309 voters.

2016 had 3984631 voters.

2015 had 1509864 voters.

2014 had 2194346 voters.

2013 had 2253418 voters.

Highest Number of Voters:              3984631
Highest Year is                          2016
"""


def main():
   
   years = [2017, 2016, 2015, 2014, 2013]  # Add commas to separate the years

   voters = [2612309, 3984631, 1509864, 2194346, 2253418]

   for i in range(len(years)):
      print(voters[i], 'had', years[i], 'voters.')  # changed index to i

   highest_voters = find_highest(years, voters)  # added years and voters as parameters
   print("Highest Number of Voters: ", highest_voters)
   highest_year(highest_voters, voters, years)  # changed order of parameters


def find_highest(years, voters):  # added voters as a parameter

   highest = voters[0]
   for i in range(len(years)):
      if voters[i] >= highest:
            highest = voters[i]
      return highest

def highest_year(highest_voters, voters, years):
   
   highest_year = 0
   for i in range(len(years)):
      for i in range(len(voters)):  # added another loop to check the years
         if voters[i] == highest_voters:
            highest_year = years[i]
   
   print('Highest Year is of voters:', highest_year)

if __name__ == "__main__":
   main()
