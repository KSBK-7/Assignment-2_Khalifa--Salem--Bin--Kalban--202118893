import datetime
from decimal import Decimal

class Book:
    """Represents a book in the e-bookstore."""
  
    def __init__(self, title, author, publication_date, genre, price):
        """
        Initializes a new Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_date (datetime.date): The publication date of the book.
            genre (str): The genre of the book.
            price (Decimal or float): The price of the book.
        """
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self._price = price

    # Getters and Setters
    def get_title(self):
        """Returns the title of the book."""
        return self._title

    def set_title(self, value):
        """Sets the title of the book."""
        self._title = value

    def get_author(self):
        """Returns the author of the book."""
        return self._author

    def set_author(self, value):
        """Sets the author of the book."""
        self._author = value

    def get_publication_date(self):
        """Returns the publication date of the book."""
        return self._publication_date

    def set_publication_date(self, value):
        """Sets the publication date of the book."""
        self._publication_date = value

    def get_genre(self):
        """Returns the genre of the book."""
        return self._genre

    def set_genre(self, value):
        """Sets the genre of the book."""
        self._genre = value

    def get_price(self):
        """Returns the price of the book."""
        return self._price

    def set_price(self, value):
        """Sets the price of the book."""
        self._price = value

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self._title} by {self._author} ({self._genre}, {self._publication_date.year})"


class EBook(Book):
    """Represents an e-book in the e-bookstore."""
    
    def __init__(self, title, author, publication_date, genre, price, file_format):
        """
        Initializes a new EBook instance.
        
        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            publication_date (datetime.date): The publication date of the e-book.
            genre (str): The genre of the e-book.
            price (Decimal): The price of the e-book.
            file_format (str): The file format of the e-book (e.g., PDF, EPUB).
        """
        super().__init__(title, author, publication_date, genre, price)
        self._file_format = file_format

    # Getters and Setters
    def get_file_format(self):
        """Returns the file format of the e-book."""
        return self._file_format

    def set_file_format(self, value):
        """Sets the file format of the e-book."""
        self._file_format = value

    def deliver_ebook(self):
        """Delivers the e-book to the customer."""
        print(f"Delivering {self.get_title()} in {self.get_file_format()} format.")

    def __str__(self):
        """Returns a detailed string representation of the e-book."""
        return (f"E-Book Title: {self._title}\n"
                f"Author: {self._author}\n"
                f"Publication Date: {self._publication_date}\n"
                f"Genre: {self._genre}\n"
                f"Price: ${self._price:.2f}\n"
                f"File Format: {self._file_format}\n")

class Catalog:
    """Represents a catalog of available e-books."""
    
    def __init__(self):
        """Initializes an empty catalog."""
        self._items = []

    # Getter and Setter for items
    def get_items(self):
        """Returns the list of items in the catalog."""
        return self._items

    def set_items(self, items):
        """Sets the list of items in the catalog."""
        self._items = items

    def add_item(self, ebook):
        """Adds an e-book to the catalog.
        
        Args:
            ebook (EBook): The e-book to be added.
        """
        self._items.append(ebook)

    def modify_item(self, title, author=None, publication_date=None, genre=None, price=None, file_format=None):
        """Modifies the details of an existing e-book by its title.
        
        Args:
            title (str): The title of the e-book to modify.
            author (str, optional): The new author name.
            publication_date (datetime.date, optional): The new publication date.
            genre (str, optional): The new genre.
            price (Decimal, optional): The new price.
            file_format (str, optional): The new file format.
        """
        ebook = self.find_by_title(title)
        if ebook:
            if author is not None:
                ebook.set_author(author)
            if publication_date is not None:
                ebook.set_publication_date(publication_date)
            if genre is not None:
                ebook.set_genre(genre)
            if price is not None:
                ebook.set_price(price)
            if file_format is not None:
                ebook.set_file_format(file_format)

    def remove_item(self, title):
        """Removes an e-book from the catalog by its title.
        
        Args:
            title (str): The title of the e-book to remove.
        """
        new_items = []
        for ebook in self._items:
            if ebook.get_title() != title:
                new_items.append(ebook)
        self._items = new_items

    def find_by_title(self, title):
        """Finds an e-book by its title.
        
        Args:
            title (str): The title of the e-book to find.
        
        Returns:
            EBook or None: The found e-book, or None if not found.
        """
        for ebook in self._items:
            if ebook.get_title().lower() == title.lower():
                return ebook
        return None

    def list_items(self):
        """Returns a list of all e-books in the catalog."""
        return self._items

    def __repr__(self):
        """Returns a string representation of the catalog."""
        return f"EBookCatalog with {len(self._items)} e-books"

    def __str__(self):
        """Returns a string representation of the catalog details."""
        if not self._items:
            return "The catalog is empty."
        ebooks_list = []
        for ebook in self._items:
            ebooks_list.append(str(ebook))
        ebooks = '\n'.join(ebooks_list)

        return (f"Catalog of E-Books:\n"
                f"Total e-books: {len(self._items)}\n"
                f"{ebooks}")

