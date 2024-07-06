#Description:This program has been created for the purchase of airline tickets 
#            for Air Ontario with a user-friendly interface. Upon launch, users 
#            enter their name and access a flight schedule displaying 
#            destinations, times, statuses, and terminals. They select their 
#            preferred destination and seat class from Economy, Business, or First Class
#            alongside options for checked and carry-on bags. The program calculates 
#            the total cost, including a 13% tax, and generates a detailed ticket 
#            summary with all relevant details. Users can choose to buy additional 
#            tickets before concluding with a thank-you message from Air Ontario.

#Importing necessary modules of the rich library. The rich Library has been used for this program
#because it is very versatile with the terminal, and allows us to create elegant tables and format 
#text, allowing us to change its color etc. and show these changes in the terminal
from rich.console import Console
from rich.table import Table
from rich import box

# Initialize the console for rich text output
console = Console()

# Define flight information as a 2D array (list of lists). Information in this array is accessed
# throughout the project
flights = [
    ["Regina", "6:30AM", "8:00AM", "AO-102", "Terminal 3", "Arrived", "2024-07-05", "1", "YQR", "254"],
    ["Thunder Bay", "7:30AM", "9:30AM", "AO-132", "Terminal 3", "Arrived", "2024-07-05", "2", "YQT", "345"],
    ["Winnipeg", "8:00AM", "9:45AM", "AO-154", "Terminal 1", "Delayed", "2024-07-05", "3", "YWG", "288"],
    ["Ottawa", "8:30AM", "11:00AM", "AO-143", "Terminal 1", "Cancelled", "2024-07-05", "4", "YOW", "330"],
    ["Yellowknife", "8:30AM", "11:15AM", "AO-089", "Terminal 1", "On Time", "2024-07-05", "5", "YZF", "254"],
    ["PEI", "9:00AM", "11:45AM", "AO-161", "Terminal 3", "On Time", "2024-07-05", "6", "YYG", "600"],
    ["Halifax", "9:30AM", "12:00PM", "AO-352", "Terminal 3", "On Time", "2024-07-05", "7", "YHZ", "455"],
    ["Edmonton", "9:45AM", "12:15PM", "AO-457", "Terminal 1", "Delayed", "2024-07-05", "8", "YEG", "248"],
    ["Hamilton", "10:15AM", "12:45PM", "AO-122", "Terminal 2", "On Time", "2024-07-05", "9", "YHM", "254"],
    ["Montreal", "10:30AM", "1:00PM", "AO-494", "Terminal 3", "Cancelled", "2024-07-05", "10", "YUL", "300"],
    ["Vancouver", "11:30AM", "1:30PM", "AO-210", "Terminal 1", "On Time", "2024-07-05", "11", "YVR", "450"],
    ["Calgary", "12:15PM", "1:45PM", "AO-188", "Terminal 1", "On Time", "2024-07-05", "12", "YYC", "674"]
]

# Define the prices of each seat class as another 2D array
seat_prices = [
    ["Economy Class", 100],
    ["Business Class", 300],
    ["First Class", 500]
]

# Print the welcome banner, which has been created using ASCII characters
console.print("""[red]
                  █████╗ ██╗██████╗                          
                 ██╔══██╗██║██╔══██╗                         
                 ███████║██║██████╔╝                         
                 ██╔══██║██║██╔══██╗                         
                 ██║  ██║██║██║  ██║                         
                 ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝[red] [cyan]                      
                                                            
 ██████╗ ███╗   ██╗████████╗ █████╗ ██████╗ ██╗ ██████╗     
██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔═══██╗    
██║   ██║██╔██╗ ██║   ██║   ███████║██████╔╝██║██║   ██║    
██║   ██║██║╚██╗██║   ██║   ██╔══██║██╔══██╗██║██║   ██║    
╚██████╔╝██║ ╚████║   ██║   ██║  ██║██║  ██║██║╚██████╔╝    
 ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝[cyan][magenta]
Nikhil Doal[magenta]\n
""")

#Function to create a flight schedule table. This uses the Rich library and creates a table with the 
#necessary data for each flight
def create_flight_table():
    table = Table(title="Flight Schedule\nFor 2024-07-05", box=box.SQUARE)
    table.add_column("[bold white]Destination[/bold white]", justify="center")
    table.add_column("[bold white]Departure Time[/bold white]", justify="center")
    table.add_column("[bold white]Arrival Time[/bold white]", justify="center")
    table.add_column("[bold white]Flight Number[/bold white]", justify="center")
    table.add_column("[bold white]Terminal[/bold white]", justify="center")
    table.add_column("[bold white]Status[/bold white]", justify="center")
    table.add_column("[bold white]Date[/bold white]", justify="center")
    table.add_column("[bold white]Carousel[/bold white]", justify="center")
    table.add_column("[bold white]Code[/bold white]", justify="center")

