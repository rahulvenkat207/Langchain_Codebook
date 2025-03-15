from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

chat_history = []

system_message = SystemMessage(content="You are a helpful AI assistant")
chat_history.append(system_message) #adding system messge to chat history

#chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))#addding human message
    
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))#addding aig message

    print(f"AI : {response}")

print("---- Message History ----")
print(chat_history)

"""You: Define AI in 100 words
AI : Artificial intelligence (AI) involves creating machines capable of performing tasks that typically require human intelligence.  This includes learning from experience, adapting to new information, understanding and responding to language, recognizing patterns, solving problems, and making decisions. AI systems utilize algorithms and computational models to simulate cognitive functions, ranging from basic tasks like image recognition to complex reasoning and problem-solving.  Different approaches exist, including machine learning, deep learning, and rule-based systems, each with its own strengths and applications.  AI aims to automate processes, enhance decision-making, and create new possibilities across various fields.

You: how ai automates the process
AI : AI automates processes by mimicking human actions and decision-making using algorithms and models. Here's a breakdown:

1. **Data Input:** AI systems ingest structured or unstructured data relevant to the process being automated. This data can come from various sources like databases, sensors, or online platforms.

2. **Pattern Recognition & Analysis:** Using techniques like machine learning, AI algorithms analyze the input data to identify patterns, trends, and anomalies. This allows the system to understand the relationships between different variables and how they influence the process.

3. **Decision Making & Action:** Based on the identified patterns, the AI system makes decisions according to pre-defined rules or learned patterns. This can involve anything from sorting items, routing requests, generating reports, or even controlling physical machinery.

4. **Learning & Improvement:** Many AI systems, especially those using machine learning, can learn from their experiences. As they process more data and make more decisions, they refine their models and improve their accuracy and efficiency over time.  This iterative process allows them to adapt to changing conditions and optimize the automated process.     

5. **Integration with Existing Systems:** AI automation tools are often integrated with existing software and hardware systems. This allows them to seamlessly take over repetitive tasks, trigger actions in other systems, and provide data-driven insights to human operators.

**Examples of AI-powered automation:**

* **Robotic Process Automation (RPA):** Automates repetitive tasks like data entry and form filling.
* **Chatbots:** Automate customer service interactions by answering questions and resolving simple issues.
* **Predictive Maintenance:**  Predicts equipment failures and schedules maintenance proactively, minimizing downtime.  
* **Fraud Detection:** Automatically identifies potentially fraudulent transactions based on historical data.

By taking over repetitive, data-heavy tasks, AI frees up human workers to focus on more complex and creative endeavors.  It also increases efficiency, reduces errors, and enables faster decision-making in many industries.

You: is it complex, data- heavy tasks
AI : AI can handle both complex and data-heavy tasks, but they represent different aspects of its capabilities:

* **Data-heavy tasks:** These tasks involve processing and analyzing large volumes of data, often beyond human capacity. AI excels at this due to its computational power and ability to identify patterns in vast datasets. Examples include:  
    * Processing millions of transactions for fraud detection.
    * Analyzing customer behavior data for personalized recommendations.
    * Sifting through scientific data to identify research trends.

* **Complex tasks:** These tasks require higher-level cognitive abilities like reasoning, problem-solving, and decision-making in intricate scenarios.  While still under development, AI is making strides in this area. Examples include:     
    * Developing strategies for complex games like Go or chess.
    * Diagnosing medical conditions based on symptoms and medical history.
    * Designing new drugs or materials using generative AI.


Often, these two aspects overlap.  A complex task might also be data-heavy, requiring the AI to analyze vast amounts of information to make informed decisions. For instance, autonomous driving involves both complex decision-making in real-time and processing massive amounts of sensor data.

So, while AI is inherently suited to data-heavy tasks, its ability to handle complexity is continuously evolving and expanding.  It's not limited to one or the other.

You: exit
---- Message History ----
[SystemMessage(content='You are a helpful AI assistant'), HumanMessage(content='Define AI in 100 words'), AIMessage(content='Artificial intelligence (AI) involves creating machines capable of performing tasks that typically require human intelligence.  This includes learning from experience, adapting to new information, understanding and responding to language, recognizing patterns, solving problems, and making decisions. AI systems utilize algorithms and computational models to simulate cognitive functions, ranging from basic tasks like image recognition to complex reasoning and problem-solving.  Different approaches exist, including machine learning, deep learning, and rule-based systems, each with its own strengths and applications.  AI aims to automate processes, enhance decision-making, and create new possibilities across various fields.\n'), HumanMessage(content='how ai automates the process'), AIMessage(content="AI automates processes by mimicking human actions and decision-making using algorithms and models. Here's a breakdown:\n\n1. **Data Input:** AI systems ingest structured or unstructured data relevant to the process being automated. This data can come from various sources like databases, sensors, or online platforms.\n\n2. **Pattern Recognition & Analysis:** Using techniques like machine learning, AI algorithms analyze the input data to identify patterns, trends, and anomalies. This allows the system to understand the relationships between different variables and how they influence the process.\n\n3. **Decision Making & Action:** Based on the identified patterns, the AI system makes decisions according to pre-defined rules or learned patterns. This can involve anything from sorting items, routing requests, generating reports, or even controlling physical machinery.\n\n4. **Learning & Improvement:** Many AI systems, especially those using machine learning, can learn from their experiences. As they process more data and make more decisions, they refine their models and improve their accuracy and efficiency over time.  This iterative process allows them to adapt to changing conditions and optimize the automated process.\n\n5. **Integration with Existing Systems:** AI automation tools are often integrated with existing software and hardware systems. This allows them to seamlessly take over repetitive tasks, trigger actions in other systems, and provide data-driven insights to human operators.\n\n**Examples of AI-powered automation:**\n\n* **Robotic Process Automation (RPA):** Automates repetitive tasks like data entry and form filling.\n* **Chatbots:** Automate customer service interactions by answering questions and resolving simple issues.\n* **Predictive Maintenance:**  Predicts equipment failures and schedules maintenance proactively, minimizing downtime.\n* **Fraud Detection:** Automatically identifies potentially fraudulent transactions based on historical data.\n\nBy taking over repetitive, data-heavy tasks, AI frees up human workers to focus on more complex and creative endeavors.  It also increases efficiency, reduces errors, and enables faster decision-making in many industries.\n"), HumanMessage(content='is it complex, data- heavy tasks'), AIMessage(content="AI can handle both complex and data-heavy tasks, but they represent different aspects of its capabilities:\n\n* **Data-heavy tasks:** These tasks involve processing and analyzing large volumes of data, often beyond human capacity. AI excels at this due to its computational power and ability to identify patterns in vast datasets. Examples include:\n    * Processing millions of transactions for fraud detection.\n    * Analyzing customer behavior data for personalized recommendations.\n    * Sifting through scientific data to identify research trends.\n\n* **Complex tasks:** These tasks require higher-level cognitive abilities like reasoning, problem-solving, and decision-making in intricate scenarios.  While still under development, AI is making strides in this area. Examples include:\n    * Developing strategies for complex games like Go or chess.\n    * Diagnosing medical conditions based on symptoms and medical history.\n    * Designing new drugs or materials using generative AI.\n\n\nOften, these two aspects overlap.  A complex task might also be data-heavy, requiring the AI to analyze vast amounts of information to make informed decisions. For instance, autonomous driving involves both complex decision-making in real-time and processing massive amounts of sensor data.\n\nSo, while AI is inherently suited to data-heavy tasks, its ability to handle complexity is continuously evolving and expanding.  It's not limited to one or the other.\n")]"""
                        