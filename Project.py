# Initial Inventory
inventory = [
    ['003', 'Shoes', 300, 20],
    ['002', 'Jeans', 600, 30]
]

# Cart to store added items
cart = []

def add_product(product_id, name, price, quantity):
    """Adds a new product to the inventory."""
    inventory.append([product_id, name, price, quantity])

def update_product(product_id, name=None, price=None, quantity=None):
    """Updates existing product details."""
    for product in inventory:
        if product[0] == product_id:
            if name:
                product[1] = name
            if price:
                product[2] = price
            if quantity is not None:
                product[3] = quantity
            return True
    return False

def remove_product(product_id):
    """Removes a product from the inventory."""
    global inventory
    inventory = [product for product in inventory if product[0] != product_id]

def display_menu():
    """Displays the main menu options."""
    print("\nMain Menu:")
    print("1. Browse Products")
    print("2. View Cart")
    print("3. Place Order")
    print("4. Exit")

def handle_user_input():
    """Handles user input to navigate through the application."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            browse_products()
        elif choice == '2':
            view_cart()
        elif choice == '3':
            place_order()
        elif choice == '4':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

def browse_products():
    """Displays available products and allows users to add them to the cart."""
    print("\nAvailable Products:")
    for product in inventory:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]} EGP, Quantity: {product[3]}")

    product_id = input("Enter the product ID to add to cart or 'b' to go back: ")
    if product_id == 'b':
        return
    add_to_cart(product_id)

def add_to_cart(product_id):
    """Adds a specified product to the cart."""
    try:
        for product in inventory:
            if product[0] == product_id:
                quantity = int(input(f"Enter quantity for {product[1]}: "))
                if quantity <= product[3]:
                    cart.append([product_id, product[1], product[2], quantity])
                    print(f"Added {quantity} of {product[1]} to your cart.")
                else:
                    print("Sorry, not enough stock available.")
                return
        print("Product ID not found.")
    except ValueError:
        print("Invalid quantity entered. Please enter a number.")

def view_cart():
    """Displays the current contents of the cart."""
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nYour Cart:")
        for item in cart:
            print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]} EGP, Quantity: {item[3]}")

def place_order():
    """Handles the process of placing an order."""
    if not cart:
        print("Your cart is empty.")
        return
    
    total = sum(item[2] * item[3] for item in cart)
    print(f"Total amount to pay: {total} EGP")
    
    confirmation = input("Do you want to place the order? (yes/no): ")
    if confirmation.lower() == 'yes':
        if process_payment(total):
            generate_order_summary()
            update_inventory()
            print("Order placed successfully!")
            cart.clear()
        else:
            print("Payment failed. Order was not placed.")
    else:
        print("Order cancelled.")

def generate_order_summary():
    """Generates and displays a summary of the order."""
    print("\nOrder Summary:")
    for item in cart:
        print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[3]}, Subtotal: {item[2] * item[3]} EGP")
    print(f"Total Amount: {sum(item[2] * item[3] for item in cart)} EGP")

def update_inventory():
    """Updates the inventory based on the items purchased."""
    for item in cart:
        for product in inventory:
            if product[0] == item[0]:
                product[3] -= item[3]

def process_payment(total_amount):
    """Simulates the payment process."""
    print(f"Your total amount to pay is: {total_amount} EGP")
    payment_method = input("Enter payment method (e.g., credit card, cash): ")

    # Simulate payment success or failure
    if payment_method.lower() in ['credit card', 'cash']:
        print("Processing payment...")
        # Simulate successful payment
        print("Payment successful!")
        return True
    else:
        print("Invalid payment method. Payment failed.")
        return False

# Add new products to the inventory
add_product('001', 'T-shirt', 450, 50)
add_product('004', 'Jacket', 800, 15)

# Initial inventory verification
print("Inventory after adding products:")
for product in inventory:
    print(product)

# Start handling user input for the application
handle_user_input()

# After user interaction, show the inventory status
print("\nInventory after user interaction:")
for product in inventory:
    print(product)