# Loop through each flight and add its details to the table
    for i in range(len(flights) - 1):
        flight = flights[i]
        status = flight[5]
        if status == "Arrived":
            status_color = "dark_green"
        elif status == "On Time":
            status_color = "green"
        elif status == "Delayed":
            status_color = "yellow"
        else:
            status_color = "red"
        row_color = "cyan" if i % 2 == 0 else "white"
        if status == "Arrived":
            status_text = "[bold " + status_color + "]" + flight[5] + "[/bold " + status_color + "]"
        else:
            status_text = "[" + status_color + "]" + flight[5] + "[/" + status_color + "]"
        table.add_row(
            "[" + row_color + "]" + flight[0] + "[/" + row_color + "]",
            "[" + row_color + "]" + flight[1] + "[/" + row_color + "]",
            "[" + row_color + "]" + flight[2] + "[/" + row_color + "]",
            "[" + row_color + "]" + flight[3] + "[/" + row_color + "]",
            "[" + row_color + "]" + flight[4] + "[/" + row_color + "]",
            status_text,
            "[" + row_color + "]" + flight[6] + "[/" + row_color + "]",
            "[" + row_color + "]" + flight[7] + "[/" + row_color + "]",
            "[" + row_color + "]" + flight[8] + "[/" + row_color + "]"
        )
    return table

# Display the flight schedule table
console.print(create_flight_table())

# Prompt user for their name and greet them
console.print("\n[bold white]Welcome to[/bold white] [red]AIR ONTARIO[red][bold white]![/bold white]")
name = console.input("\nWhat is your name?: ")
console.print(f"[white]\nHi [bold gold3]{name}[/bold gold3]! Please follow the steps below to get your ticket.[white]")

# Function to select a location from the available flights
def select_location():
    console.print("\n[bold]1. Choose a Location[/bold]\n")
    for i in range(len(flights)):
        console.print(str(i + 1) + ". [bold]" + flights[i][0] + "[/bold]: [green]$" + flights[i][9] + "[/green]")
#A while toop is used to check for a valid input, ensuring that the program does not crash when the user 
#enters an incorrect input. Flights that have arrived or been cancelled are excluded.
    valid = False
    while not valid:
        try:
            location = input("Choose your preferred location(1-12): ")
            if location in ["4", "11"]:
                console.print("[yellow]Unfortunately this flight has been cancelled, we are sorry for this inconvenience.[yellow]\n[red]Please choose another destination[red]")
                valid = False
            elif location in ["1", "2"]:
                console.print("[green]This flight has already arrived.[green]\n[red]Please choose another destination[red]")
            elif location not in ["3", "5", "6", "7", "8", "9", "10", "12"]:
                console.print("[bold dark_red]Please enter a valid input[/bold dark_red]")
                valid = False                
            else:
                console.print(f"The location you chose is: [bold red]{flights[int(location)-1][0]}[/bold red], which will cost ${flights[int(location)-1][9]}")
                valid = True
        except:
            console.print("[bold red]Please enter a valid input[/bold red]")
    return location

# Function to select a seat class. A list of all the seats are printed and the user can select a seat from the
# options. Validation is done again.
def select_seat_class():
    console.print("\n[bold]2. Select Seat Class[/bold]\n")
    console.print("[bold white]Available Seat Classes:[/bold white]")
    console.print("1. [white]Economy: [white][bold green]$100[/bold green]")
    console.print("2. [white]Business: [white][bold green]$300[/bold green]")
    console.print("3. [white]First Class: [white][bold green]$500[/bold green]")
    valid = False
    while not valid:
        try:
            seat_class = input("Choose your preferred seat class (Enter 1, 2 or 3): ")
            if seat_class not in ["1", "2", "3"]:
                console.print("[bold dark_red]Please enter a valid input[/bold dark_red]")
                valid = False
            else:
                console.print(f"The seat class you chose is: [bold red]{seat_prices[int(seat_class)-1][0]}[/bold red], which will cost ${seat_prices[int(seat_class)-1][1]}")
                valid = True
        except:
            console.print("[bold red]Please enter a valid input[/bold red]")
    return seat_class

