# default parameters: param_name=value
def food_order_form(
        first_name,
        last_name,
        phone,
        email,
        food,
        coupon=None,
        message=None,
):
    print(f"Thank you for you order {first_name} {last_name}")
    print(f"The food that you ordered: {food}")
    print(f"Your phone: {phone}")
    print(f"Your email: {email}")

    price = 1000

    if message:
        print(f"Your message: {message}")

    if coupon:
        print(f"Total price: {price / 2} Ft")
    else:
        print(f"Total price: {price} Ft")


food_order_form(
    first_name="Robert",
    last_name="Vari",
    phone="0620 334 9876",
    email="mail.pythonsuli@gmail.com",
    food="gulas",
    coupon="4342jgregr",
    message="A kapukód a futárnak: 34",
)