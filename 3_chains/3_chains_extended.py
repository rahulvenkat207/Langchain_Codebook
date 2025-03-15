from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
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

# Define additional processing steps using RunnableLambda
uppercase_output = RunnableLambda(lambda x: x.upper()) # type: ignore
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}") # type: ignore

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser() | uppercase_output | count_words

# Run the chain
result = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
print(result)

"""Word count: 72
1. WHY DON'T SHARKS ATTACK LAWYERS?  PROFESSIONAL COURTESY.

2. WHAT'S THE DIFFERENCE BETWEEN A GOOD LAWYER AND A GREAT LAWYER? A GOOD LAWYER KNOWS THE LAW. A GREAT LAWYER KNOWS THE JUDGE.

3. A LAWYER DIES AND GOES TO HEAVEN. ST. PETER SAYS, "WE'VE NEVER HAD A LAWYER HERE BEFORE. WE'RE NOT SURE WHAT TO DO WITH YOU." THE LAWYER SAYS, "NO PROBLEM, JUST LET ME IN AND I'LL FILE A LAWSUIT."
"""