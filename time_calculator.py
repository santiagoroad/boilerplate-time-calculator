def add_time(start, duration, dayofweek=""):
  # Variables
  new_time = ""
  dayspassed = 0
  daysweek = [
      "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
      "sunday"
  ]

  # To abtain the data needed to solve the problem
  hour, complement = start.split()
  starthour, startminutes = hour.split(":")
  addhour, addminutes = duration.split(":")

  # To know the result of the minutes
  if ((int(startminutes) + int(addminutes)) >= 60):
    addhour = int(addhour) + 1
    startminutes = (int(startminutes) + int(addminutes)) - 60
  else:
    startminutes = (int(startminutes) + int(addminutes))

  #To know the result of the hour and how many days had passed
  # I add 12 to change the format to 24 hours
  if complement == "PM":
    starthour = int(starthour) + 12

  # To calculate the result of the hour
  # I divide the hours to add into 24, because i need the days that had paseed and the rest of the hours I'm going to add.
  if ((int(addhour)) >= 24):
    dayspassed = int(addhour) // 24
    addhour = int(addhour) % 24

  # Add the initial time to the time that need's to be added, if the result is bigger than 24, i  add a day and subtract 24 to the sum
  if (int(starthour) + int(addhour)) >= 24:
    starthour = (int(starthour) + int(addhour)) - 24
    dayspassed += 1
  else:
    starthour = (int(starthour) + int(addhour))

  # Validations to construct the answer, chage the information back to format 12 hours
  if int(starthour) == 0:
    starthour = str(12)
    complement = "AM"
  elif int(starthour) == 12:
    complement = "PM"
  elif int(starthour) > 12:
    starthour = int(starthour) - 12
    complement = "PM"
  else:
    complement = "AM"

  if startminutes < 10:
    startminutes = '0' + str(startminutes)

  # Validate day of the week.
  if dayofweek != "":
    dayweek = daysweek.index(dayofweek.lower())

    if dayspassed == 0:
      complement += ", " + daysweek[dayweek].title()
    else:
      if (len(daysweek) - dayweek) > dayspassed:
        complement += ", " + daysweek[dayweek + dayspassed].title()
      else:
        complement += ", " + daysweek[(dayspassed + dayweek) %
                                      len(daysweek)].title()

  if dayspassed == 1:
    new_time = str(starthour) + ":" + str(
        startminutes) + " " + complement + " (next day)"
  elif dayspassed > 1:
    new_time = str(starthour) + ":" + str(
        startminutes) + " " + complement + " (" + str(
            dayspassed) + " days later)"
  else:
    new_time = str(starthour) + ":" + str(startminutes) + " " + complement

  return new_time
