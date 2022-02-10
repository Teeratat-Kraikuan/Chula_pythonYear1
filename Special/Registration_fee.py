def invalid_id(id):
    return (len(id) != 10 or int(id[:2]) < 50 or id[2] not in ['3','4','7'] or int(id[8:]) < 21 or int(id[8:]) > 27)

def calculate_price(id, sem):
    prices = [[[[['18,000'], ['21,000']], [['4,500'], ['5,250']]], [[['26,000'], ['31,000']], [['7,000'], ['7,750']]]], \
              [[[['14,500'], ['17,000']], [['4,500'], ['5,250']]], [[['19,000'], ['23,000']], [['7,000'], ['7,750']]]]]
    
    # a is Group
    # b is Bachelor or Graduated
    # c is sem
    # d is the first 2 char in id
    a = 0 if id[8:] in ['21', '23', '25', '28'] else 1
    b = 0 if id[2] in ['3', '4'] else 1
    c = 0 if sem in [1,2] else 1
    d = 0 if int(id[:2]) < 56 else 1

    return prices[a][b][c][d][0]

def main():
    id = input("Enter student ID : ")
    if invalid_id(id):
        print("Invalid ID")
        return
    
    sem = int(input("Enter semester : "))
    if sem < 1 or sem > 3:
        print("Invalid semester")
        return    
    
    price = calculate_price(id, sem)
    print("Registration fee : " + price)
    
main()