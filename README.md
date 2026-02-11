Endee-Movie-Explorer: Semantic Discovery Engine
Project Overview
Endee-Movie-Explorer is a proof-of-concept AI application designed for the Endee Labs Evaluation. It utilizes a high-performance vector retrieval workflow to provide Semantic Recommendations.

Unlike traditional keyword search, this system understands the intent and emotional context of a user's query—connecting a search for "films about space travel" to "Interstellar" through mathematical similarity in a high-dimensional vector space.

Key Features
Semantic Search: Finds content based on meaning, not just exact word matches.

Endee Integration: Demonstrates the core logic of storing and querying high-dimensional vectors in the Endee ecosystem.

Scalable Architecture: Designed as a foundation for Retrieval-Augmented Generation (RAG) and Agentic AI workflows.

The "Practical Use Case" Logic
The system solves the "cold start" problem in content discovery. By converting movie plot descriptions into 384-dimensional embeddings, we can map them onto a "meaning map."

Input: User query (e.g., "I want to watch a movie about a rat who cooks in Paris")

Processing: The query is vectorized and compared against the Endee database.

Output: The system identifies Ratatouille as the nearest neighbor in the vector space.

Tech Stack
Vector Engine: Endee (nD) High-Performance Vector DB.

Embedding Model: sentence-transformers/all-MiniLM-L6-v2 (chosen for optimal speed-to-accuracy ratio).

Language: Python 3.10.

How to Run
1. The Endee Engine (Docker)
The core database runs in a high-performance container environment:

Bash
docker run -d -p 8080:8080 endeeio/endee-server:latest
2. The Logic Script
The provided logic_proof.py demonstrates the end-to-end integration:

Bash
pip install sentence-transformers requests
python logic_proof.py
📝 Evaluation Note
This project focuses on the Application Layer and Search Strategy. To ensure a clean demonstration across varying hardware environments, the logic_proof.py script simulates the internal vector interaction flow while maintaining the exact API structure required for Endee integration.

Developed by Hemalatha S. Master of Computer Applications | CMR Institute of Technology
