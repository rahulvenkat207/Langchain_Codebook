from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
#Prompt with single placeholder
template = "Tell me a joke about {topic}."

prompt_template = ChatPromptTemplate.from_template(template)


prompt = prompt_template.invoke({"topic":"Lion"})
result = model.invoke(prompt)
print("--------")
print(result.content)


#Prompt with multiple placeholder
template_multiple = """You are helpful assistant.
Human:Tell me a {adjective} story about a {animal}.
Assistant:"""

prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective":"funny","animal":"Lion"})
result = model.invoke(prompt)
print("--------")
print(result.content)


# prompt with System and  Human messages(using tuples)

messages = [
    ("system", "you are a comedian who tells joke about {topic}"),
    ("human", "tell me {no} of jokes")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic":"Poilce","no":3})
result = model.invoke(prompt)
print("--------")
print(result.content)


"""--------
What's a lion's favorite Christmas carol?

Jungle Bells!

--------
Leo the lion was having an existential crisis.  He was the king of the jungle, sure, but what did that even *mean* these days?  The zebras had unionized, the giraffes had started a podcast about mindful chewing, and the meerkats were all obsessed with some new cryptocurrency called "BugCoin."  It was exhausting.

Leo decided he needed a vacation.  A real getaway.  He booked himself an all-inclusive trip to the "Serengeti Sands Resort and Spa," promising himself massages, mango smoothies, and absolutely NO zebra negotiations.

The resort, however, wasn't quite as advertised.  The "sands" were more like gritty dirt, the "spa" was a muddy puddle frequented by hippos, and the "all-inclusive" buffet consisted mostly of wilted lettuce.  Leo was fuming.

The final straw came during the "Jungle Jamboree" evening entertainment.  A particularly enthusiastic warthog DJ was blasting ear-splitting techno music, and a group of baboons were doing an interpretative dance routine that seemed to be about the plight of the dung beetle.

Leo, overwhelmed, decided to take matters into his own paws. He marched up to the DJ booth, roared mightily (which, admittedly, did momentarily clear the dance floor), and grabbed the microphone.

"Right!" he bellowed, his voice cracking slightly. "Who here wants to hear a *real* roar?"

The crowd, expecting a terrifying display of primal power, went silent.  Leo took a deep breath, puffed out his chest, and... let out a pathetic squeak.  He'd forgotten that he'd lost his voice from complaining about the lettuce.

The silence hung in the air for a beat, then the entire jungle erupted in laughter.  Even the dung beetles seemed to be chuckling.  Leo, mortified, slunk off the stage, his tail between his legs.  He decided to stick to roaring at zebras.  At least they took him seriously.

--------
1.  Why did the police officer bring a ladder to work?  He wanted to go undercover.

2.  A police officer pulls a guy over for speeding.  He walks up to the car and says, "Papers."  The driver replies, "Scissors, I win!"  The officer says, "No, really, can I see your license and registration?" The driver says, "Rock, I win again!"  Finally, exasperated, the officer says, "Sir, this isn't a game!" The driver replies, "Oh, right.  Sorry, what were we playing?"

3.  My wife told me to stop impersonating a police officer.  I said, "You have the right to remain silent."
"""