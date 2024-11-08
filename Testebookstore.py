
from datetime import datetime
from decimal import Decimal
from io import StringIO
import sys

from ebookstore import EBook, Customer, CustomerList, Order, Catalog, ShoppingCart

def test_catalog_operations():
    # Create a catalog
    catalog = Catalog()
    
    # 1. Add E-book
    print("\nTesting Add E-book:")
    ebook1 = EBook("Learn Python", "Alice Smith", datetime(2022, 1, 1), "Programming", Decimal('29.99'), "PDF")
    catalog.add_item(ebook1)
    assert len(catalog.list_items()) == 1, "Failed to add e-book to catalog"
    print(f"Added: {ebook1.get_title()} - Total items: {len(catalog.list_items())}")
    
    # 2. Modify E-book
    print("\nTesting Modify E-book:")
    catalog.modify_item("Learn Python", price=Decimal('24.99'), genre="Computer Science")
    modified_ebook = catalog.find_by_title("Learn Python")
    assert modified_ebook.get_price() == Decimal('24.99'), "Failed to modify e-book price"
    assert modified_ebook.get_genre() == "Computer Science", "Failed to modify e-book genre"
    print(f"Modified: {modified_ebook.get_title()} - New Price: {modified_ebook.get_price()}, New Genre: {modified_ebook.get_genre()}")
    
    # 3. Remove E-book
    print("\nTesting Remove E-book:")
    catalog.remove_item("Learn Python")
    assert len(catalog.list_items()) == 0, "Failed to remove e-book from catalog"
    print(f"Removed: Learn Python - Total items: {len(catalog.list_items())}")
    print("\n", catalog)


def test_customer_operations():
    # Create a customer list
    customer_list = CustomerList()
    
    # 1. Create a New Customer Account
    print("\nTesting Create Customer Account:")
    customer1 = Customer("John Doe", "john.doe@example.com", "+1234567890")
    customer_list.add_customer(customer1)
    assert len(customer_list.get_all_customers()) == 1, "Failed to create new customer account"
    print(f"Created Customer: {customer1.get_name()} - Total Customers: {len(customer_list.get_all_customers())}")
    
    # 2. Update Existing Customer Account
    print("\nTesting Update Customer Account:")
    customer_list.modify_customer(customer1, new_email="john.new@example.com", new_phone="+0987654321")
    updated_customer = customer_list.get_all_customers()[0]
    assert updated_customer.get_email() == "john.new@example.com", "Failed to update customer email"
    assert updated_customer.get_phone() == "+0987654321", "Failed to update customer phone"
    print(f"Updated Customer: {updated_customer.get_name()} - New Email: {updated_customer.get_email()}, New Phone: {updated_customer.get_phone()}")
    
    # 3. Delete Customer Account
    print("\nTesting Delete Customer Account:")
    customer_list.remove_customer(customer1)
    assert len(customer_list.get_all_customers()) == 0, "Failed to delete customer account"
    print(f"Deleted Customer: {customer1.get_name()} - Total Customers: {len(customer_list.get_all_customers())}")

    print("\n", customer_list)

