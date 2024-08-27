# Initial Inventory
inventory = [
    ['001', 'T-shirt', 450, 50],
    ['002', 'Jeans', 600, 30]
]

def add_product(product_id, name, price, quantity):
    inventory.append([product_id, name, price, quantity])

def update_product(product_id, name=None, price=None, quantity=None):
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
    global inventory
    inventory = [product for product in inventory if product[0] != product_id]

def display_menu():
    print("1. Browse Products")
    print("2. View Cart")
    print("3. Place Order")
    print("4. Exit")

def handle_user_input():
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

cart = []

def browse_products():
    print("Available Products:")
    for product in inventory:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]} EGP, Quantity: {product[3]}")

    product_id = input("Enter the product ID to add to cart or 'b' to go back: ")
    if product_id == 'b':
        return
    add_to_cart(product_id)

def add_to_cart(product_id):
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

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        for item in cart:
            print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]} EGP, Quantity: {item[3]}")

def place_order():
    if not cart:
        print("Your cart is empty.")
        return
    
    total = sum(item[2] * item[3] for item in cart)
    print(f"Total amount to pay: {total} EGP")
    
    confirmation = input("Do you want to place the order? (yes/no): ")
    if confirmation.lower() == 'yes':
        generate_order_summary()
        update_inventory()
        print("Order placed successfully!")
        cart.clear()
    else:
        print("Order cancelled.")

def generate_order_summary():
    print("Order Summary:")
    for item in cart:
        print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[3]}, Subtotal: {item[2] * item[3]} EGP")
    print(f"Total Amount: {sum(item[2] * item[3] for item in cart)} EGP")

def update_inventory():
    for item in cart:
        for product in inventory:
            if product[0] == item[0]:
                product[3] -= item[3]

def add_to_cart(product_id):
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

# Add new products to the inventory
add_product('003', 'Shoes', 300, 20)
add_product('004', 'Jacket', 800, 15)

# Print inventory to verify
print("Inventory after adding products:")
for product in inventory:
    print(product)

browse_products()

# Add items to cart
browse_products()
# Manually add some items through the prompts

# View cart
view_cart()

place_order()

print("Inventory after placing the order:")
for product in inventory:
    print(product)

# Try adding an invalid product ID to the cart
browse_products('999')  # Enter an invalid product ID, e.g., 999

# Try placing an order with an out-of-stock product
add_product('005', 'Hat', 200, 1)
browse_products()  # Add 'Hat' to the cart with a quantity of 2

# Try providing invalid payment information during order placement (if implemented)
place_order()
