# 1.dict.get(key, default)
# Returns the value for the given key if it exists in
# the dictionary, otherwise returns the specified default value.

grades = {"Math": 90, "Science": 85}
math_grade = grades.get("Math", "N/A")
english_grade = grades.get("English", "N/A")
print("Math Grade:", math_grade)
print("English Grade:", english_grade)

#2. dict.keys()
# Returns a view of the dictionary's keys.

grades = {"Math": 90, "Science": 85}
subject_names = grades.keys()
print("Subjects:", list(subject_names))


#3. dict.values()
# Returns a view of the dictionary's values.

grades = {"Math": 90, "Science": 85}
score_values = grades.values()
print("Scores:", list(score_values))

#4. dict.items()
# Returns a view of the dictionary's key-value pairs as tuples.
grades = {"Math": 90, "Science": 85}
subject_scores = grades.items()
print("Subject Scores:", list(subject_scores))

#5. dict.pop(key, default)
# Removes and returns the value associated with the given key.
#  If the key is not found, it returns the specified default value.

grades = {"Math": 90, "Science": 85}
math_grade = grades.pop("Math")
english_grade = grades.pop("English", -1)
print("Removed Math Grade:", math_grade)
print("Removed English Grade (default):", english_grade)

#6. dict.popitem()
# Removes and returns a random key-value pair as 
# a tuple from the dictionary.

grades = {"Math": 90, "Science": 85, "History": 78}
removed_item = grades.popitem()
print("Removed Item:", removed_item)
print("Updated Dictionary:", grades)

#7. dict.clear()
# dict.clear()
# Removes all items from the dictionary, making it empty.
grades = {"Math": 90, "Science": 85}
grades.clear()
print("Cleared Dictionary:", grades)

