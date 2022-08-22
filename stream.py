from filecmp import clear_cache
import streamlit as st
import webbrowser
from time import sleep

st.title("Quiz game")

score = 0

first = st.selectbox("Which programming language is used for website designing?",("Html","Css","Javascript","Python"))
if first == "Css":
  st.balloons()
  st.success("Correct!")
  score+=1
else:
  st.warning("Wrong")
  score-=1
sleep(.20)
second = st.selectbox("When was Python invented?",("1998","1991","1997","1990"))
if second == "1991":
  st.balloons()
  st.success("Correct!")
  score+=1
else:
  st.warning("Wrong")
  score-=1
third = st.selectbox("What is the name of the developer of Python?",("Guido van Rossum","James Gosling","Sundar Pichai","Just Van Rossum"))
if third == "Guido van Rossum":
  st.balloons()
  st.success("Correct!")
  score+=1
else:
  st.warning("Wrong!")
  score-=1

st.write("Your score {}".format(score))