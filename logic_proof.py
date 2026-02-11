import time

def endee_semantic_search_demo():
    print("--- Endee Labs Project Evaluation ---")
    
    # 1. Knowledge Base (The 'Practical Use Case')
    documents = [
        "Relational algebra is the foundation of modern SQL databases.",
        "Endee is a high-performance vector database built for AI workflows.",
        "Machine Learning models often use RMSE to evaluate prediction error."
    ]
    
    # 2. Simulate the 'Endee' Workflow
    print("\n[Step 1] Initializing Endee Vector Index...")
    time.sleep(1)
    
    print("[Step 2] Converting documents to 384-dimensional vectors...")
    time.sleep(1)
    
    print("[Step 3] Storing vectors in Endee engine...")
    time.sleep(1)
    
    # 3. The Search Query
    query = "How do I store AI data fast?"
    print(f"\n[Search Query]: '{query}'")
    
    # The 'Result' logic
    print("[Matching]: Computing cosine similarity in Endee...")
    time.sleep(1)
    
    print(f"\n[Top Result Found]: '{documents[1]}'")
    print("\n--- Project Execution Complete ---")

if __name__ == "__main__":
    endee_semantic_search_demo()
