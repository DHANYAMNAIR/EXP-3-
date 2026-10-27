from input_module import get_customer_details
from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import summarize_conversation
from save_module import save_reply


def main():

    # 1. Customer Email
    name, subject, email = get_customer_details()

    print("\n[1] Customer Email Received")
    print("---------------------------")
    print(email)

    # 2. Intent Detection
    intent = detect_intent(email)

    print("\n[2] Intent Detection")
    print("--------------------")
    print(intent)

    # 3. Similar Email Retrieval
    similar_email, score = retrieve_similar_email(email)

    print("\n[3] Similar Email Retrieval")
    print("---------------------------")
    print("Similar Customer:", similar_email["Customer Name"])
    print("Similar Email:", similar_email["Customer Email"])
    print("Similarity Score:", round(score, 2))

    # 4. AI Reply
    reply = generate_reply(name, email, intent)

    print("\n[4] AI Generated Reply")
    print("----------------------")
    print(reply)

    # 5. Tone Improvement
    improved_reply = improve_tone(reply)

    print("\n[5] Tone Improvement")
    print("--------------------")
    print(improved_reply)

    # 6. Conversation Summary
    summary = summarize_conversation(email, improved_reply)

    print("\n[6] Conversation Summary")
    print("------------------------")
    print(summary)

    # 7. Save Reply
    filename = save_reply(
        name,
        email,
        intent,
        improved_reply,
        summary
    )

    print("\n[7] Saved Reply")
    print("----------------")
    print("Reply saved successfully!")
    print("File:", filename)

    print("\n======================================")
    print("       EMAIL ASSISTANT COMPLETED")
    print("======================================")


if __name__ == "__main__":
    main()