# Function to select the number of bags. Validation is done again
def select_num_bags():
    console.print("\n[bold]3. Baggage[/bold]\n")
    console.print("[white]Checked Bags: [white][bold green]$30[/bold green]")
    console.print("[white]Carry On Bags: [white][bold green]$15[/bold green]")
    console.print("[red]There is a limit of 2 Checked and 2 Carry On Bags per Passenger[/red]")
    valid = False
    while not valid:
        try:
            checked = input("Number of Checked Bags (0-2): ")
            carryon = input("Number of Carry-On Bags (0-2): ")
            if checked not in ["0", "1", "2"] or carryon not in ["0", "1", "2"]:
                console.print("[bold dark_red]Please enter a valid input[/bold dark_red]")
                valid = False
            else:
                valid = True
        except:
            console.print("[bold red]Please enter a valid input[/bold red]")
    return checked, carryon

# Function to create and display the ticket. This is a summary of the information the user has inputted.
def create_ticket(name, location, seat_class, checked, carryon, total, taxed):
    table = Table(title="Your Ticket - [bold red]Air Ontario[/bold red]", box=box.ROUNDED)
    table.add_column("[bold white]Item[/bold white]", justify="left")
    table.add_column("[bold white]Details[/bold white]", justify="left")
    table.add_column("[bold white]Price[/bold white]", justify="right")

    table.add_row("[bold white]Name[/bold white]", f"[bold white]{name}[/bold white]", "")
    table.add_row("[bold white]Destination[/bold white]", f"[bold white]{flights[int(location)-1][0]}[/bold white]", f"[bold green]${flights[int(location)-1][9]}[/bold green]")
    table.add_row("[bold white]Departure Time[/bold white]", f"[bold white]{flights[int(location)-1][1]}[/bold white]", "")
    table.add_row("[bold white]Arrival Time[/bold white]", f"[bold white]{flights[int(location)-1][2]}[/bold white]", "")
    table.add_row("[bold white]Flight Number[/bold white]", f"[bold white]{flights[int(location)-1][3]}[/bold white]", "")
    table.add_row("[bold white]Seat Class[/bold white]", f"[bold white]{seat_prices[int(seat_class)-1][0]}[/bold white]", f"[bold green]${seat_prices[int(seat_class)-1][1]}[/bold green]")
    table.add_row("[bold white]Checked Bags[/bold white]", f"[bold white]{checked}[/bold white]", f"[bold green]${int(checked) * 30}[/bold green]")
    table.add_row("[bold white]Carry-On Bags[/bold white]", f"[bold white]{carryon}[/bold white]", f"[bold green]${int(carryon) * 15}[/bold green]")
    table.add_row("[bold white]Subtotal[/bold white]", "", f"[bold green]${total}[/bold green]")
    table.add_row("[bold white]Total (with tax)[/bold white]", "", f"[bold green]${taxed:.2f}[/bold green]")

    console.print(table)

# Function to calculate the final price and create the ticket. This function uses all the other functions and 
#calculates the final cost. It also displays the ticket and prompts the user to add another ticket
def calculate_final_price(name):
    location = select_location()
    seat_class = select_seat_class()
    checked, carryon = select_num_bags()

    total = 0
    total += int(flights[int(location)-1][9])
    total += int(seat_prices[int(seat_class) - 1][1])
    total += int(checked) * 30
    total += int(carryon) * 15
    taxed = total * 1.13
    console.print(f"\nYour subtotal not including taxes is ${total}")
    console.print(f"\nYour total with taxes is ${taxed:.2f}\n\n")
    create_ticket(name, location, seat_class, checked, carryon, total, taxed)

    # Check if the user wants to purchase another ticket
    again = console.input("\n[cyan]Would you like to purchase another Ticket? \n[bold red](Please enter \"Y\" for Yes, or enter anything else to exit)[/bold red][cyan]")
    if again == "Y":
        create_flight_table()
        name = console.input("\nName: ")
        calculate_final_price(name)
        valid = True

# Start the ticket purchasing process
calculate_final_price(name)

# Print a thank you message
console.print("\nThank you for choosing [red bold]Air Ontario[/red bold]. Have a great flight!\n")
console.print("""[yellow]
.-.
 \  `.
  \    `-.________________
   \_____                []`-.
   <____()-=O=O=O=O=O=[]====--)
     `.___ ,-----,_______...-'
          /    .'
         /   ,'
        /_ ,      [yellow]    
""")
