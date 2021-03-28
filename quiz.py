# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:07:26 2021

# streamlit run draft_quiz.py
"""

import streamlit as st
import time

"""
# Emotion Quiz
Here's our first attempt to create a quiz!
"""

scores = []

options = ['A: purple', 'B: green',  'C: red',  'D: blue']
points = [20, 5, 10, 30]
score_dict = dict(zip(options, points))
ans = st.selectbox(
        """
        Q1: What is your favourite colour? 
        """,
        options)
scores.append(score_dict[ans])
# 'You selected: ', ans
# st.write( f"You got {score_dict[ans]} points." )

options = ['A: ermine', 'B: dolphin',  'C: red panda',  'D: koala']
points = [10, 30, 20, 5]
score_dict = dict(zip(options, points))
ans = st.selectbox(
        """
        Q2: What is your favourite animal? 
        """,
        options)
scores.append(score_dict[ans])
# st.write( f"You got {score_dict[ans]} points." )

options = ['A: badminton', 'B: tennis',  'C: basketball',  'D: running']
points = [10, 30, 20, 5]
score_dict = dict(zip(options, points))
ans = st.selectbox(
        """
        Q3: What is your best sports? 
        """,
        options)
scores.append(score_dict[ans])
# st.write( f"You got {score_dict[ans]} points." )

# -------------------- #

# Calculate the total score and output the result.
total_score = sum(scores)

if 0 <= total_score <= 100:
    result = "angry"
elif 101 <= total_score <= 150:
    result = "calm"
elif 151 <= total_score <= 200:
    result = "sad"
elif 201 <= total_score <= 250:
    result = "happy"
else:
    result = "unknown"

# print(f"You got {total_score} points in total.")
# print(f"You are {result} !!")

left_column, right_column = st.beta_columns(2)
pressed = right_column.button('Done!')
if pressed:
    # right_column.write(f"You got {total_score} points in total.")
    # right_column.write(f"You are {result}!!")
    f"""## You are {result}!!   
    You got {total_score} points in total."""
    





