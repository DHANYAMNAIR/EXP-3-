import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def detect_intent(email):
    prompt = f"""
Classify the following customer email into exactly ONE of these categories:

1. Delivery Issue
2. Refund Request
3. Product Complaint
4. Technical Support
5. Order Cancellation
6. General Inquiry

Customer email:
{email}

Return ONLY the category name.
Do not return the number.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"].strip()

    # Clean unwanted numbering
    categories = [
        "Delivery Issue",
        "Refund Request",
        "Product Complaint",
        "Technical Support",
        "Order Cancellation",
        "General Inquiry"
    ]

    for category in categories:
        if category.lower() in result.lower():
            return category

    return "General Inquiry"


if __name__ == "__main__":
    email = input("Enter customer email: ")

    intent = detect_intent(email)

    print("\nDetected Intent")
    print(intent)