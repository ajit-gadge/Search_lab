# Search_lab
Here are few simple examples that showcase Standard Search , Full-text Search, Semantic Search and Hybrid Search.


This Search Lab will help to create demo on various capabilities of Search in PostgreSQL and explore the differance amongh those. This lab also inteded to shoecase how Hybrid search and how one can use for various purpose.

Step 1: Create the Sample table in PostgreSQL with pgvector as extension that enables to create vector as Data Type. Use “Data Load” script  which will add sample sentances in Postgresql with simple text.

Step 2:  Once Data is loaded, we can do simple keyword based searching as standard search. Lets take a simple standard search. if i like search simple world like “PostgreSQL” then it’s work well. Use Standard_Search script to do demo.

Step 3:  Lets look at the full text search which understand the workd combination , conjuction , stemming etc.  Use “full-text Search” file this example. So if you look at the tsvector column data, it does tokenization of world here which including how many times that particuler word comes and position. It does understanding the conjuction word as well like “&” and stemming word.  lets search our conjction word “Postgresql & vector”. In this example,it provide me two results which does have Postgresql as word and vector as word regardless of their postion , freqancy of word and stemming and stop word.

You can also customize stop word like a, the , an, are etc in dictinory  further advanced tunning. You can further customise this for advanced trigram similarity as well with extension pg_trgm.
Fulltext search also provide lexmes based weightage and ranking. One can customise this weightage as well. So you can see on my screen the ranking of the given words.

Step 4: Now lets do the semantic search based on the pgvector. Use “Data_Embedding.py” python script for data embedding using gemelese mini llm v6 model which produced 384 dimensions. 

Step 5: After embedding the vector data into same table using LLM model, lets do simple hybrid search which is combination of Keyword based full text search + Similarity/Semantic search. Here we are using cosine similarity search operator with ranking functionality. This will produce results which are order by or rank by cross encoder LLM model. Use “hybrid_search_with_ranking.py” script to run this step.

Step 6: Similar like #4, we are doing hybrid search which is combination of full-text based search for key-world saerching and semantic search for similariry search.We have use “distance”  as order by the to rank the result. Observe the ranking which is differ in step #5 and step #6 here.  Use “Hybrid_Search_SQL_with_Distance” script.

