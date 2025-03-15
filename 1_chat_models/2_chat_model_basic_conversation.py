from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

# Loading environment varibale
load_dotenv()

#createa chatgoole model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro" )

#System Message -> Messages for priming AI behaviour
#Human Messages -> Message from a human to the AI model
messages = [
  SystemMessage(content="Solve the following  math problem"),
  HumanMessage(content= "What is 72 divided by 9"),
]

result = model.invoke(messages)
print(f"Answer from AI model: {result.content}")

"""Answer from AI model: 72 divided by 9 is 8."""

#AI Message-> Message from AI
messages = [
  SystemMessage(content="Solve the following  math problem"),
  HumanMessage(content= "What is 72 divided by 9"),
  AIMessage(content="72 divided by 9 is 8."),
  HumanMessage(content= "What is 72 divided by 12"),
]

result = model.invoke(messages)
print(f"Answer from AI model:{result.content} ")

"""Answer from AI model:72 divided by 12 is 6."""