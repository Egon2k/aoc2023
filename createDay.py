import os

# ask for day
day = input("Enter day: ")

if 1 <= int(day) <= 24:
    folder = f'day{int(day):02d}'
    
    if not os.path.exists(f'{folder}'):
        os.mkdir(f'{folder}')
        os.system(f'cp ./day00/template.py ./{folder}/solution.py')
        open(f'./{folder}/data.txt', 'a').close()
    else:
        print(f'Folder {folder} already exists...')
    
else:
    print(f'Do you know how an advent calender works? Enter number between 1 and 24...')

