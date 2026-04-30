import random
import string
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

numbers = string.digits

class Client:
    def __init__(self, c_name, c_phone, c_money, account_ID, c_status):
        self.c_name = c_name
        self.c_phone = c_phone
        self.c_money = c_money
        self.account_ID = account_ID
        self.c_status = c_status
    
    def print_info(self):
        print(f'Client name: {self.c_name}')
        print(f'Client phone number: {self.c_phone}')
        print(f'Client money: {self.c_money}')
        print(f'Client ID: {self.account_ID}')
        print(f'Client status: {self.c_status}')
        print('_' * 20)

def new_client():
    c_name = input('Enter the name: ')
    c_phone = input('Enter the phone number: ')
    while True:
        try:
            c_money = int(input('Enter the money: '))
            break
        except ValueError:
            print('Please enter a valid number.')
    account_ID = ''.join(random.choices(numbers, k = 4))

    if c_money < 1000000:
        c_status = 'Normal client'
    else:
        c_status = 'Important client'

    return Client(c_name, c_phone, c_money, account_ID, c_status)

def search(clients):
    if not clients:
        print('\nSorry, There is no client to search!')
        time.sleep(3)
        return
    
    print('\n--- Search Menu ---')
    search_choice = input('Search by (1) Account ID or (2) Name: ').strip()
    
    found = False
    
    if search_choice == '1':
        search_id = input('Enter Account ID: ').strip()
        for c in clients:
            if c.account_ID == search_id:
                print('\nClient Found:\n')
                c.print_info()
                found = True
                break
                
    elif search_choice == '2':
        search_name = input('Enter Client Name: ').strip().lower()
        for c in clients:
            if search_name in c.c_name.lower():
                print('\nClient Found:\n')
                c.print_info()
                found = True
                
    else:
        print('\nInvalid choice!')
        time.sleep(2)
        return

    if not found:
        print('\nNo client matches your criteria.')
    
    time.sleep(5)

clients = []

while True:
    clear_screen()
    print('''
| Welcome to Hscoo Bank |

Choose an action:

1. Add a new client
2. Display all clients
3. Search for client
4. Exit''')
    
    choice = input('\nEnter your choice: ')

    if choice == '1':
        time.sleep(1)
        clear_screen()
        clients.append(new_client())
        print('\nClient added successfully!')
        time.sleep(2)

    elif choice == '2':
        if clients:
            time.sleep(1)
            clear_screen()
            print('Displaying all clients:\n')
            
            for c in clients:
                time.sleep(3)
                c.print_info()
            print('\nDisplaying is finished.')
            time.sleep(8)
        
        else:
            print('\nSorry, There is no clients to display!')
            time.sleep(3)

    elif choice == '3':
        time.sleep(1)
        clear_screen()
        search(clients)

    elif choice == '4':
        print('\nExiting...')
        time.sleep(2)
        break 
    
    else:
        print('\nError, Please choose from the options!')
        time.sleep(2)