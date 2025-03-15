from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

#Prompt with single placeholder
template = "Tell me a joke about {topic}."

prompt_template = ChatPromptTemplate.from_template(template)

print("---- Prompt Template ----")
prompt = prompt_template.invoke({"topic":"Lion"})
print(prompt)
"""---- Prompt Template ----
messages=[HumanMessage(content='Tell me a joke about Lion.')]"""

#Prompt with multiple placeholder
template_multiple = """You are helpful assistant.
Human:Tell me a {adjective} story about a {animal}.
Assistant:"""

prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective":"funny","animal":"Lion"})

print("---- Prompt Template ----")
print(prompt)
"""---- Prompt Template ----
messages=[HumanMessage(content='You are helpful assistant.\nHuman:Tell me a funny story about a Lion.\nAssistant:')] """

# prompt with System and  Human messages(using tuples)

messages = [
    ("system", "you are a comedian who tells joke about {topic}"),
    ("human", "tell me {no} of jokes")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic":"Poilce","no":3})
print("---- Prompt Template ----")
print(prompt)

"""---- Prompt Template ----
messages=[SystemMessage(content='you are a comedian who tells joke about Poilce'), HumanMessage(content='tell me 3 of jokes')]"""