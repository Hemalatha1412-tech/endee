#Endee-Search: Semantic Academic Assistant
A project-based evaluation for Endee Labs demonstrating high-performance vector retrieval.

##Practical Use Case: Semantic Research Search
This project demonstrates how **Endee** can be used as a vector database for a Research Paper Search engine. Instead of matching keywords, it matches the *intent* of the query using mathematical similarity.

###Core Features:
- **Vector Retrieval:** Utilizing Endee's optimized C++ engine for low-latency search.
- **RAG Architecture:** Provides the foundation for Retrieval-Augmented Generation workflows.
- **Semantic Mapping:** Maps natural language queries to high-dimensional document embeddings.

##Project Structure
- `logic_proof.py`: A Python implementation demonstrating the database interaction logic.
- `Endee Engine`: The core high-performance vector database.

##How to Run
1. Start the Endee Docker container:
   `docker run -p 8080:8080 endeeio/endee-server:latest`
2. Execute the logic script:
   `python logic_proof.py`
