# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# 1. Create a variable for every player that scored
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

# 2. Create a variable for each minute of the match that a goal was scored in
goal_0 = 32
goal_1 = 54

# 3. Using the +-operator, create a string that reports on who scored when,
# according to the format
scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
print(scorers)

# 4. Use f-strings or the +-operator to create a single string with information
# about who scored when in the format
report = f'{scorer_0} scored in the {str(goal_0)}nd minute\n{scorer_1} scored in\
 the {str(goal_1)}th minute'
print(report)

# 1. Choose a player that played in the soccer match and store his name as a
# string 
player = "Ronald Koeman"

# use slicing and the find-method (help) to isolate and store the player's first
# name
y = player.find("Ronald")
z = player.find("Koeman")
first_name = player[:7].rstrip()

# 3. use find, slicing and len to isolate and store the length of their last name
last_name_len = len(player[7:])

# 4. isolate and store the player's name in this format
name_short = player[:1]+ '.' + ' ' + player[7:]
print(name_short)

# 5. his is what the crowd chants when it looks like your player is going to score
# a goal -- their first name plus an exclamation mark(!), x-times, where x is the
# number of characters in their first name. Make sure the last character of this
# string is not a space!
first_name_len = len(player[:7].rstrip())
chant = ((first_name + '!' + ' ') * first_name_len).rstrip()

# Make super-sure the last character of chant is not a space by using the
# inequality operator(!=).
good_chant = chant != " "
print(good_chant)