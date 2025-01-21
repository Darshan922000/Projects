import pandas as pd
# student_dict = {
#     "student": ["darshan", "smit", "jinay"],
#     "score": [56,76,98]
# }
#
# # # looping through dictionary:-
# # for (key, value) in student_dict.items():
# #     print(value)
#
# student_dsta_frame = pd.DataFrame(student_dict)
# #print(student_dsta_frame)
#
# # loop through a data frame:-
# # for (key, value) in student_dsta_frame.items():
# #     print(value)
#
# # loop through the row of data frame
# for (index, row) in student_dsta_frame.iterrows():
#     #print(row.student)
#     if row.student == "darshan":
#         print(row.score)

# Project:- nato_phonetic_alphabet:-
''' Note:- We also update this code after learning handling errors in Day-30...'''

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter : row.code for (index, row) in nato_alphabet.iterrows()}

'''code_running = True
while code_running:
    #print(dict)
    user_word = (input("Enter a word: ")).upper()
    try:
        output_list = [dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, Only Letters In The Alphabet Please.")
        continue
    else:
        print(output_list)
        code_running = False'''

# Or...There is another method...

def generate_phonatic():
    user_word = (input("Enter a word: ")).upper()
    try:
        output_list = [dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, Only Letters In The Alphabet Please.")
        generate_phonatic()
    else:
        print(output_list)

generate_phonatic()