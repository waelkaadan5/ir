from test1.retrieving_functions import get_top_related_docs, get_top_related_docs_clustered

query1 = "why do u need to put thermometr , oxygen stuff and others in fish tank when fishes happily survive in sea?"
query = "Why don't the Greeks ask the British to return some of their ancient artifacts like the Elgin Marbles?"
print(get_top_related_docs(query))
print(get_top_related_docs_clustered(query))
