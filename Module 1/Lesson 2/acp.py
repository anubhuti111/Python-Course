# ================================
# PERSONAL GOALS DISPLAY
# ================================

# ---------- PART 1: import the keyword module ----------
# YOUR CODE HERE
# One line. You need this for Part 7.
import keyword

# ---------- PART 2: ask the three questions ----------
# YOUR CODE HERE
# Use input() three times and store each answer in its own variable:
#   person_name    <- "Enter your name: "
#   goal_name      <- "Enter one skill you want to get better at: "
#   target_month   <- "Enter the month you want to reach it by: "
name = input("Enter your name: ")
goal_name = input("Enter one skill: ")
target_month = input("Enter trget month: ")

# ---------- PART 3: store the practice time ----------
# YOUR CODE HERE
# Store the number 30 in a variable called daily_minutes.
# Type it as 30, NOT as "30".
daily_minutes = 30

# ---------- PART 4: the heading ----------
# YOUR CODE HERE
# Print MY PERSONAL GOAL PLAN with one blank line above it and one below.
# Do it in a single print() using \n at the start and the end.
print("\nMY PERSONAL GOAL PLAN\n")

# ---------- PART 5: the four plan lines ----------
# YOUR CODE HERE
# Four print() statements, each with a label and a variable separated by a comma:
#   Name: ...
#   Goal: ...
#   Target month: ...
#   Daily practice: ... minutes      <- this one has THREE values
print("Name: ", name)
print("Goal: ", goal_name)
print("Target month: ", target_month)
print("Daily practice: ", daily_minutes, "minutes")

# ---------- PART 6: two lines that join up ----------
# YOUR CODE HERE
# Print "Status:" ending in a space, then "Not started" on the next print.
# Print "Reminder:" ending in " - ", then "Practise every day!" on the next print.
# Both pairs must appear on ONE line each in the output.
print("Status ", end=" ")
print("Not Started")
print("Reminder", end="-")
print("Practice Everyday")


# ---------- PART 7: the sentence and the keywords ----------
# YOUR CODE HERE
# Print "In one sentence:" then one print() that joins the name, the goal,
# the minutes and the month into a readable sentence.
# Then print Python's reserved word list using
print("In one sentence: ")
print(name, "has to develop ", goal_name, " skill by ", target_month, " dedicating ", daily_minutes, "minutes everyday")
print ("\n")
print(keyword.kwlist)