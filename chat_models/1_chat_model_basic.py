from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

# model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro"  
)

result = model.invoke("What is Machine Learning")
print("Full result:")
print(result)
print("Content only:")
print(result.content)

"""Full result:
content="Machine learning is a subfield of artificial intelligence (AI) that focuses on enabling computers to learn from data without being explicitly programmed.  Instead of relying on hard-coded rules, machine learning algorithms identify patterns, make predictions, and improve their performance over time based on the data they are exposed to.\n\nHere's a breakdown of key aspects:\n\n* **Data-driven:** Machine learning relies heavily on data.  The quality and quantity of the data significantly impact the performance of a machine learning model.\n* **Learning from experience:**  Algorithms learn by analyzing data and adjusting their internal parameters to improve their ability to perform a specific task. This learning process is often iterative.\n* **Generalization:** The goal is for a machine learning model to generalize well to new, unseen data.  This means it should be able to accurately predict or classify data it hasn't encountered during training.\n* **Automation:** Machine learning automates the process of finding patterns and making decisions, reducing the need for manual intervention.\n\n**Types of Machine Learning:**\n\n* **Supervised Learning:** The algorithm learns from labeled data (input data paired with correct output).  Common tasks include classification (e.g., spam detection) and regression (e.g., predicting house prices).\n* **Unsupervised Learning:** The algorithm learns from unlabeled data, discovering hidden patterns and structures. Common tasks include clustering (e.g., customer segmentation) and dimensionality reduction.\n* **Reinforcement Learning:** The algorithm learns through trial and error by interacting with an environment. It receives rewards or penalties based on its actions and aims to maximize its cumulative reward.  Common applications include robotics and game playing.\n\n**Key Concepts:**\n\n* **Training data:** The data used to train the machine learning model.\n* **Testing data:**  The data used to evaluate the performance of the trained model.\n* **Model:** The representation of the patterns learned by the algorithm.\n* **Algorithm:** The set of rules and calculations used to learn from the data.\n* **Features:** The individual measurable properties or characteristics of the data.\n\n\n**Examples of Machine Learning Applications:**\n\n* **Image recognition:** Identifying objects or faces in images.\n* **Natural language processing:** Understanding and generating human language.\n* **Recommendation systems:** Suggesting products or content to users.\n* **Fraud detection:** Identifying fraudulent transactions.\n* **Medical diagnosis:** Assisting doctors in diagnosing diseases.\n* **Self-driving cars:** Enabling cars to navigate and drive autonomously.\n\n\nIn essence, machine learning empowers computers to learn from data and make intelligent decisions without explicit programming, opening up a wide range of possibilities across various industries.\n" response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'safety_ratings': []} id='run-2ddbd2e2-6e2d-4bab-8308-9c78dd4df136-0' usage_metadata={'input_tokens': 4, 'output_tokens': 550, 'total_tokens': 554}
Content only:
Machine learning is a subfield of artificial intelligence (AI) that focuses on enabling computers to learn from data without being explicitly programmed.  Instead of relying on hard-coded rules, machine learning algorithms identify patterns, make predictions, and improve their performance over time based on the data they are exposed to.

Here's a breakdown of key aspects:

* **Data-driven:** Machine learning relies heavily on data.  The quality and quantity of the data significantly impact the performance of a machine learning model.
* **Learning from experience:**  Algorithms learn by analyzing data and adjusting their internal parameters to improve their ability to perform a specific task. This learning process is often iterative.
* **Generalization:** The goal is for a machine learning model to generalize well to new, unseen data.  This means it should be able to accurately predict or classify data it hasn't encountered during training.
* **Automation:** Machine learning automates the process of finding patterns and making decisions, reducing the need for manual intervention.

**Types of Machine Learning:**

* **Supervised Learning:** The algorithm learns from labeled data (input data paired with correct output).  Common tasks include classification (e.g., spam detection) and regression (e.g., predicting house prices).
* **Unsupervised Learning:** The algorithm learns from unlabeled data, discovering hidden patterns and structures. Common tasks include clustering (e.g., customer segmentation) and dimensionality reduction.
* **Reinforcement Learning:** The algorithm learns through trial and error by interacting with an environment. It receives rewards or penalties based on its actions and aims to maximize its cumulative reward.  Common applications include robotics and game playing.

**Key Concepts:**

* **Training data:** The data used to train the machine learning model.
* **Testing data:**  The data used to evaluate the performance of the trained model.
* **Model:** The representation of the patterns learned by the algorithm.
* **Algorithm:** The set of rules and calculations used to learn from the data.
* **Features:** The individual measurable properties or characteristics of the data.


**Examples of Machine Learning Applications:**

* **Image recognition:** Identifying objects or faces in images.
* **Natural language processing:** Understanding and generating human language.
* **Recommendation systems:** Suggesting products or content to users.
* **Fraud detection:** Identifying fraudulent transactions.
* **Medical diagnosis:** Assisting doctors in diagnosing diseases.
* **Self-driving cars:** Enabling cars to navigate and drive autonomously.


In essence, machine learning empowers computers to learn from data and make intelligent decisions without explicit programming, opening up a wide range of possibilities across various industries.
"""