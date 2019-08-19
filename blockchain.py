#initilize our blockchain list
blockchain = []


def get_last_blockchain_value():
    ''' Returns the last vaule of the current blockchain'''
    return blockchain[-1]


def add_value(transaction_amount,last_transaction=[1]):
  ''''Append a new value as weel as the last blockchain value to the blockchain'''
  blockchain.append([last_transaction,transaction_amount])


def get_transcation_value():
    ''' Returns the input of the users ( a new transcation amount) to blockchain'''
    user_input = float(input('Your transcation amount please: '))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    #output the blockain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

#get the first transcation input and add the value to the blockchain
tx_amount = get_transcation_value()
add_value(tx_amount)


while True:
    print('Please choose')
    print('1: Add a new transcation value')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transcation_value()
        add_value(tx_amount,get_last_blockchain_value())
    else:
        print_blockchain_elements()


   


print('Done!!!!')
