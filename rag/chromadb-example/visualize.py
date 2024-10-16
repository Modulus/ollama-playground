import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset for visualization
doc_embeddings = np.array(embeddings)
query_embedding = np.array(query_embedding)

# Plot the document embeddings
plt.scatter(doc_embeddings[:, 0], doc_embeddings[:, 1], color='blue', label='Documents')
plt.scatter(query_embedding[0], query_embedding[1], color='red', label='Query')
plt.legend()
plt.title('Document and Query Embeddings')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()