class Customer:
    """Represents a customer of the e-bookstore."""
    
    def __init__(self, name, email, phone):
        """
        Initializes a new Customer instance.
        
        Args:
            name (str): The name of the customer.
            email (str): The email address of the customer.
            phone (str): The phone number of the customer.
        """
        self._name = name
        self._email = email
        self._phone = phone
        self._loyalty_points = 0        

    def get_name(self):
        """Returns the name of the customer."""
        return self._name

    def set_name(self, value):
        """Sets the name of the customer."""
        self._name = value

    def get_email(self):
        """Returns the email of the customer."""
        return self._email

    def set_email(self, value):
        """Sets the email of the customer."""
        self._email = value

    def get_phone(self):
        """Returns the phone number of the customer."""
        return self._phone

    def set_phone(self, value):
        """Sets the phone number of the customer."""
        self._phone = value

    def get_loyalty_points(self):
        """Returns the loyalty points of the customer."""
        return self._loyalty_points

    def set_loyalty_points(self, value):
        """Sets the loyalty points of the customer to 0 or more."""
        self._loyalty_points = max(0, value)  

    def create_account(self):
        """Creates a new customer account."""
        print(f"New customer account created for {self.get_name()}.")

    def update_account(self, name=None, email=None, phone=None):
        """Updates the existing customer account.
        
        Args:
            name (str, optional): The new name of the customer.
            email (str, optional): The new email of the customer.
            phone (str, optional): The new phone number of the customer.
        """
        if name:
            self.set_name(name)  
        if email:
            self.set_email(email) 
        if phone:
            self.set_phone(phone) 
        print(f"Customer account updated for {self.get_name()}.")

    def update_loyalty_points(self, points):
        """Updates the loyalty points for the customer.
        
        Args:
            points (int): The number of points to add.
        """
        self.set_loyalty_points(self.get_loyalty_points() + points)  
        print(f"Loyalty points updated for {self.get_name()}. Current points: {self.get_loyalty_points()}")

    def place_order(self, ebook):
        """Places an order for an e-book and updates loyalty points.
        
        Args:
            ebook (EBook): The e-book being ordered.
        """
        print(f"{self.get_name()} placed an order for {ebook.get_title()}.")
        self.update_loyalty_points(1)  # Example: 1 point for every order

    def __str__(self):
        """Returns a string representation of the customer."""
        return f"Customer Name: {self._name}\nEmail: {self._email}\nPhone: {self._phone}\nLoyalty Points: {self._loyalty_points}"


class CustomerList:
    """Manages a list of customer accounts."""

    def __init__(self):
        """Initializes the CustomerList with an empty list of customers."""
        self._customers = []

    # Getter and Setter for customers
    def get_customers(self):
        """Returns the list of customers."""
        return self._customers

    def set_customers(self, customers):
        """Sets the list of customers."""
        self._customers = customers

    def add_customer(self, customer):
        """Add a new customer to the list.

        Args:
            customer (Customer): The customer to add.
        """
        self._customers.append(customer)
        print(f"Added customer: {customer.get_name()}")

    def modify_customer(self, old_customer, new_name=None, new_email=None, new_phone=None):
        """Modify the details of an existing customer.

        Args:
            old_customer (Customer): The customer to modify.
            new_name (str, optional): New name for the customer.
            new_email (str, optional): New email for the customer.
            new_phone (str, optional): New phone number for the customer.
        """
        if old_customer in self._customers:
            old_customer.update_account(new_name, new_email, new_phone)
        else:
            print("Customer not found.")

    def remove_customer(self, customer):
        """Remove a customer from the list.

        Args:
            customer (Customer): The customer to remove.
        """
        if customer in self._customers:
            self._customers.remove(customer)
            print(f"Removed customer: {customer.get_name()}")
        else:
            print("Customer not found.")

    def get_all_customers(self):
        """Return a list of all customers.

        Returns:
            list: The list of customers.
        """
        return self._customers

    def __str__(self):
        """Returns a string representation of the customer list."""
        if not self._customers:
            return "Customer List is empty."

        customer_details_list = [str(customer) for customer in self._customers]
        customer_details = "\n".join(customer_details_list)

        return (f"Customer List ({len(self._customers)} customers):\n"
                f"{customer_details}")


