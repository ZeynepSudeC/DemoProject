
row1 = ["⬜️","⬜️","⬜️"] 
row2 = ["⬜️","⬜️","⬜️"] 
row3 = ["⬜️","⬜️","⬜️"] 

map = [row1,row2,row3]


position = input("Where do you want to put the treasure?")

horizantol = int(position[0]) #2
vertical = int(position[1]) #3

#selected_row = map[horizantol - 1]
#selected_row[vertical - 1] = "X"

map[horizantol - 1][vertical - 1] = "X"


print(f'{row1}\n{row2}\n{row3}')