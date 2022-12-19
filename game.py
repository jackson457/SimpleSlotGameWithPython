import random
MAX_LINES=3
MIN_BET=1
MAX_BET=500

###define row and column ######
ROWS=3
COLS=3

######default vale#####
symbol_count={
	"A" : 2,
	"B" : 4,
	"C" : 6,
	"D" : 8,
	}
symbol_value={
	"A" :5,
 "B" :4,
 "C" :3,
 "D" :2,
	}
####Color#####
RED="\033[1;31m"
GREEN="\033[0;32m"
COLOR_RESET="\033[0m"

#####Spin machine #######
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range (cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

####### Print slot machine #####
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print (column[row], end= " | " )
            else:
                print(column[row],end="")
        print()
    	             
#######check winning #####
def check_winning(columns,lines,bet,symbol_value):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_value[symbol] * bet
            winning_line.append(line + 1)
    return winnings,winning_line
##### amount_to_deposit ########
def deposit():
    while True:
      amount=input("Enter amount to deposit $")
      if amount.isdigit():
         amount=int(amount)
         if amount >0:
            break 
         else:
            print("Amount must be greater than")
      else:
           print("You must enter number")
    return amount

###### get number ######
def get_number_of_lines():
    while True:
      lines=input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
      if lines.isdigit():
         lines=int(lines)
         if 1 <= lines <= MAX_LINES:
            break
         else:
            print("Enter a valid number of lines.")
      else:
           print("You must enter number")
    return lines

####### get_amount_to_bet ########
def get_bet():
    while True:
      amount = input(" How much would you like to bet on each line $  ")
      if amount.isdigit(): 
         amount=int(amount)
         if MIN_BET <= amount <= MAX_BET:
            break
         else:
            print(f"Enter a valid number between {MIN_BET}-{MAX_BET}")
      else:
           print("You must enter number")
    return amount

####Hame,########

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet= bet * lines
        if total_bet > balance:
            print(f"You do not have that amount to be.Your current balance is ${balance}")
        else:
            break
    print(f"You are betting {bet} on {lines} lines.Total bet is {total_bet}")
    slot=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slot)
    winning , winning_line=check_winning(slot,lines,bet,symbol_value)
    print(f"You won ${winning}")
    print(f"You won on lines: ",*winning_line)
    return winning - total_bet
###### Main function ######
def main():
    balance=deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer=input("Press enter to play q to quit: ")
        if answer == 'q':
             break
        balance += spin(balance)
        print(f"You left ${balance}")
main()
