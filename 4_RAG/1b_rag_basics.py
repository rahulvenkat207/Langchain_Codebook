import os

from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Define the embedding model
embeddings =  GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Load the existing vector store with the embedding function
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings)

# Define the user's question
query = "Who is Odysseus' wife?"

# Retrieve relevant documents based on the query
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.5},
)
relevant_docs = retriever.invoke(query)

# Display the relevant results with metadata
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")

"""-- Relevant Documents ---
Document 1:
daughter of the magician Atlas, who looks after the bottom of the
ocean, and carries the great columns that keep heaven and earth
asunder. This daughter of Atlas has got hold of poor unhappy Ulysses,
and keeps trying by every kind of blandishment to make him forget his
home, so that he is tired of life, and thinks of nothing but how he may
once more see the smoke of his own chimneys. You, sir, take no heed of
this, and yet when Ulysses was before Troy did he not propitiate you
with many a burnt sacrifice? Why then should you keep on being so angry
with him?”
And Jove said, “My child, what are you talking about? How can I forget
Ulysses than whom there is no more capable man on earth, nor more
liberal in his offerings to the immortal gods that live in heaven? Bear
in mind, however, that Neptune is still furious with Ulysses for having
blinded an eye of Polyphemus king of the Cyclopes. Polyphemus is son to
Neptune by the nymph Thoosa, daughter to the sea-king Phorcys;

Source: C:/C1X-intern/Langchain_study/4_Rag/books/odyssey.txt

Document 2:
such deeds! But my heart is rent for wise Odysseus, the hapless
    one, who far from his friends this long while suffereth affliction
    in a sea-girt isle, where is the navel of the sea, a woodland isle,
    and therein a goddess hath her habitation, the daughter of the
    wizard Atlas, who knows the depths of every sea, and himself
    upholds the tall pillars which keep earth and sky asunder. His
    daughter it is that holds the hapless man in sorrow: and ever with
    soft and guileful tales she is wooing him to forgetfulness of
    Ithaca. But Odysseus yearning to see if it were but the smoke leap
    upwards from his own land, hath a desire to die. As for thee, thine
    heart regardeth it not at all, Olympian! What! Did not Odysseus by
    the ships of the Argives make thee free offering of sacrifice in
    the wide Trojan land? Wherefore wast thou then so wroth with him, O
    Zeus?’
The “Odyssey” (as every one knows) abounds in passages borrowed from

Source: C:/C1X-intern/Langchain_study/4_Rag/books/odyssey.txt

Document 3:
Tell me, Muse, of that man, so ready at need, who wandered far and
wide, after he had sacked the sacred citadel of Troy, and many were the
men whose towns he saw and whose mind he learnt, yea, and many the woes
he suffered in his heart on the deep, striving to win his own life and
the return of his company. Nay, but even so he saved not his company,
though he desired it sore. For through the blindness of their own
hearts they perished, fools, who devoured the oxen of Helios Hyperion:
but the god took from them their day of returning. Of these things,
goddess, daughter of Zeus, whencesoever thou hast heard thereof,
declare thou even unto us.
    Now all the rest, as many as fled from sheer destruction, were at
    home, and had escaped both war and sea, but Odysseus only, craving
    for his wife and for his homeward path, the lady nymph Calypso
    held, that fair goddess, in her hollow caves, longing to have him
    for her lord. But when now the year had come in the courses of the

Source: C:/C1X-intern/Langchain_study/4_Rag/books/odyssey.txt"""