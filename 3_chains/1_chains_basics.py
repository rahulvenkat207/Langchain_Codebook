from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
#Prompt with single placeholder
template = "Tell me a joke about {topic}."

prompt_template = ChatPromptTemplate.from_template(template)
chain = prompt_template | model | StrOutputParser()
result = chain.invoke({"topic": "Virat"})
print("--------")
print(result)


#Prompt with multiple placeholder
template_multiple = """You are helpful assistant.
Human:Tell me a {adjective} story about a {animal}.
Assistant:"""

prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
chain = prompt_multiple | model | StrOutputParser()
prompt =chain.invoke({"adjective":"funny","animal":"Lion"})
result = model.invoke(prompt)
print("--------")
print(result.content)


# prompt with System and  Human messages(using tuples)

messages = [
    ("system", "you are a comedian who tells joke about {topic}"),
    ("human", "tell me {no} of jokes")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
chain = prompt_template | model | StrOutputParser()
prompt = chain.invoke({"topic":"Poilce","no":3})
print("--------")
print(result.content)

"""--------
Why did Virat Kohli bring a ladder to the cricket ground?

He heard the bowlers were going to give him some short deliveries!

--------
This is a great little story! It's humorous and well-written. Here are a few of its strengths:

* **Humorous premise:** The idea of a lion tripping over his own mane is inherently funny, and you've executed it well. 
* **Character development:** Leo's character is well-defined. He's proud but incompetent, which makes him relatable and sympathetic despite his predatory nature. Zelda, the sassy zebra, also adds a lot of personality to the story.
* **Vivid imagery:**  Descriptions like "his heart pounding a dramatic rhythm against his ribs" and "a spray of water droplets flying" create a clear picture in the reader's mind.
* **Dialogue:** The dialogue is snappy and entertaining, particularly Zelda's lines.  "Nice mane trip, Leo. Did you get a perm?" is a great comedic line.
* **Pacing:** The story moves along at a good pace, keeping the reader engaged.
* **Satisfying ending:** The ending is humorous and leaves the reader with a smile.  Leo's resignation to sticking with tortoises is a funny and fitting conclusion.


Here are a few minor suggestions, though the story works perfectly well as it is:

* **Show, don't tell:**  While the story is generally well-written, there are a few places where you could show rather than tell. For example, instead of saying "his hunting skills… well, let's just say they were still a work in progress," you could show this through a brief anecdote of a previous failed hunting attempt.
* **Build up the tension:** You could slightly increase the tension before Leo's fall.  Perhaps describe him getting closer and closer to the zebras, his excitement building, before the comedic mishap.
* **Consider adding a little more conflict:** While the story works well as a humorous anecdote, you could consider adding a small element of conflict.  Perhaps Leo needs to catch something to prove himself to the other lions, or maybe he's particularly hungry. This could add another layer to the story.


Overall, it's a very enjoyable and well-written story.  I chuckled throughout!

--------
This is a great little story! It's humorous and well-written. Here are a few of its strengths:

* **Humorous premise:** The idea of a lion tripping over his own mane is inherently funny, and you've executed it well. 
* **Character development:** Leo's character is well-defined. He's proud but incompetent, which makes him relatable and sympathetic despite his predatory nature. Zelda, the sassy zebra, also adds a lot of personality to the story.
* **Vivid imagery:**  Descriptions like "his heart pounding a dramatic rhythm against his ribs" and "a spray of water droplets flying" create a clear picture in the reader's mind.
* **Dialogue:** The dialogue is snappy and entertaining, particularly Zelda's lines.  "Nice mane trip, Leo. Did you get a perm?" is a great comedic line.
* **Pacing:** The story moves along at a good pace, keeping the reader engaged.
* **Satisfying ending:** The ending is humorous and leaves the reader with a smile.  Leo's resignation to sticking with tortoises is a funny and fitting conclusion.


Here are a few minor suggestions, though the story works perfectly well as it is:

* **Show, don't tell:**  While the story is generally well-written, there are a few places where you could show rather than tell. For example, instead of saying "his hunting skills… well, let's just say they were still a work in progress," you could show this through a brief anecdote of a previous failed hunting attempt.
* **Build up the tension:** You could slightly increase the tension before Leo's fall.  Perhaps describe him getting closer and closer to the zebras, his excitement building, before the comedic mishap.
* **Consider adding a little more conflict:** While the story works well as a humorous anecdote, you could consider adding a small element of conflict.  Perhaps Leo needs to catch something to prove himself to the other lions, or maybe he's particularly hungry. This could add another layer to the story.


Overall, it's a very enjoyable and well-written story.  I chuckled throughout!
"""