class ShoppingCart:
    """Represents a customer's shopping cart."""

    def __init__(self, customer):
        """Initializes the ShoppingCart with the associated customer.

        Args:
            customer (Customer): The customer associated with the cart.
        """
        self._customer = customer
        self._items = []
        self._total_price = Decimal('0.00')

    # Getters and setters
    def get_customer(self):
        """Returns the customer associated with the shopping cart."""
        return self._customer

    def set_customer(self, customer):
        """Sets the customer associated with the shopping cart.

        Args:
            customer (Customer): The customer to associate with the cart.
        """
        self._customer = customer

    def get_items(self):
        """Returns the list of items in the shopping cart."""
        return self._items

    def set_items(self, items):
        """Sets the list of items in the shopping cart.

        Args:
            items (list): The items to set in the cart.
        """
        self._items = items

    def get_total_price(self):
        """Returns the total price of items in the shopping cart."""
        return self._total_price

    def set_total_price(self, total_price):
        """Sets the total price of items in the shopping cart.

        Args:
            total_price (Decimal): The total price to set.
        """
        self._total_price = total_price

    def add_item(self, ebook, quantity=1):
        """Add an e-book to the shopping cart.

        Args:
            ebook (EBook): The e-book to add.
            quantity (int, optional): The quantity of the e-book to add. Defaults to 1.
        """
        self._items.append((ebook, quantity))
        self._total_price += ebook.get_price() * quantity

    def apply_loyalty_discount(self):
        """Apply a loyalty discount if applicable."""
        if self._customer.get_loyalty_points() > 0:
            self._total_price *= Decimal('0.90')  # Apply 10% discount

    def remove_item(self, ebook):
        """Remove an e-book from the shopping cart.

        Args:
            ebook (EBook): The e-book to remove.
        """
        for item in self._items:
            if item[0] == ebook:
                self._items.remove(item)
                self._total_price -= ebook.get_price() * item[1]
                break

    def update_quantity(self, ebook, quantity):
        """Update the quantity of an e-book in the shopping cart.

        Args:
            ebook (EBook): The e-book to update.
            quantity (int): The new quantity for the e-book.
        """
        item = None
        for existing_item in self._items:
            if existing_item[0] == ebook:
                item = existing_item
                break

        if item:
            self._total_price -= ebook.get_price() * item[1]
            self._items.remove(item)
        self._items.append((ebook, quantity))
        self._total_price += ebook.get_price() * quantity

    def create_order(self, order_date, vat_rate=Decimal('0.08')):
        """Create an Order from the shopping cart items.

        Args:
            order_date (datetime): The date of the order.
            vat_rate (Decimal, optional): The VAT rate to apply. Defaults to 8%.

        Returns:
            Order: The created order or a message if the cart is empty.
        """
        if not self._items:
            return f"{self._customer.get_name()}'s Shopping Cart is empty."

        order = Order(order_date, self._customer)
        for ebook, quantity in self._items:
            for _ in range(quantity):
                order.add_ebook(ebook)
        return order

    def __str__(self):
        """Returns a string representation of the shopping cart."""
        if not self._items:
            return f"{self._customer.get_name()}'s Shopping Cart is empty."

        items_summary_list = [
            f"{ebook.get_title()} - Quantity: {quantity} - Price: {ebook.get_price() * quantity:.2f}"
            for ebook, quantity in self._items
        ]

        items_summary = "\n".join(items_summary_list)
        return (f"{self._customer.get_name()}'s Shopping Cart:\n"
                f"Total Price: {self._total_price:.2f}\n"
                f"Items:\n{items_summary}")

