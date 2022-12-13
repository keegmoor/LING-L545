# Project

`In this project, I have created a pipeline that trains a pre-trained open-source conversational chatbot called DialoGPT to learn grammar and syntax from whatever books I feed in. From the Classic English Literature Kaggle Corpus here https://www.kaggle.com/datasets/raynardj/classic-english-literature-corpus , I have created 4 test models from different time periods that have distinct voices. With GPU acceleration on Google Colab, it takes only around 5 minutes to train the models, and the text generation based on user input is in real time. I used some of a Jupyter notebook from a tutorial on DialoGPT by Lynn Zhang here https://www.freecodecamp.org/news/discord-ai-chatbot/ to create the models.

Each model file is 510MB, and since Github limits storage space, I have stored these on Huggingface, a machine learning hosting website. By running the Talk.py file and following the prompts, you can speak to each of these chatbots. 

When the chatbot gets a response that is does not understand, it will respond in some way with several '!' or '?' in a row. When it was learning from both user and its own responses, one of these would trigger a chain of such reactions, so I have limited it to only seeing user-inputed chat history.

Checker.py is what I used to check the books database I was using for any key words or phrases the chatbots were using, to make sure that the vocabulary was all from the books, and not the initial training of the open-source skeleton. I have never caught it using a word that was not in its learning. Since model trainin time and space requirements are both directly proportional to how much training data is inputted, I limited it to using 900 sentences to train and 100 to validate. However, each sentence had both itself and the 5 previous sentences for context, so the training size is closer to 4500 sentences. With larger training data, the GPU storage would run out shortly into training, and without that the training would have taken many hours if not days.`

Examples:

0-1500:
>> User:What is your name?
Bot: oedipus, you are my son.
>> User:Who am I?
Bot: !!!
>> User:what year is it?
Bot: i will tell you the year of my birth, when i will be a child of a man.
>> User:What year were you born, then?
Bot: i am a woman of the law, and i have been to the land of jupiter, and to the earth of mars.


1500-1700:

>> User:Hello?
Bot: no, sir, sir.
>> User:Who are you?
Bot: girard.
>> User:Who am I?
Bot: paul.
>> User:what year is it?
Bot: come, here, let me go to the door.
>> User:which door?
Bot: the one with the little black door, that's been opened, and all the houses are set up, and the doors are all set up and all there are the gates, and so on.


1700-1850:

>> User:Hello?
Bot: i am the girl, and i know her well.
>> User:What is your name?
Bot: "i have a brother named brian, and i have a sister named mary."  ***this seems like a quote, but it doesn't actually appear in any book***
>> User:Who is brian?
Bot: 'brian,' answered mr. jones, 'i am the son of a lady, i am the daughter of a man, i believe i am not your father. ***this appears in no book***
>> User:what year is it?
Bot: !!!


1850-1900:

>> User:hello?
Bot: i've been gone for a long time, and i have no idea what you're saying.
>> User:who are you?
Bot: i am jane.
>> User:what year is it?
Bot: i'm going to ask my doctor.
>> User:what is your doctor's name?
Bot: you have a doctorate in philosophy.
>> User:who am I?
Bot: you are the son of god.
