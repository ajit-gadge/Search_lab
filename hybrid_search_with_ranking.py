== Hybrid Search with Ranking. Full text search to search for keyword and Semantic search to do near by search with ranking ========

import psycopg2
from sentence_transformers import SentenceTransformer, CrossEncoder
import itertools
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers.tokenization_utils_base")


# Load the models. Use 'all-MiniLM-L6-v2' as generliase sentance trasnformer and crossencoder 'ms-macro-MiniLM-L-6-v2' for ranking as  
semantic_model = SentenceTransformer('all-MiniLM-L6-v2')
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Establish the connection to the PostgreSQL database
conn = psycopg2.connect(
    host="",
    database="",
    user="",
    password=""
)
cursor = conn.cursor()

# Function to re-rank search results
def rerank(query, results):
    # Deduplicate
    results = list(set(itertools.chain(*results)))

    # Re-rank using CrossEncoder
    scores = cross_encoder.predict([(query, item[1]) for item in results])
    ranked_results = [v for _, v in sorted(zip(scores, results), reverse=True)]
    
    return ranked_results

# Perform semantic search
def semantic_search(cursor, query_embedding):
    query_embedding_list = query_embedding.tolist()  # Convert numpy.ndarray to list
    cursor.execute('SELECT id, body FROM articles ORDER BY embeddings <=> %s::vector LIMIT 5', (query_embedding_list,))
    return cursor.fetchall()

# Perform keyword search
def keyword_search(cursor, query):
    cursor.execute("SELECT id, body FROM articles, plainto_tsquery('english', %s) query WHERE to_tsvector('english', body) @@ query ORDER BY ts_rank_cd(to_tsvector('english', body), query) DESC LIMIT 5", (query,))
    return cursor.fetchall()

# Function to perform hybrid search with re-ranking
def hybrid_search_with_rerank(cursor, query):
    # Generate the embedding for the query
    query_embedding = semantic_model.encode(query)

    # Perform searches
    semantic_results = semantic_search(cursor, query_embedding)
    keyword_results = keyword_search(cursor, query)

    # Re-rank the combined results
    ranked_results = rerank(query, [semantic_results, keyword_results])

    return ranked_results

# Prompt for the search query
query = input("Enter your search query: ")

# Execute the hybrid search with re-ranking
ranked_results = hybrid_search_with_rerank(cursor, query)

# Print the ranked results
for result in ranked_results:
    print(f"ID: {result[0]}, Body: {result[1]}")

# Close the connection
cursor.close()
conn.close()