class Order:
    """Represents a customer order with discount capabilities."""
  
    def __init__(self, order_date, customer, vat_rate=Decimal('0.08'), loyalty_discount=Decimal('0.1'), bulk_discount=Decimal('0.2')):
        """Initializes the Order with the specified date, customer, and discount rates.

        Args:
            order_date (datetime): The date of the order.
            customer (Customer): The customer placing the order.
            vat_rate (Decimal, optional): The VAT rate. Defaults to 0.08 (8%).
            loyalty_discount (Decimal, optional): The loyalty discount rate. Defaults to 0.1 (10%).
            bulk_discount (Decimal, optional): The bulk discount rate. Defaults to 0.2 (20%).
        """
        self._order_date = order_date
        self._customer = customer
        self._total_price = Decimal(0)
        self._vat_rate = vat_rate  
        self._ebooks = []
        self._loyalty_discount = Decimal(loyalty_discount)
        self._bulk_discount = Decimal(bulk_discount)

    # Getters and setters
    def get_order_date(self):
        """Returns the order date.

        Returns:
            datetime: The date when the order was placed.
        """
        return self._order_date

    def set_order_date(self, order_date):
        """Sets the order date.

        Args:
            order_date (datetime): The new order date.
        """
        self._order_date = order_date

    def get_customer(self):
        """Returns the customer associated with the order.

        Returns:
            Customer: The customer placing the order.
        """
        return self._customer

    def set_customer(self, customer):
        """Sets the customer for the order.

        Args:
            customer (Customer): The customer to set for the order.
        """
        self._customer = customer

    def get_total_price(self):
        """Returns the total price of the order.

        Returns:
            Decimal: The total price of the order.
        """
        return self._total_price

    def set_total_price(self, total_price):
        """Sets the total price for the order.

        Args:
            total_price (Decimal): The total price to set.
        """
        self._total_price = total_price

    def get_vat_rate(self):
        """Returns the VAT rate applied to the order.

        Returns:
            Decimal: The VAT rate.
        """
        return self._vat_rate

    def set_vat_rate(self, vat_rate):
        """Sets the VAT rate for the order.

        Args:
            vat_rate (Decimal): The VAT rate to set.
        """
        self._vat_rate = Decimal(vat_rate)

    def get_ebooks(self):
        """Returns the list of e-books in the order.

        Returns:
            list: The list of e-books.
        """
        return self._ebooks

    def set_ebooks(self, ebooks):
        """Sets the list of e-books for the order.

        Args:
            ebooks (list): The list of e-books to set.
        """
        self._ebooks = ebooks

    def get_loyalty_discount(self):
        """Returns the loyalty discount rate.

        Returns:
            Decimal: The loyalty discount rate.
        """
        return self._loyalty_discount

    def set_loyalty_discount(self, loyalty_discount):
        """Sets the loyalty discount rate.

        Args:
            loyalty_discount (Decimal): The loyalty discount to set.
        """
        self._loyalty_discount = loyalty_discount

    def get_bulk_discount(self):
        """Returns the bulk discount rate.

        Returns:
            Decimal: The bulk discount rate.
        """
        return self._bulk_discount

    def set_bulk_discount(self, bulk_discount):
        """Sets the bulk discount rate.

        Args:
            bulk_discount (Decimal): The bulk discount to set.
        """
        self._bulk_discount = bulk_discount

    def add_ebook(self, ebook):
        """Add an e-book to the order and update the total price.

        Args:
            ebook (EBook): The e-book to add to the order.
        """
        self._ebooks.append(ebook)
        self._total_price += ebook.get_price()

    def apply_discounts(self):
        """Apply discounts to the total price of the order.

        Returns:
            Decimal: The discounted price after applying loyalty and bulk discounts.
        """
        discounted_price = self._total_price
        if len(self._ebooks) >= 5:
            discounted_price *= (1 - self._bulk_discount)
        if self._customer.get_loyalty_points() > 0:
            discounted_price *= (1 - self._loyalty_discount)
        return discounted_price

    def generate_invoice(self):
        """Generate an invoice for the order and print it to the console."""
        print("Order Invoice:")
        print(f"Order Date: {self._order_date.strftime('%Y-%m-%d')}")
        print("Items:")
        for ebook in self._ebooks:
            print(f"- {ebook.get_title()} - {ebook.get_price():.2f}")
        print(f"Subtotal: {self._total_price:.2f}")
        vat_amount = self._total_price * self._vat_rate
        print(f"VAT ({self._vat_rate * 100}%): {vat_amount:.2f}")
        
        # Calculate total after discounts
        grand_total = self.apply_discounts() + vat_amount
        print(f"Total: {grand_total:.2f}")

    def __str__(self):
        """Returns a string representation of the order invoice, including items, subtotal, VAT, and total after discounts.

        Returns:
            str: A formatted string representing the order invoice.
        """
        items_summary_list = []
        for ebook in self._ebooks:
            items_summary_list.append(f"- {ebook.get_title()} - Price: {ebook.get_price():.2f}")
        
        items_summary = "\n".join(items_summary_list)
        vat_amount = self._total_price * self._vat_rate
        grand_total = self.apply_discounts() + vat_amount
        
        return (f"Order Invoice:\n"
                f"Order Date: {self._order_date.strftime('%Y-%m-%d')}\n"
                f"Customer: {self._customer.get_name()}\n"
                f"Items:\n{items_summary}\n"
                f"Subtotal: {self._total_price:.2f}\n"
                f"VAT ({self._vat_rate * 100}%): {vat_amount:.2f}\n"
                f"Total after discounts: {grand_total:.2f}")