def test_shopping_cart_operations():
    # Create an e-book catalog and a shopping cart
    catalog = Catalog()
    customer1 = Customer("John Doe", "john.doe@example.com", "+1234567890")
    shopping_cart = ShoppingCart(customer1)

    # Create some e-books to add to the catalog
    ebook1 = EBook("E-Book One", "Author A", datetime(2022, 1, 1), "Fiction", Decimal('9.99'), "PDF")
    ebook2 = EBook("E-Book Two", "Author B", datetime(2023, 5, 15), "Non-Fiction", Decimal('14.99'), "EPUB")
    
    # Add e-books to the catalog
    catalog.add_item(ebook1)
    catalog.add_item(ebook2)

    # 1. Add an E-book to the Shopping Cart
    print("\nTesting Add E-book to Shopping Cart:")
    shopping_cart.add_item(ebook1, quantity=1)
    assert len(shopping_cart.get_items()) == 1, "Failed to add e-book to shopping cart"
    assert shopping_cart.get_total_price() == ebook1.get_price(), "Total price is incorrect after adding e-book"
    print(f"Added E-book: {ebook1.get_title()} - Total Price: {shopping_cart.get_total_price():.2f}")

    # 2. Remove an E-book from the Shopping Cart
    print("\nTesting Remove E-book from Shopping Cart:")
    shopping_cart.remove_item(ebook1)
    assert len(shopping_cart.get_items()) == 0, "Failed to remove e-book from shopping cart"
    assert shopping_cart.get_total_price() == Decimal('0.00'), "Total price is incorrect after removing e-book"
    print(f"Removed E-book: {ebook1.get_title()} - Total Price: {shopping_cart.get_total_price():.2f}")

    # 3. Update the Quantity of an E-book in the Shopping Cart
    print("\nTesting Update Quantity of E-book in Shopping Cart:")
    shopping_cart.add_item(ebook1, quantity=2)  # Add it back with quantity 2
    shopping_cart.add_item(ebook2, quantity=1)  # Add another e-book
    assert len(shopping_cart.get_items()) == 2, "Failed to add multiple e-books to shopping cart"
    assert shopping_cart.get_total_price() == (ebook1.get_price() * 2 + ebook2.get_price()), "Total price is incorrect after adding multiple e-books"
    print(f"Current Total Price: {shopping_cart.get_total_price():.2f}")

    # Update the quantity of ebook1 to 3
    shopping_cart.update_quantity(ebook1, quantity=3)
    assert len(shopping_cart.get_items()) == 2, "Shopping cart item count changed unexpectedly"
    assert shopping_cart.get_total_price() == (ebook1.get_price() * 3 + ebook2.get_price()), "Total price is incorrect after updating quantity"
    print(f"Updated Quantity of E-book: {ebook1.get_title()} - New Total Price: {shopping_cart.get_total_price():.2f}")
    print("\n", catalog)


def test_order_discount_application():
    """Test case to verify discount applications in Order class."""

    print("\nTesting discount applications in Order")
    
    # Create e-book instances
    ebook1 = EBook("E-Book One", "Author A", datetime(2022, 1, 1), "Fiction", Decimal('10.00'), "PDF")
    ebook2 = EBook("E-Book Two", "Author B", datetime(2022, 2, 1), "Non-Fiction", Decimal('20.00'), "EPUB")
    ebook3 = EBook("E-Book Three", "Author C", datetime(2022, 3, 1), "Fiction", Decimal('15.00'), "MOBI")
    ebook4 = EBook("E-Book Four", "Author D", datetime(2022, 4, 1), "Fiction", Decimal('25.00'), "PDF")
    ebook5 = EBook("E-Book Five", "Author E", datetime(2022, 5, 1), "Non-Fiction", Decimal('30.00'), "EPUB")

    # Create a customer and set loyalty points
    customer_with_loyalty = Customer("John Doe", "john.doe@example.com", "+1234567890")
    customer_with_loyalty.set_loyalty_points(100)  # Set loyalty points

    # Create a shopping cart and add e-books
    shopping_cart = ShoppingCart(customer_with_loyalty)
    shopping_cart.add_item(ebook1, quantity=1)
    shopping_cart.add_item(ebook2, quantity=1)
    shopping_cart.add_item(ebook3, quantity=1)
    shopping_cart.add_item(ebook4, quantity=1)
    shopping_cart.add_item(ebook5, quantity=1)  # Total of 5 e-books

    # Create an order from the shopping cart
    order = shopping_cart.create_order(datetime(2024, 1, 1), customer_with_loyalty)

    # Expected totals without discounts
    expected_total = (ebook1.get_price() + ebook2.get_price() + ebook3.get_price() + 
                      ebook4.get_price() + ebook5.get_price())
    
    # Apply discounts
    grand_total = order.apply_discounts()  # Apply discounts to the order total

    vat_amount = Decimal(expected_total) * order.get_vat_rate()
    expected_grand_total = grand_total + vat_amount

    # Calculate expected price after discounts
    expected_price_after_bulk_discount = expected_total * Decimal('0.80')  # Apply bulk discount
    expected_price_after_loyalty_discount = expected_price_after_bulk_discount * Decimal('0.90')  # Apply loyalty discount

    # Final grand total with VAT
    final_expected_grand_total = expected_price_after_loyalty_discount + vat_amount

    # Assertions
    assert grand_total == expected_price_after_loyalty_discount, "Loyalty discount not applied correctly"
    assert order.get_total_price() == expected_total, "Total price in order should match expected total price before discounts"
    assert final_expected_grand_total == grand_total + vat_amount, "Grand total should include VAT correctly"
    
    print(f"Loyalty Discount Applied: New Total Price After Loyalty Discount: {grand_total:.2f}")
    print(f"Grand Total (Including VAT): {final_expected_grand_total:.2f}")
    print("\n", shopping_cart)



