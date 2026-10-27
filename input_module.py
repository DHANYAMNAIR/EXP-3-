def get_customer_details():
    print("\n" + "=" * 60)
    print("CUSTOMER EMAIL DETAILS")
    print("=" * 60)

    customer_name = input("Enter Customer Name : ")
    subject = input("Enter Email Subject : ")
    customer_email = input("Enter Customer Email : ")

    return customer_name, subject, customer_email


def display_customer_details(customer_name, subject, customer_email):
    print("\n" + "=" * 60)
    print("ENTERED CUSTOMER DETAILS")
    print("=" * 60)

    print("Customer Name  :", customer_name)
    print("Subject        :", subject)
    print("Customer Email :", customer_email)


if __name__ == "__main__":
    name, subject, email = get_customer_details()
    display_customer_details(name, subject, email)