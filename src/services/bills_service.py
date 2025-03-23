import shlex
from src.commands.bills import make_bill, list_bills, change_bill, delete_bill

def lsbills(arg):
    """List all bills."""
    list_bills()

def mkbill(arg):
    """
            Create a new bill.
            Usage: mkbill -description <description> -price <price>
            """
    try:
        args = shlex.split(arg)
        description = None
        price = None

        if "-description" in args:
            description = args[args.index("-description") + 1]
        if "-price" in args:
            price = args[args.index("-price") + 1]

        if description and price:
            make_bill(description, price)
        else:
            print("Error: -description and -price are required.")
    except (ValueError, IndexError) as e:
        print("Error: Invalid arguments. Usage: mktodo -description <description> -price <price>")

def chbill(arg):
    """
            Modify an existing bill.
            Usage: chbill -id <id> [-description <description>] [-price <price>]
            """
    try:
        args = shlex.split(arg)
        bill_id = None
        description = None
        price = None

        if "-id" in args:
            bill_id = int(args[args.index("-id") + 1])
        if "-description" in args:
            description = args[args.index("-description") + 1]
        if "-price" in args:
            price = args[args.index("-price") + 1]

        if bill_id is not None:
            change_bill(bill_id, description, price)
        else:
            print("Error: -id is required.")
    except (ValueError, IndexError) as e:
        print(
            "Error: Invalid arguments. Usage: chbill -id <id> [-description <description>] [-price <price>]")

def rmbill(arg):
    """
            Remove a bill by ID.
            Usage: rmbill -id <id>
            """
    try:
        args = shlex.split(arg)
        bill_id = None

        if "-id" in args:
            bill_id = int(args[args.index("-id") + 1])

        if bill_id is not None:
            delete_bill(bill_id)
        else:
            print("Error: -id is required.")
    except (ValueError, IndexError) as e:
        print("Error: Invalid arguments. Usage: rmbill -id <id>")