def test_invoice_generation():
    print("\nTesting Invoice generation")
    
    # Create a customer with loyalty points
    customer_with_loyalty = Customer("John Doe", "john.doe@example.com", "+1234567890")
    customer_with_loyalty.update_loyalty_points(100)

    # Create the specified e-books
    ebook1 = EBook("E-Book One", "Author A", datetime(2022, 1, 1), "Fiction", Decimal('10.00'), "PDF")
    ebook2 = EBook("E-Book Two", "Author B", datetime(2022, 2, 1), "Non-Fiction", Decimal('20.00'), "EPUB")
    ebook3 = EBook("E-Book Three", "Author C", datetime(2022, 3, 1), "Fiction", Decimal('15.00'), "MOBI")
    ebook4 = EBook("E-Book Four", "Author D", datetime(2022, 4, 1), "Fiction", Decimal('25.00'), "PDF")
    ebook5 = EBook("E-Book Five", "Author E", datetime(2022, 5, 1), "Non-Fiction", Decimal('30.00'), "EPUB")

    # Create the shopping cart and add multiple items
    shopping_cart = ShoppingCart(customer_with_loyalty)
    shopping_cart.add_item(ebook1, quantity=1)
    shopping_cart.add_item(ebook2, quantity=1)
    shopping_cart.add_item(ebook3, quantity=1)
    shopping_cart.add_item(ebook4, quantity=1)
    shopping_cart.add_item(ebook5, quantity=1)

    # Create an order from the shopping cart
    order = shopping_cart.create_order(datetime(2024, 1, 1), customer_with_loyalty)

    # Redirect stdout to capture print output
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Generate the invoice
    order.generate_invoice()


    # Get the printed output
    invoice_output = sys.stdout.getvalue()

    # Reset stdout
    sys.stdout = old_stdout

    # Expected output
    expected_items = [
        f"- {ebook1.get_title()} - {ebook1.get_price():.2f}",
        f"- {ebook2.get_title()} - {ebook2.get_price():.2f}",
        f"- {ebook3.get_title()} - {ebook3.get_price():.2f}",
        f"- {ebook4.get_title()} - {ebook4.get_price():.2f}",
        f"- {ebook5.get_title()} - {ebook5.get_price():.2f}"
    ]
    expected_items_output = "\n".join(expected_items)

    # Calculate expected subtotal, VAT, discounts, and total
    subtotal = (
        ebook1.get_price() + ebook2.get_price() +
        ebook3.get_price() + ebook4.get_price() +
        ebook5.get_price()
    )
    vat_amount = subtotal * order.get_vat_rate()
    grand_total = order.apply_discounts() + vat_amount

    # Check if the invoice output contains the expected values
    assert "Order Invoice:" in invoice_output, "Invoice header is missing"
    assert f"Order Date: {order.get_order_date().strftime('%Y-%m-%d')}" in invoice_output, "Order date is incorrect"
    assert expected_items_output in invoice_output, "Item list is incorrect"
    assert f"Subtotal: {subtotal:.2f}" in invoice_output, "Subtotal is incorrect"
    assert f"VAT ({order.get_vat_rate() * 100}%): {vat_amount:.2f}" in invoice_output, "VAT calculation is incorrect"
    assert f"Total: {grand_total:.2f}" in invoice_output, "Grand total is incorrect"

    print(order)
    print("Invoice generation test passed.")


# Run tests
if __name__ == "__main__":
    test_catalog_operations()
    test_customer_operations()
    test_shopping_cart_operations()
    test_order_discount_application()
    test_invoice_generation()