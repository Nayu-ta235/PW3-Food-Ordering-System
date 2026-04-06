import streamlit as st

def main():
    st.title("Food Ordering System")

    # Menu with prices
    menu = {
        "Nasi Lemak - RM5": 5,
        "Chicken Chop - RM 12": 12,
        "Burger - RM8": 8
    }

    # Input widgets
    customer_name = st.text_input("Customer Name")
    food_selection = st.selectbox("Food Selection", list(menu.keys()))
    quantity = st.number_input("Quantity", min_value=0, step=1, value=1)
    order_button = st.button("Order")

    # Handle button click
    if order_button:
        try:
            # Exception handling for empty name
            if not customer_name.strip():
                st.error("❌ Error: Customer name cannot be empty!")
            # Exception handling for invalid quantity
            elif quantity <= 0:
                st.error("❌ Error: Quantity must be greater than zero!")
            else:
                # Calculate total price
                price_per_unit = menu[food_selection]
                total_price = price_per_unit * quantity

                # Display order info
                st.success("✅ Order placed successfully!")
                st.subheader("------- Order Information -------")
                st.write(f"**Customer Name:** {customer_name}")
                st.write(f"**Food Item:** {food_selection}")
                st.write(f"**Quantity:** {quantity}")
                st.write(f"**Price per unit:** RM{price_per_unit:.2f}")
                st.write(f"**Total Price:** RM{total_price:.2f}")

        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()