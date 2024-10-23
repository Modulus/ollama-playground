import qdrant_client
from qdrant_client.models import Batch
from qdrant_client import models
import ollama
import random
# Initialize Ollama model

## Using fast embeddings insertion

# Generate embeddings for niche applications
documents = [
    "Taking place in San Francisco, USA, from the 10th to the 12th of June, 2024, the Global Developers Conference is the annual gathering spot for developers worldwide, offering insights into software engineering, web development, and mobile applications.",
    "The AI Innovations Summit, scheduled for 15-17 September 2024 in London, UK, aims at professionals and researchers advancing artificial intelligence and machine learning.",
    "Berlin, Germany will host the CyberSecurity World Conference between November 5th and 7th, 2024, serving as a key forum for cybersecurity professionals to exchange strategies and research on threat detection and mitigation.",
    "Data Science Connect in New York City, USA, occurring from August 22nd to 24th, 2024, connects data scientists, analysts, and engineers to discuss data science's innovative methodologies, tools, and applications.",
    "Set for July 14-16, 2024, in Tokyo, Japan, the Frontend Developers Fest invites developers to delve into the future of UI/UX design, web performance, and modern JavaScript frameworks.",
    "The Blockchain Expo Global, happening May 20-22, 2024, in Dubai, UAE, focuses on blockchain technology's applications, opportunities, and challenges for entrepreneurs, developers, and investors.",
    "Singapore's Cloud Computing Summit, scheduled for October 3-5, 2024, is where IT professionals and cloud experts will convene to discuss strategies, architectures, and cloud solutions.",
    "The IoT World Forum, taking place in Barcelona, Spain from December 1st to 3rd, 2024, is the premier conference for those focused on the Internet of Things, from smart cities to IoT security.",
    "Los Angeles, USA, will become the hub for game developers, designers, and enthusiasts at the Game Developers Arcade, running from April 18th to 20th, 2024, to showcase new games and discuss development tools.",
    "The TechWomen Summit in Sydney, Australia, from March 8-10, 2024, aims to empower women in tech with workshops, keynotes, and networking opportunities.",
    "Seoul, South Korea's Mobile Tech Conference, happening from September 29th to October 1st, 2024, will explore the future of mobile technology, including 5G networks and app development trends.",
    "The Open Source Summit, to be held in Helsinki, Finland from August 11th to 13th, 2024, celebrates open source technologies and communities, offering insights into the latest software and collaboration techniques.",
    "Vancouver, Canada will play host to the VR/AR Innovation Conference from June 20th to 22nd, 2024, focusing on the latest in virtual and augmented reality technologies.",
    "Scheduled for May 5-7, 2024, in London, UK, the Fintech Leaders Forum brings together experts to discuss the future of finance, including innovations in blockchain, digital currencies, and payment technologies.",
    "The Digital Marketing Summit, set for April 25-27, 2024, in New York City, USA, is designed for marketing professionals and strategists to discuss digital marketing and social media trends.",
    "EcoTech Symposium in Paris, France, unfolds over 2024-10-09 to 2024-10-11, spotlighting sustainable technologies and green innovations for environmental scientists, tech entrepreneurs, and policy makers.",
    "Set in Tokyo, Japan, from 16th to 18th May '24, the Robotic Innovations Conference showcases automation, robotics, and AI-driven solutions, appealing to enthusiasts and engineers.",
    "The Software Architecture World Forum in Dublin, Ireland, occurring 22-24 Sept 2024, gathers software architects and IT managers to discuss modern architecture patterns.",
    "Quantum Computing Summit, convening in Silicon Valley, USA from 2024/11/12 to 2024/11/14, is a rendezvous for exploring quantum computing advancements with physicists and technologists.",
    "From March 3 to 5, 2024, the Global EdTech Conference in London, UK, discusses the intersection of education and technology, featuring e-learning and digital classrooms.",
    "Bangalore, India's NextGen DevOps Days, from 28 to 30 August 2024, is a hotspot for IT professionals keen on the latest DevOps tools and innovations.",
    "The UX/UI Design Conference, slated for April 21-23, 2024, in New York City, USA, invites discussions on the latest in user experience and interface design among designers and developers.",
    "Big Data Analytics Summit, taking place 2024 July 10-12 in Amsterdam, Netherlands, brings together data professionals to delve into big data analysis and insights.",
    "Toronto, Canada, will see the HealthTech Innovation Forum from June 8 to 10, '24, focusing on technology's impact on healthcare with professionals and innovators.",
    "Blockchain for Business Summit, happening in Singapore from 2024-05-02 to 2024-05-04, focuses on blockchain's business applications, from finance to supply chain.",
    "Las Vegas, USA hosts the Global Gaming Expo from October 18th to 20th, 2024, a premiere event for game developers, publishers, and enthusiasts.",
    "The Renewable Energy Tech Conference in Copenhagen, Denmark, from 2024/09/05 to 2024/09/07, discusses renewable energy innovations and policies.",
    "Set for 2024 Apr 9-11 in Boston, USA, the Artificial Intelligence in Healthcare Summit gathers healthcare professionals to discuss AI's healthcare applications.",
    "Nordic Software Engineers Conference, happening in Stockholm, Sweden from June 15 to 17, 2024, focuses on software development in the Nordic region.",
    "The International Space Exploration Symposium, scheduled in Houston, USA from 2024-08-05 to 2024-08-07, invites discussions on space exploration technologies and missions."
]

# embeddings = ollama.embeddings(model="nomic-embed-text", prompt="dsfad")["embedding"]

# Initialize Qdrant client
client = qdrant_client.QdrantClient(host="localhost", port=6333)

name = "demo"

# try:
#     client.get_collection(collection_name=name)
# except qdrant_client.http.exceptions.UnexpectedResponse as e:
#     response = client.create_collection(collection_name=name,
#                                             vectors_config=models.VectorParams(
#                                                 size=384,
#                                                 distance=models.Distance.COSINE,

#                                             )
#                                         )

# Upsert the embedding into Qdrant
# client.add will use fast embeddings insertion
client.add(
    collection_name=name,
    documents=documents,
    # metadata=[{"source": "ollama"}],
    ids=range(len(documents))
)

questions = [
                "What happens May 5-7 in 2024", 
                "What is the AI Innovations Summit?", 
                "When is the Global EdTech Conference?", 
                "Where is the Renewable Energy Tech Conference?", 
                "Who attends the Blockchain Expo Global?", 
                "Why attend the Digital Marketing Summit?", 
                "How to participate in the Global Developers Conference?",
                "What happens in May 2024? Give answers as a list",
                "What events are going on in 2024? Give answers as a list"
                ]

prompt = random.choice(questions) #questions[len(questions)-1] #

print(f"Sending prompt: {prompt}")

print("\n\n")

# response = ollama.embeddings(
#   prompt=prompt,
#   model="nomic-embed-text" #mxbai-embed-large
# )


search_result = client.query(
    collection_name=name,
    query_text=prompt
)
print(f"Found matching documents: {len(search_result)}")

result = [entry.document for entry in search_result]

print(f"Extracted raw documents from results: {result}")
print("\n\n")
print("Sending promt to model")
print("\n\n")

output = ollama.generate(
    prompt=f"Using data: {result}. Respond to this prompt: {prompt}",
    model="llama3.2",
)
print("\n\nGot response from model: ")
print(output["response"])