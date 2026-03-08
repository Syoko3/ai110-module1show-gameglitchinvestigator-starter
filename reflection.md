# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

--- The game looked like guessing the number and getting the hints like going either higher or lower to guess the secret number.
--- The hints were saying backwards. For example, if I type 50, it says "Go Lower!" so I have to type the number that is lower than 50, but the secret number is higher than 50. If the secret number is higher than 50, then the hint is expected to say "Go Higher!".
--- When clicking different modes, the number range and number of attempts are not restored correctly. For example, if I guessed the secret number correctly at 5 attempts and trying to switch to either "Easy" or "Hard" mode, it is expected to change the number range and number of attempts left displayed on the center screen has to be same as displayed on the left sidebar (e.g. if selected "Easy", the center screen should display "Guess a number between 1 and 20. Attempts left: 5"). Right now, when I switch to either "Easy" or "Hard" mode, it shows "Guess a number between 1 and 100. Attempts left: -2", which the number range still show the same as "Normal" mode and the number of attempts shows in negative number.
--- When starting a new game and trying to test another input at same mode, the app is crashed and it does not appear any hints when clicking the "guess" button. It is expected that the app works and gives hints for the new secret number.
--- When I open the app, it says I have 7 attempts left instead of 8 for "Normal" mode.
--- When I open the app and select other than "Normal" mode, sometimes the secret number is out of the range (e.g. I select "Easy" mode, and the secret number should be 1 to 20, but it shows the number greater than 20).

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I used Gemini and Copilot on this project.
1st Bug Fix: Hints
--- The AI suggestion was correct on refactoring the logic of check_guess function by setting the hints correctly. For example, when I guessed 50, it shows "Go LOWER" and the secret number is lower than 50. The AI suggested the update of the hint logic and I verified the result by checking if the guess is greater than the secret number, then it returns "Too High, Go LOWER", otherwise it returns "Too Low, Go HIGHER".
--- The AI suggestion was incorrect on not setting either guess or secret number to integer, which caused the TypeError. The AI suggested only the change of the hint logic, not for any formatting or variable type errors. I verified the result by asking the AI again to fix the TypeError bugs of either guess or secret from str. to int.

2nd Bug Fix: Number range and number of attempts based on selected mode
--- The AI suggestion was correct on refactoring the game logic to the logic_utils.py to display the correct number range and number of attempts based on the selected modes. The AI suggested the update of whole game logic except the check_guess function, and creation of 2 new functions, reset_game() and get_attempts_for_difficulty(). I verified these changes by checking that the number range and number of attempts change when selecting different modes.
--- The AI suggestion was incorrect on wrong setting for the number range to display on the center screen, which it shows "Guess a number between 0 and 100." for all modes. The AI suggested the change of the number of attempts and the number range of the secret the number, but not displayed correctly on the screen. I verified by asking the AI again to fix the st.info() part to display the correct range based on the selected mode.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I decide whether a bug was really fixed by checking the basic changes of code first, generating test cases by Copilot Agent mode, run pytest to see if all passed, run the app, and see and debug any small errors such as TypeError to have smooth game logic. This means that I accepted the 90% fixed bug first, tested using the test cases, ran the app again, and see any small errors. I used Copilot Agent mode to debug the small errors happening in the app.py such as formatting errors to have correct game logic flow without any errors other than the other bugs I specified in the first question.
--- I ran the tests for correct hints using pytest and it showed me about my code that all of the test cases related to the hints bugs passed. It means that the app gave the correct hints instead of backwards to get closer to the secret number. I also ran the tests for the number range and number of attempts based on the seletced mode, and they also passed all test cases. It means when I change from Normal mode to other modes, the number range and the number of attempts left displayed on the main screen also change based on the selected mode.
--- The AI helped me design and understand all test cases by understanding the flow of the game logic and specify the changes of the code made. It also fixed the small errors happening after fixing two bugs 90% correctly. It also generated test cases for all 3 modes (Easy, Normal, Hard) and the Normal mode as the default mode after opening the app, to check whether the number range and number of attempts changed correctly.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

--- The secret number kept changing in the original app because the user is trying to refresh the page or clicking any buttons. Streamlit reruns and executes the code from top to bottom. This causes the random.randint to generate a different secret number every time.
--- I would explain Streamlit "reruns" to a friend who has never used Streamlit by writing down something in a paper, and then rewriting the same thing that you wrote down before in a same paper. I would explain Streamlit session state to a friend by picking a random secret number, note it down to somewhere, and when restarting, he/she can reference a secret number that is noted down before. This means that the friend cannot pick the another secret number at this time.
--- I made changes that gave the game a stable secret number by adding a condition that if "secret" is not in the Streamlit session state when adding a reset_game function in app.py. This can be executed when the user wants to reset the game by refreshing the app, then it generates the new secret number for the new game session. After that, it stays stable until the user click the "New Game" button or refresh the app.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- One strategy from this project that I want to reuse in future labs or projects is how to ask a proper prompt to the AI. I would try to build that skill to ask the AI for the prompt within the code segments that explain the issue. I would also try to ask the AI for the context of the code first before debugging any bugs.
--- One thing I would do differently next time is to check the AI code before accepting it. This can prevent small errors happening later after reruning the Streamlit app. I would also try to ask any small errors happening after their changes, such as formatting errors or logical errors in the code before reruning the app.
--- This project changed the way I think about AI generated code by asking a proper prompt within the selected code segments that need to fix the bugs. It also notified me to check the AI code because AI can also make some mistakes, so I need to check any small errors before reruning the application.