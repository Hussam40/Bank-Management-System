import os
import time
import random
import string

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

numbers = string.digits

class Client:
    def __init__(self, c_name, c_phone, c_money):
        self.c_name = c_name
        self.c_phone = c_phone
        self.c_money = c_money
        self.account_ID = ''.join(random.choices(numbers, k=5))

        self.c_status = 'Important client' if c_money >= 1000000 else 'Normal client'

    def print_info(self):
        print(f"[{self.account_ID}] Name: {self.c_name}")
        print(f"      Phone: {self.c_phone}")
        print(f"      Balance: ${self.c_money:,.2f}")
        print(f"      Status: {self.c_status}")
        print("-" * 35)

class HussamBank:
    def __init__(self):
        self.clients = []

    def add_new_client(self):
        clear_screen()
        print("--- Registration Form ---")
        c_name = input("Enter client full name: ").strip().capitalize()
        
        while True:
            c_phone = input("Enter phone number: ").strip()
            if c_phone.isdigit() and len(c_phone) >= 8:
                break
            print("Error: Please enter a valid phone number (digits only).")

        while True:
            try:
                c_money = float(input("Enter initial deposit amount: "))
                if c_money < 0:
                    print("Error: Money cannot be negative.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid numeric amount.")

        new_obj = Client(c_name, c_phone, c_money)
        self.clients.append(new_obj)
        print(f"\nDone! Client assigned ID: {new_obj.account_ID}")
        input("Press enter to continue")

    def display_all(self):
        clear_screen()
        if not self.clients:
            print("The bank database is currently empty.")
        else:
            print(f"Total Clients: {len(self.clients)}\n" + "="*35)
            for c in self.clients:
                c.print_info()
        input("\nPress Enter to go back...")

    def search_for_client(self):
        clear_screen()
        if not self.clients:
            print("No data available to search.")
            time.sleep(2)
            return

        query = input("Search by Name or Account ID: ").lower()
        results = [c for c in self.clients if query in c.c_name.lower() or query == c.account_ID]
        
        print("\n--- Search Results ---")
        if results:
            for c in results:
                c.print_info()
        else:
            print("No matches found.")
        input("\nPress Enter to continue...")

    def run(self):
        while True:
            clear_screen()
            print("      HUSSAM CENTRAL BANK      ")
            print("===============================")
            print("1) Open New Account")
            print("2) Directory (All Clients)")
            print("3) Search Database")
            print("4) Terminate System")
            print("===============================")
            
            choice = input("Select Option: ")

            if choice == '1':
                self.add_new_client()
            elif choice == '2':
                self.display_all()
            elif choice == '3':
                self.search_for_client()
            elif choice == '4':
                print("\nSystem shutting down... Goodbye!")
                break
            else:
                print("\nInvalid command!")
                time.sleep(1)

if __name__ == "__main__":
    bank_system = HussamBank()
    bank_system.run()
