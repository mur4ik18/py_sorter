import os 
files_moved = 0

folder = "~/Documents"

if os.path.isdir(os.path.expanduser(f'{folder}/zips')) == False:
    os.mkdir(os.path.expanduser(f'{folder}/zips'))
if os.path.isdir(os.path.expanduser(f'{folder}/photos')) == False:
    os.mkdir(os.path.expanduser(f'{folder}/photos'))
if os.path.isdir(os.path.expanduser(f'{folder}/pdfs')) == False:
    os.mkdir(os.path.expanduser(f'{folder}/pdfs'))   
if os.path.isdir(os.path.expanduser(f'{folder}/words')) == False:
    os.mkdir(os.path.expanduser(f'{folder}/words'))   

for i in os.listdir(os.path.expanduser(f'{folder}')):
    if i.endswith('.pdf'):
        os.replace(os.path.expanduser(f'{folder}/{i}'), os.path.expanduser(f'{folder}/pdfs/{i}'))
        files_moved += 1
    elif i.endswith('.docx') or i.endswith('.doc') or i.endswith('.txt') or i.endswith('.xlsx') or i.endswith('.xls') or i.endswith('.pptx') or i.endswith('.ppt') or i.endswith('.csv') or i.endswith('.odt'): 
        os.replace(os.path.expanduser(f'{folder}/{i}'), os.path.expanduser(f'{folder}/words/{i}'))
        files_moved += 1
    elif i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg'):
        os.replace(os.path.expanduser(f'{folder}/{i}'), os.path.expanduser(f'{folder}/photos/{i}'))
        files_moved += 1
    elif i.endswith('.zip'):
        os.replace(os.path.expanduser(f'{folder}/{i}'), os.path.expanduser(f'{folder}/zips/{i}'))
        files_moved += 1

print(f"Nombre total de fichiers déplacés : {files_moved}")