# import models.clients as clients
from models import (Client, 
                    PostalAddress, 
                    Email, 
                    Invoice, 
                    InvoiceItem)




def main():
    postal_address = PostalAddress("Ulica Primjera", "10A", "10000", "Zagreb", "Hrvatska")
    email_address = Email("pero@email.com", "Work")
    pero_peric = Client("Pero", "Peric", postal_address, email_address, "+38591234567")


    invoice = Invoice(
        invoice_number="INV-1001",
        invoice_date="2024-06-15",
        due_date="2024-07-15",
        client=pero_peric,
        items=[
            InvoiceItem(description="Web Design Services", quantity=1, unit_price=1500.00),
            InvoiceItem(description="Hosting (12 months)", quantity=1, unit_price=240.00),
            InvoiceItem(description="Domain Registration (1 year)", quantity=1, unit_price=15.00)
        ],
        tax_rate=0.25
    )
    pero_peric.add_invoice(invoice)
    invoice.add_item(InvoiceItem("SEO Services", 5, 300.00))


    invoice_1 = Invoice(
        invoice_number="INV-1002",
        invoice_date="2024-06-20",
        due_date="2024-07-20",
        client=pero_peric,
        items=[
            InvoiceItem(description="Consulting Services", quantity=2, unit_price=800.00)
        ],
        tax_rate=0.25
    )
    pero_peric.add_invoice(invoice_1)


    for invoice in pero_peric.invoices:
        invoice.print_invoice()
        print("\n" + "="*40 + "\n")

    print(pero_peric.total_invoices_amount)

    print()
    print("\n" + "="*40 + "\n")
    print()
    pero_peric.invoices[0].print_invoice()


if __name__ == "__main__":
    main()