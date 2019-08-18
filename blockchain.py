#initilize our blockchain list
blockchain = []


def get_last_blockchain_value():
    ''' Returns the last vaule of the current blockchain'''
    return blockchain[-1]


def add_value(transaction_amount,last_transaction=[1]):
  ''''Append a new value as weel as the last blockchain value to the blockchain'''
    blockchain.append([last_transaction,transaction_amount])


def get_user_input():
    ''' Returns the input of the users ( a new transcation amount) to blockchain'''
    return float(input('Your transcation amount please: '))


tx_amount = get_user_input()
add_value(tx_amount)


tx_amount = get_user_input()                                                                           
add_value(last_transaction=get_last_blockchain_value(),transaction_amount=tx_amount)


tx_amount = get_user_input() 
add_value(tx_amount,get_last_blockchain_value())


print(blockchain)