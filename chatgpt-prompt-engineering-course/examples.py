def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt = f"""
Find an original source document regarding a product before answering. If there is actually a product called AeroGlide UltraSlim Smart Toothbrush created by the company Boie, tell me about that product. If there is not a product, simply tell me that there is no such product"""
response = get_completion(prompt)
print(response

#display(HTML(response))
import re
# Define regex pattern to extract text inside div tag
pattern = r'<*p>'
print(response)
# Use re.split to extract text and store in list called words
text = re.split(pattern, response)[1]  # Extract captured text
print(text)
words = text.split()  # Split text by whitespace into list called words

print(len(words))
# Print the list of words
print(words)  # Output: ['This', 'is', 'the', 'text', 'we', 'want', 'to', 'extract.'])

for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a product \ 
    review from an ecommerce site. 

    write a headline for each and give between 1 and 5 stars based on the revies. 

    Review: ```{reviews[i]}```
    """

    response = get_completion(prompt)
    print(i, response, "\n")


prompt = f"""
Is the writer of the following review expressing any issues that came up?\
If issues came up, add details of the issue such as what it was and if if was resolved.
Based on the results, is there anything that could be better, think carefully, is there anything that would make less work on the company, for example, what if the product could have been shipped more securing so things didn't break, could the packaging been done more safely perhap, think in the big picture and not just from the review itself?
The review is delimited with triple backticks. \
Give your answer as either yes or no.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)


prompt = f"""
In general, find things the company could do better, for example, if the product breaks in shipping indicate that the shipping could be done more securely

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)


prompt = f"""
Determine whether each item in the following list of \
topics is a topic in the text below, which
is delimited with triple backticks.

Give your answer in JSON format.\

List of topics: {", ".join(topic_list)}

Text sample: '''{story}'''
"""
response = get_completion(prompt)
print(response)


prompt = f"""
Determine whether each item in the following list of \
topics is a topic in the text below, which
is delimited with triple backticks.

Give your answer in JSON format.\

List of topics: {", ".join(topic_list)}

Text sample: '''{story}'''
"""
response = get_completion(prompt)
print(response)

import json

# Assuming `response` is the JSON string response
data = json.loads(response)

for topic in topic_list:
    if data.get(topic, True):
        print(f"ALERT: New {topic} story!")

prompt = f"""
proofread and correct this review. Make it more compelling. 
Ensure it follows APA style guide and targets an advanced reader. 
Output in markdown format with bulleted list
Text: ```{text}```
"""
response = get_completion(prompt)
print(response)

print(response)
from IPython.display import display, Markdown, Latex, HTML, JSON
display(Markdown(response))

from redlines import Redlines

diff = Redlines(text,response)
display(Markdown(diff.output_markdown))


prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service. 
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""
response_steady = get_completion(prompt, temperature=0)
response_random = get_completion(prompt, temperature=0.9)

from IPython.display import display, Markdown, Latex, HTML, JSON
from redlines import Redlines

diff = Redlines(response_random,response_steady)
display(Markdown(diff.output_markdown))

print(response_random)
print(response_steady)
