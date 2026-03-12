# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game involved typing a number as a guess and seeing if I could guess the secret number before exceeding the number of attempts. The issues found are in the following response.
- List at least two concrete bugs you noticed at the start (for example: "the secret number kept changing" or "the hints were backwards").
  - Issue 1: When inputting a number lower than SECRET NUMBER, it said to go lower; when inputting a number higher than SECRET NUMBER, it said to go higher.
  - Issue 2: After inputting a number and pressing "Submit Guess", the History list does not show the number until after pressing "Submit Guess" on a subsequent number.
  - Issue 3: The "New Game" button generates a new SECRET number and resets the number of attempts to 0, and this does not clear the History list.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code CLI as the AI tool for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Ok new bug. The game starts off saying I have 8 attempts left. After making my first guess, it still shows "Attempts left: 8". It decrements to 7 after the next guess. So when I run out of attempts, it shows I have 1 attempt left; so a delay of 1 attempt after each guess.
Remove:
      112 -st.info(                                                                                                                                                                                                
      113 -    f"Guess a number between 1 and 100. "                                                                                                                                                                     114 -    f"Attempts left: {attempt_limit - st.session_state.attempts}"                                                                                                                                       
      115 -)                                                                                                                                                                                                             116 -  

Fix:
      179 +with feedback:                                                                                                                                                                                          
      180 +    st.info(                                                                                                                                                                                                  181 +        f"Guess a number between {low} and {high}. "                                                                                                                                                  
      182 +        f"Attempts left: {attempt_limit - st.session_state.attempts}"                                                                                                                                         183 +    )                                                                                                                                                                                                         184 +      

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The Higher and Lower logic looks good. Now, upon pressing Submit, the attempt doesn't go through and the History list doesn't update with the current guess.
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
  This did not fix the issue. I tested it by restarting the application and running "python -m streamlit run app.py". Upon restarting the application, I attempted to make a guess and the guess didn't change the number of attempts I have made nor added my guess to the History list. Upon submitting a second guess, the first guess was registered, where the number of attempts was changed by one and the History list registered this first guess; but now, the second guess was not registered. So the application was "lagging" by one guess after every guess attempt.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
To decide whether a bug was really fixed, I restarted the application by pressing Ctrl+C to terminate the application and running "python -m streamlit run app.py" in the CLI to start it up. Upon the application restart, I would make the action and compare the result vs. what I expected. If there was no difference between the application's result(s) and my expectations, then the bug was fixed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
One pytest I ran was the one in the tests\test_game_logic.py file to test the "Go HIGHER" and "Go LOWER" logic on guess attempts. I asked Claude Code to write me five test cases (two lower, two higher, and one matching cases), as well as run pytest on that file. The result was that all five test cases passed.
- Did AI help you design or understand any tests? How?
AI did help me see one of the logical issues involving the inverse logic in the response to a guess being HIGHER or LOWER. It pointed out that the initial code was showing the message to "Go HIGHER" when a guess was higher than the secret number, and "Go LOWER" when a guess was lower the secret number; both cases are inverses of each other. AI pointed them out in the lines 38, 40, 46, and 47 of the app.py file. With that, I was able to ask it to swap the logic to execute the fix.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number was not changing unless I pressed "New Game." Thus, there were no bugs regarding the secret number constantly changing. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit "reruns" occur when the program completely restarting every time the user interacts with the application. For instance, when the user clicks a button, the script runs and the app goes into a new state; when a user types in a text box, the script also runs and the app goes into a new state. To fix this, a session state is provided by Streamlit to keep local variables persisted until the user explicitly wants to restart the game (ex. pressing "New Game").
- What change did you make that finally gave the game a stable secret number?
No change was needed in this program. The program was already giving a stable secret number for each game. The block that allowed this was:
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
One strategy I repeatedly use in this project that I would like to reuse in future labs or projects would be to experiment with the existing application to really understand any bugs that may appear rather than not experimenting and instead, just attaching the file to AI and asking it to "fix any bugs." When attempting to use AI to fix bugs, I found that tackling one bug at a time allowed me to track and understand what is fixed and what is not fixed after every attempt.
- What is one thing you would do differently next time you work with AI on a coding task?
One thing that I would do differently next time would be to explain the bug to Claude Code in a clearer manner to prevent it from falsely fixing a bug. There were times when Claude Code said it fixed the bug that I was targeting even though the bug persisted. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project allowed me to see how much I overestimated Claude Code to write code. Unless I explained complex bugs clearly, Claude Code struggled to fix them.
