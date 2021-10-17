"""
Dictionaries
"""


friends_list = [
  {"name": "Emad", "age": 40},
  {"name": "Amjad","age": 47},
  {"name": "Tamer", "age": 44},
  {"name": "Yanal", "age": 48}
]

# update first name
friends_list[0]["name"] = "William"

# print first friend name
print(friends_list[0]["name"])

# print all friends
print(friends_list[0])

# ====================
print("\n")

students_score = {"Emad": 96, "Amad": 88, "Tamer": 85}

for name, score in students_score.items():

  print(name, score)


# calculate average scores:

scores_list = list()
for score in students_score.values():
  scores_list.append(score)

scores_sum = sum(scores_list)
avg_scores = scores_sum / len(scores_list)
# round avg score to the nearest two decimals  
print(f"avg_scores: {avg_scores:.2f}")
