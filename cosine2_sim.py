documents = (
"life learning",
"The game of life is a game of everlasting learning",
"The unexamined life is not worth living",
"Never stop learning"
)

#text1 = "The sky is blue"

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print(tfidf_matrix.shape)

from sklearn.metrics.pairwise import cosine_similarity
print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix))