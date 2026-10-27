import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_similar_email(customer_email):
    data = pd.read_csv("data/emails.csv")

    emails = data["Customer Email"].fillna("").astype(str).tolist()

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(emails + [customer_email])

    similarities = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )[0]

    best_index = similarities.argmax()

    return data.iloc[best_index], similarities[best_index]


if __name__ == "__main__":
    email = input("Enter customer email: ")

    row, score = retrieve_similar_email(email)

    print("\nSimilar Email Retrieved")
    print("-----------------------")
    print("Customer:", row["Customer Name"])
    print("Subject:", row["Email Subject"])
    print("Email:", row["Customer Email"])
    print("Intent:", row["Intent"])
    print("Similarity Score:", round(score, 2))