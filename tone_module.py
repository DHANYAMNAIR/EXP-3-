import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


def improve_tone(reply):
    prompt = f"""
Improve the tone of this customer support email.

Make it:
- Professional
- Polite
- Empathetic
- Clear
- Customer-friendly

Do not change the meaning.

Original reply:
{reply}

Return only the improved reply.
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
    reply = input("Enter reply: ")

    improved = improve_tone(reply)

    print("\nTone Improved Reply")
    print("-------------------")
    print(improved)