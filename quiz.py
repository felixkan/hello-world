# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:07:26 2021

# streamlit run quiz.py
"""


import streamlit as st
import time

"""
# Emotion Quiz
Get ready to answer these questions and you'll see what is your emotion!'
"""

scores = []

options = ['A: Pizza', 'B: Hot Dog',  'C: Curry',  'D: Bun']
points = [10, 30, 5, 20]
score_dict = dict(zip(options, points))
ans = st.selectbox(
        """
        Q1: What do you like to eat? 
        """,
        options)
scores.append(score_dict[ans])

options = ['A: Coca cola', 'B: Canada Dry',  'C: Nestea',  'D: Sprite']
points = [30, 5, 20, 10]
score_dict = dict(zip(options, points))
ans = st.selectbox(
        """
        Q2: Choose a kind of pop. 
        """,
        options)
scores.append(score_dict[ans])

options = ['A: Basketball', 'B: Soccer',  'C: Badminton',  'D: Tennis']
points = [20, 5, 30, 10]
score_dict = dict(zip(options, points))
ans = st.selectbox(
        """
        Q3: Which sport is most interesting to you? 
        """,
        options)
scores.append(score_dict[ans])


options = ['A: Purple', 'B: Green',  'C: Red',  'D: Blue']
points = [10, 30, 5 ,20 ]
score_dict = dict(zip(options, points))
ans = st.selectbox(
        """
        Q4: Choose a colour. 
        """,
        options)
scores.append(score_dict[ans])

options = ['A: Fall', 'B: Spring',  'C: Summer',  'D: Winter']
points = [5, 20, 30 ,10 ]
score_dict = dict(zip(options, points))
ans = st.selectbox(
        """
        Q5: Which season do you like? 
        """,
        options)
scores.append(score_dict[ans])
# -------------------- #

# Calculate the total score and output the result.
total_score = sum(scores)

if 130 <= total_score <= 150:
    result = "angry"
elif 51 <= total_score <= 100:
    result = "calm"
elif 0 <= total_score <= 50:
    result = "sad"
elif 101 <= total_score <= 130:
    result = "happy"
else:
    result = "What in the whole wide world?! You didn't pass the quiz!"


# Output the results.
left_column, right_column = st.beta_columns(2)
pressed = right_column.button('See what is your emotion!')
if pressed:
    f"""## You are {result}!! Good job!   
    You got {total_score} points in total.Thank you for doing the quiz!"""
    





