import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


def summarize_conversation(email, reply):
    prompt = f"""
Summarize this customer support conversation.

Customer Email:
{email}

Support Reply:
{reply}

Give a short summary in 2-3 sentences.
Return only the summary.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()


if __name__ == "__main__":
    email = input("Customer Email: ")
    reply = input("Support Reply: ")

    summary = summarize_conversation(email, reply)

    print("\nConversation Summary")
    print("-------------------")
    print(summary)