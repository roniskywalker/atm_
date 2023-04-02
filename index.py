#private
acc_fname = 'Abc'
acc_sname = 'Xyz'
acc_phone = '999xxxx999'
acc_address = 'Mnoxxx, xfg'
acc_mpin = 1111
acc_tpin = 1234
acc_balance = 1000

min_balance = 500
min_deposit = 100
max_deposit = 100000

#public
import time

print('\n-----------------------------------')
print('            ATM Machine')
print('-----------------------------------\n')

print('Please insert your ATM Card\n')

time.sleep(3)

pin = int(input('Enter your 4 digit ATM mPin '))

if pin == acc_mpin:
    print(f'\nWelcome back {acc_fname},')
    while True:
        print('\n-----------------------------------')
        print('            Dash Board')
        print('-----------------------------------')
        print("1 = Account Information")
        print("2 = Withdraw Money")
        print("3 = Deposit Money")
        print("4 = Check Balance")
        print("5 = Change tPin")
        print("6 = Exit")
        option = int(input('\nChoose any option above '))
        if option<=6: 
            if option == 1:
                check_pin = int(input('\nEnter your tpin '))
                if check_pin == acc_tpin:
                    print(f'\nAccount Holder Name: {acc_fname} {acc_sname}')
                    print(f'Phone Number: {acc_phone}')
                    print(f'Address: {acc_address}')
                else:
                    print("\nYou have entered wrong pin")
            if option == 2:
                withdraw_money = int(input('\nEnter the withdraw amount '))
                check_pin = int(input('\nEnter your tpin '))
                if check_pin == acc_tpin:
                    left_money = acc_balance - withdraw_money
                    if left_money >= min_balance:
                        acc_balance -= withdraw_money
                        print(f'\nRs.{withdraw_money} is debited from your account')
                    else:
                        print('\nYou do not have sufficient balance')
                else:
                    print("\nYou have entered wrong pin")
            if option == 3:
                deposit_money = int(input('\nEnter the deposit amount '))
                if deposit_money>=min_deposit and deposit_money<=max_deposit:
                    acc_balance += deposit_money
                    print(f'\nRs.{deposit_money} is credited to your account')
                else:
                    print("\nYour deposit amount is not valid")
            if option == 4:
                check_pin = int(input('\nEnter your tpin '))
                if check_pin == acc_tpin:
                    print(f'\nYour current balance is Rs.{acc_balance}')
                else:
                    print("\nYou have entered wrong pin")
            if option == 5:
                check_pin = int(input('\nEnter your previous tpin '))
                if check_pin == acc_tpin:
                    acc_newtpin = int(input('\nEnter the new tpin '))
                    acc_tpin = acc_newtpin
                    print("\ntPin is Successfully changed")
                else:
                    print("\nPlease enter correct tpin")
            if option == 6:
                print('\nThank you for visiting ATM Machine.\n')
                break
        else:
            print("\nPlease choose the valid option")

else:
    print('\nYou have entered the wrong pin. Try Again\n')
