# Search_lab

Here are a few simple examples that showcase Standard Search, Full-text Search, Semantic Search and Hybrid Search.


This Search Lab will help to create a demo on various capabilities of Search in PostgreSQL and explore the differences among those. This lab also intended to showcase how Hybrid search can be used for various purposes.

Step 1: Create the Sample table in PostgreSQL with pgvector as an extension that enables the creation of a vector as Data Type. Use the “Data Load” script to add sample sentences with simple text to Postgresql.

Step 2:  Once data is loaded, we can do simple keyword-based searching, which is a standard search. Let’s take a simple standard search. It works well if I like searching a simple world like “PostgreSQL”. Use the “Standard_Search” script to do a demo.

Step 3: look at the full-text search, which understands the word combination, conjunction, stemming, etc.  Use the “full-text Search” file for this example. So, if you look at the tsvector column data, it tokenises the word here, including how many times that particular word comes and positions. It also understands conjunction words, such as “&” and stemming. Let's search our conjunction word “Postgresql & vector”. This example provides me with two results: Postgresql as word and vector as word, regardless of their position, frequency of the word, and stemming and stop word.

In the dictionary, you can also customise stop words like a, the, an, are, etc., for further advanced tunning. You can further customise this for advanced trigram similarity with the extension pg_trgm.
Fulltext search also provides lexemes-based weightage and ranking. One can customise this weightage as well. So you can see the ranking of the given words on my screen.

Step 4: Now, let's do the semantic search based on the pgvector. The “Data_Embedding.py” Python script was used for data embedding using the Generalised LLM v6 model, which produced 384 dimensions. 

Step 5: After embedding the vector data into the same table using the LLM model, let's do a simple hybrid search, combining keyword-based full-text search + Similarity/Semantic search. Here, we are using a cosine similarity search operator with ranking functionality. This will produce results ordered by or ranked by the cross-encoder LLM model. Use the “hybrid_search_with_ranking.py” script to run this step.

Step 6: Similar to #5, we are doing a hybrid search, which combines a full-text-based search for keyword searching and a semantic search for similarity search. We have used “distance” to rank the results. Observe the ranking, which is different in step #5 and step #6 here.  Use the “Hybrid_Search_SQL_with_Distance” script.
![image](https://github.com/user-attachments/assets/6f17af52-9974-42af-a4ce-1d53a536cd42)
