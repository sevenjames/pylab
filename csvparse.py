"""
2020-02-18

Parse CSV file challenge
Given the file 'football.csv',
print the name of the team with the smallest difference
between 'goals' and 'goals allowed'

"""

import csv

def calc_best_a():
    """SKIP THE HEADER WITH A ROW POINTER AND CHECK"""
    with open('football.csv', newline='') as file:
        reader = csv.reader(file)
        team_data = list(reader)
        row_pointer = 0
        best_diff = 9999
        for row in team_data:
            if row_pointer == 0:
                pass
            else:
                goal_diff = abs(int(row[5]) - int(row[6]))
                if goal_diff < best_diff:
                    best_team = row[0]
                    best_diff = goal_diff
            row_pointer += 1
        print('Team', 'Diff')
        print(best_team, best_diff)

def calc_best_b():
    """SKIP THE HEADER BY REMOVING IT WITH POP()"""
    with open('football.csv', newline='') as file:
        reader = csv.reader(file)
        team_data = list(reader)
        team_data.pop(0)
        best_diff = 9999
        for row in team_data:
            goal_diff = abs(int(row[5]) - int(row[6]))
            if goal_diff < best_diff:
                best_team = row[0]
                best_diff = goal_diff
        print('Team', 'Diff')
        print(best_team, best_diff)

def calc_best_c():
    """SKIP THE HEADER BY SPECIFYING A SLICE INSTEAD OF THE WHOLE LIST"""
    with open('football.csv', newline='') as file:
        reader = csv.reader(file)
        team_data = list(reader)
        best_diff = 9999
        for row in team_data[1:]:
            goal_diff = abs(int(row[5]) - int(row[6]))
            if goal_diff < best_diff:
                best_team = row[0]
                best_diff = goal_diff
        print('Team', 'Diff')
        print(best_team, best_diff)
