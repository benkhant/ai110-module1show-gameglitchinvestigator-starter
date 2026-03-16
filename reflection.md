# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
<<<<<<< HEAD
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
=======
The game run on the website and it looks pretty good.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The hints were wrong. I think they might be backwards from the correct order.
  Also, the new game button is not working as I could not restart the game. 
>>>>>>> 536293a (Fix Streamlit game state bugs and logic refactor)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

<<<<<<< HEAD
=======
Ans: I used Copilot as my teammate. Copilot suggested refactoring logic from `app.py` into `logic_utils.py` so I could unit test the game behavior more easily. I verified this by running `pytest` and confirming the new tests passed. Another suggestion from Copilot initially had the `new_game` reset missing the `status` field, which would keep the game stuck in `won`/`lost`. I found this by running the app and seeing `Game over` immediately, then fixed it to reset `status` to `playing`.
>>>>>>> 536293a (Fix Streamlit game state bugs and logic refactor)
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
<<<<<<< HEAD
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
=======
I decided a bug was fixed when the expected behavior matched both the app output and the unit tests after code changes. For example, the new game button now starts a fresh round instead of getting stuck.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran `pytest -q` with tests for `check_guess` and a new reset-state test. The tests passed, and manual Streamlit runs confirmed difficulty and new-game reset behavior now works.
- Did AI help you design or understand any tests? How?
Yes, AI helped me split logic into `logic_utils.py` so I could write focused unit tests, and it suggested adding a regression test for state reset to prevent the same bug.
>>>>>>> 536293a (Fix Streamlit game state bugs and logic refactor)

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
