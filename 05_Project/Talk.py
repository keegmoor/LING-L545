from transformers import AutoModelWithLMHead, AutoModelForCausalLM, AutoTokenizer
import torch


YEAR = input('Select year range from the following built models:\n1: 0-1500\n2: 1500-1700\n3: 1700-1850\n4: 1850-1900\n')
while YEAR not in ['1', '2', '3', '4']:
    YEAR = input('Type one of 1, 2, 3, or 4 ')
years = {'1':'0-1500', '2':'1500-1700', '3':'1700-1850', '4':'1850-1900'}
YEAR = years[YEAR]
tokenizer = AutoTokenizer.from_pretrained('keeg8/Book-' + YEAR)

model = AutoModelWithLMHead.from_pretrained('keeg8/Book-' + YEAR)
print('loading model ' + 'Book-' + YEAR)
# Let's chat for 4 line



for step in range(10):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')
    # print(new_user_input_ids)

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    # generated a response,
    chat_history_ids = model.generate(
        bot_input_ids,max_length = 100,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature=0.8
    )
    # pretty print last output tokens from bot
    print("Bot: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))