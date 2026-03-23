# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---1. the hints were backward to guess the number. I expected to follow the instruction and to go lower for the score but it should have been opposite because I should gone upwards 2. The scoring of this game is not logical. I was first expecting that the too low of the guess will not treated harshly by decreassing the score but instead this is treated harshly. 3. The New Game button was not working at any time. I was expecting the game to get refreshed after clicking the button but it was presenting me with the game over message.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I have used Copilot to use on this project. Example of AI was correct: AI was correct about the error in the logic of guess. AI suggested thst the hint's messages are inverted and when I was checking the logic I thought the same. So I verified the logic by swapping the message. Example of AI was incorrect
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I have fixed the code by using the pytest. AI helped with the process by giving answer to my logic question of the failed test and refactoring the code block. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Stremlit is like a whiteboard. When we rerun the streamlit web, it will erase all the output and the procedure. When we rerun it, it runs the entire python script from line 1. So rerunning is basically writing every similar thing on the whitboard after erasing it first. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- Answer:  This project changed me how I communicate with the AI agent. Because going over every logic of the code with AI gent is far better than just saying fix the error. 
