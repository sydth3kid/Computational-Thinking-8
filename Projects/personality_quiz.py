#Beginning: create variables
waffle_points = 0
pancake_points = 0

#Middle: Ask questions
answer = input ("Would you rather eat A) bananas, or B) strawberries")
if answer == "A":
    waffle_points += 1
elif answer == "B":
    pancake_points += 1

answer = input ("Would you rather wear A) Athleta, or B) Lululemon")
if answer == "A":
    waffle_points += 1
elif answer == "B":
    pancake_points += 1

answer = input ("Do you like A) Blue, or B) Yellow")
if answer == "A":
    waffle_points += 1
elif answer == "B":
    pancake_points += 1

answer = input ("Would you eat A) maple syrup, or B) jam")
if answer == "A":
    waffle_points += 1
elif answer == "B":
    pancake_points += 1

answer = input("Would you rather drink A) coffee, or B) tea")
if answer == "A":
    waffle_points += 1
elif answer == "B":
    pancake_points += 1

#End: Give answer
if waffle_points > pancake_points:
    print("You are a Waffle")
elif pancake_points > waffle_points:
    print("You are a Pancake")