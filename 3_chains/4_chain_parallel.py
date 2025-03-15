from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}."),
    ]
)


# Define pros analysis step
def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the pros of these features.",
            ),
        ]
    )
    return pros_template.format_prompt(features=features)


# Define cons analysis step
def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the cons of these features.",
            ),
        ]
    )
    return cons_template.format_prompt(features=features)


# Combine pros and cons into a final review
def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\n\nCons:\n{cons}"


# Simplify branches with LCEL
pros_branch_chain = (
    RunnableLambda(lambda x: analyze_pros(x)) | model | StrOutputParser()
)

cons_branch_chain = (
    RunnableLambda(lambda x: analyze_cons(x)) | model | StrOutputParser()
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = (
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain})
    | RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"])) # type: ignore
)

# Run the chain
result = chain.invoke({"product_name": "MacBook Pro"})

# Output
print(result)

"""Pros:
## MacBook Pro (Late 2023) - Pros based on Features:

**Performance & Power:**

* **Blazing Fast Performance:** The M2 Pro and M2 Max chips offer exceptional performance, making demanding tasks like video editing, 3D rendering, and software development incredibly smooth and efficient. The M2 Max stands out with its superior GPU performance for graphics-intensive workloads.
* **Industry-Leading Efficiency:** Apple silicon's architecture delivers remarkable performance per watt, resulting in longer battery life and cooler operation compared to competing laptops.
* **Unified Memory Architecture:**  Streamlines multitasking and resource allocation, boosting overall system performance and responsiveness.
* **Fast Storage:**  The SSD ensures rapid boot times, application loading, and file transfers, minimizing downtime.    

**Display & Design:**

* **Stunning Visuals:** The Liquid Retina XDR display with mini-LED technology delivers exceptional contrast, vibrant colors, and high brightness, creating an immersive viewing experience.
* **Smooth Scrolling & Animations:** ProMotion technology with adaptive refresh rates up to 120Hz provides a fluid and responsive user interface.
* **Premium Build Quality:** The aluminum unibody design exudes durability and sophistication.
* **Maximized Screen Real Estate:** Thin bezels allow for a larger display within a compact footprint, enhancing productivity and immersion.
* **Choice of Sizes:** The 14-inch and 16-inch options cater to different needs and preferences regarding portability and screen size.

**Connectivity & Input:**

* **Versatile Connectivity:**  Multiple Thunderbolt 4 ports offer high-speed data transfer, charging, and external display support. The inclusion of an HDMI port and SDXC card slot (M2 Max models) further expands connectivity options for professionals.
* **MagSafe 3:** The magnetic charging port provides a secure connection while also preventing accidental drops due to tripping over the cable.
* **High-Quality Audio:** The improved headphone jack with support for high-impedance headphones caters to audiophiles, while the six-speaker sound system with force-cancelling woofers delivers an immersive audio experience.
* **Excellent Input Devices:** The backlit Magic Keyboard offers a comfortable typing experience, and the large Force Touch trackpad provides precise and responsive control.

**Other Features:**

* **Improved Webcam:** The 1080p FaceTime HD camera delivers higher-quality video for video conferencing and online meetings.
* **Superior Microphone Array:**  The studio-quality three-mic array ensures clear voice recording for podcasts, voiceovers, and online calls.
* **All-Day Battery Life:**  Provides ample power for extended use, reducing the need for frequent charging.
* **macOS Ecosystem:** Seamless integration with other Apple devices and services, along with access to a vast library of optimized applications.


These pros paint a picture of a powerful, versatile, and well-designed professional laptop. The MacBook Pro (Late 2023) offers top-tier performance, a stunning display, and a range of features tailored for demanding users.


Cons:
While the late 2023 MacBook Pro models offer impressive features, some potential downsides exist depending on individual needs and priorities:

**Price:**

* **High Cost:** The MacBook Pro, especially in higher configurations with the M2 Max chip and larger storage options, is a premium product with a premium price tag. This can be a significant barrier for budget-conscious consumers.

**Design and Functionality:**

* **The Notch:** While the notch houses an improved webcam, some users find it intrusive and distracting, especially in full-screen mode.
* **Limited Port Selection (on M2 Pro models):** While the M2 Max models offer an SDXC card slot, the M2 Pro configurations rely solely on Thunderbolt/USB-C ports. This may necessitate the use of dongles and adapters for users who frequently connect to various peripherals.
* **Keyboard and Trackpad Issues (potential):** While generally well-regarded, the butterfly keyboard's past reliability issues may linger as a concern for some users, even with the newer Magic Keyboard.  Similarly, the large trackpad, while appreciated by many, can be prone to accidental palm rejection issues for some users.
* **Repair Complexity and Cost:** Apple's tight integration of components and use of proprietary parts can make repairs more complex and expensive than with other laptops.

**Performance and Software:**

* **Gaming Limitations:** While the M2 Pro and M2 Max offer impressive GPU performance, macOS still lags behind Windows in terms of game availability and optimization.  Not all AAA titles are available or perform optimally on macOS.        
* **Software Compatibility (niche professional software):** While the transition to Apple Silicon has been generally smooth, some niche professional software may still lack native Apple Silicon support, requiring Rosetta 2 emulation which can impact performance.
* **Unified Memory Limitations (for extreme workloads):** While unified memory is beneficial in most cases, for extremely demanding workloads requiring massive amounts of VRAM, a dedicated GPU with its own memory pool might offer better performance.

**Other Considerations:**

* **Dongle Life (especially on M2 Pro):**  The reliance on USB-C/Thunderbolt necessitates dongles for many common peripherals, which can be inconvenient and add to the overall cost.
* **Ecosystem Lock-in:**  Investing in the Apple ecosystem can create a sense of lock-in, making it more difficult to switch to other platforms in the future.


It's crucial to weigh these potential drawbacks against the MacBook Pro's strengths to determine if it's the right machine for your specific needs and budget.  For many professionals, the performance and ecosystem benefits outweigh the costs and limitations, but it's important to be aware of these potential downsides before making a purchase.
"""