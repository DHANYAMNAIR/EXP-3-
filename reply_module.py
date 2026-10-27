import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


def generate_reply(name, email, intent):
    prompt = f"""
You are a professional customer support assistant.

Customer Name: {name}
Customer Email: {email}
Detected Intent: {intent}

Write a polite, professional and helpful customer support reply.

Rules:
- Address the customer by name.
- Acknowledge the issue.
- Provide a helpful response.
- Be concise.
- Do not invent order numbers, refund amounts or company policies.
- End professionally.

Return only the email reply.
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
    name = input("Customer Name: ")
    email = input("Customer Email: ")
    intent = input("Detected Intent: ")

    reply = generate_reply(name, email, intent)

    print("\nAI Generated Reply")
    print("------------------")
    print(reply)