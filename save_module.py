from datetime import datetime


def save_reply(name, email, intent, reply, summary):
    filename = "saved_reply.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("INTELLIGENT EMAIL ASSISTANT\n")
        file.write("===========================\n\n")

        file.write("Customer Name: " + name + "\n")
        file.write("Customer Email: " + email + "\n")
        file.write("Detected Intent: " + intent + "\n")
        file.write(
            "Generated On: "
            + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            + "\n\n"
        )

        file.write("AI REPLY\n")
        file.write("--------\n")
        file.write(reply + "\n\n")

        file.write("CONVERSATION SUMMARY\n")
        file.write("--------------------\n")
        file.write(summary + "\n")

    return filename


if __name__ == "__main__":
    name = input("Customer Name: ")
    email = input("Customer Email: ")
    intent = input("Intent: ")
    reply = input("Reply: ")
    summary = input("Summary: ")

    filename = save_reply(
        name,
        email,
        intent,
        reply,
        summary
    )

    print("\nReply saved successfully!")
    print("File:", filename)