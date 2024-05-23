from time import sleep
sec_clock = 0
min_clock = 0
hour_clock = 0
while True:
    print('''
    
    
    
    
    
    

    



    






    ''')
    print('='*30)
    print(f'''
{hour_clock:^9}:{min_clock:^10}:{sec_clock:^10}    
    ''')
    print('='*30)
    sleep(1)
    sec_clock += 1
    if sec_clock == 60:
        sec_clock -= 60
        min_clock += 1
    if min_clock == 60:
        min_clock -= 60
        hour_clock += 1