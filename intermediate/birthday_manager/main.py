from datetime import datetime
import smtplib
import random
import json

today = datetime.now()
day = today.strftime("%m-%d")
year = today.year


my_email = 'emrakhibragimov5@gmail.com'
password = 'rgbzaerhvevmdoou'

with open('intermediate/birthday_manager/birthdays.json') as file:
    emails = json.load(file)
    closest_people = []
    birth = None
    for email in emails:
        if day == email['birthday']:
            birth = email
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: {email['subject']}\n\n{email['body']}")
    if birth == None:
        for person in emails:
            birthday = person['birthday']
            convert = datetime.strptime(birthday, "%m-%d")
            convert_day = f"{convert.month:02d}-{convert.day:02d}"
            if today.month - convert.month == 0 and today.day - convert.day > 0:
                closest_people.append(person['name'])
        if len(closest_people) > 1:
            print(f"No birthdays today. However, {', '.join(closest_people[:-1]) + ' and ' + closest_people[-1]} have a birthday this month.")
        elif len(closest_people) == 1:
            print(f"No birthdays today. However, {closest_people[0]} has a birthday this month.")
        else:
            print(f"No birthdays today or this month.")
