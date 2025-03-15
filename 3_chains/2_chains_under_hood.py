from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages())) # type: ignore
parse_output = RunnableLambda(lambda x: x.content) # type: ignore

# (equivalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Run the chain
response = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
print(response)
"""1.  Why don't sharks attack lawyers?  Professional courtesy.

2.  What's the difference between a good lawyer and a great lawyer?  A good lawyer knows the law. A great lawyer knows the judge.

3. A lawyer is standing at the pearly gates. St. Peter looks at him and says, "You've lived a long life, but I see no good deeds that would let you into Heaven." The lawyer replies, "Well, I did get that guy off on a double homicide charge." St. Peter checks his notes. "Ah yes, I see that. But that was overturned on appeal." The lawyer smiles, "Not yet."    
"""