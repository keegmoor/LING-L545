# Project

`In this project, I have created a pipeline that trains a pre-trained open-source conversational chatbot called DialoGPT to learn grammar and syntax from whatever books I feed in. From the Classic English Literature Kaggle Corpus here https://www.kaggle.com/datasets/raynardj/classic-english-literature-corpus , I have created 4 test models from different time periods that have distinct voices. With GPU acceleration on Google Colab, it takes only around 5 minutes to train the models, and the text generation based on user input is in real time. I used some of a Jupyter notebook from a tutorial on DialoGPT by Lynn Zhang here https://github.com/RuolinZheng08/twewy-discord-chatbot/blob/main/model_train_upload_workflow.ipynb to create the models.

Each model file is 510MB, and since Github limits storage space, I have stored these on Huggingface, a machine learning hosting website. By running the Talk.py file and following the prompts, you can speak to each of these chatbots. 

When the chatbot gets a response that is does not understand, it will respond in some way with several '!' or '?' in a row. When it was learning from both user and its own responses, one of these would trigger a chain of such reactions, so I have limited it to only seeing user-inputed chat history.`
