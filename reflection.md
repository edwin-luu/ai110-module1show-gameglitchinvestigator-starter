# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - Issue 1: When inputting a number lower than SECRET NUMBER, it said to go lower; when inputting a number higher than SECRET NUMBER, it said to go higher.
  - Issue 2: After inputting a number and pressing "Submit Guess", the History list does not show the number until after pressing "Submit Guess" on a subsequent number.
  - Issue 3: The "New Game" button generates a new SECRET number and resets the number of attempts to 0, does not clear the History list
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
1. Ok new bug. The game starts off saying I have 8 attempts left. After making my first guess, it still shows "Attempts left: 8". It decrements to 7 after the next guess. So when I run out of attempts, it shows I have 1 attempt left; so a delay of 1 attempt in each guess.
Remove:
      112 -st.info(                                                                                                                                                                                                
      113 -    f"Guess a number between 1 and 100. "                                                                                                                                                                     114 -    f"Attempts left: {attempt_limit - st.session_state.attempts}"                                                                                                                                       
      115 -)                                                                                                                                                                                                             116 -  

Fix:
      179 +with feedback:                                                                                                                                                                                          
      180 +    st.info(                                                                                                                                                                                                  181 +        f"Guess a number between {low} and {high}. "                                                                                                                                                  
      182 +        f"Attempts left: {attempt_limit - st.session_state.attempts}"                                                                                                                                         183 +    )                                                                                                                                                                                                         184 +      
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
1. The Higher and Lower logic looks good. Now, upon pressing Submit, the attempt doesn't go through and the History list doesn't update with the current guess.
Output: ● Update(app.py)
  ⎿  Added 8 lines, removed 8 lines
      118      st.write("Difficulty:", difficulty)
      119      st.write("History:", st.session_state.history)
      120
      121 -raw_guess = st.text_input(                                                                                                                                                                              
      122 -    "Enter your guess:",                                                                                                                                                                                
      123 -    key=f"guess_input_{difficulty}"                                                                                                                                                                     
      124 -)                                                                                                                                                                                                       
      121 +with st.form("guess_form"):                                                                                                                                                                             
      122 +    raw_guess = st.text_input(                                                                                                                                                                          
      123 +        "Enter your guess:",                                                                                                                                                                            
      124 +        key=f"guess_input_{difficulty}"                                                                                                                                                                 
      125 +    )                                                                                                                                                                                                   
      126 +    submit = st.form_submit_button("Submit Guess 🚀")                                                                                                                                                   
      127
      126 -col1, col2, col3 = st.columns(3)                                                                                                                                                                        
      128 +col1, col2 = st.columns(2)                                                                                                                                                                              
      129  with col1:
      128 -    submit = st.button("Submit Guess 🚀")                                                                                                                                                               
      129 -with col2:                                                                                                                                                                                              
      130      new_game = st.button("New Game 🔁")
      131 -with col3:                                                                                                                                                                                              
      131 +with col2:                                                                                                                                                                                              
      132      show_hint = st.checkbox("Show hint", value=True)
      133
      134  if new_game:
  This did not fix the issue.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
