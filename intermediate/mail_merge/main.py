
with open("intermediate/mail_merge/name_list.txt") as file:
    contents = file.read()

names = contents.split('\n')

for name in names:
    file = open(f"intermediate/mail_merge/invites/{name}.txt", mode='w')
    file.write(f'''Dear {name},
    You are invited to my birthday this weekend.
    ''')

