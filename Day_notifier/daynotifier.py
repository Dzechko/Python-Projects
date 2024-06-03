from datetime import datetime


def keepCount():
    with open('file.txt', 'r') as r:
        lines = r.readlines()
    count = int(lines[2].split('=')[1])
    count += 1

    # update the count
    lines[2] = f"count = {count}\n"
    # write the updated count into the file
    with open("file.txt", "w") as r:
        r.writelines(lines)
    return count


def updateData(condition):
    if condition == "y":
        date_str = input("Enter current date in format {YYYY-MM-DD}: ")
        time_str = input("Enter current time in format {Hour:Minute:Seconds}: ")

        try:

            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            time_obj = datetime.strptime(time_str, "%H:%M:%S").time()
        except ValueError:
            print(
                "Invalid date or time entered. Please enter dates in YYYY-MM-DD format and times in "
                "Hour:Minute:Seconds format.")
            return None

        with open('file.txt', 'r') as file:
            lines = file.readlines()

        lines[0] = f"date = {date_str}\n"
        lines[1] = f"time = {time_str}\n"

        with open('file.txt', 'w') as file:
            file.writelines(lines)

        current_date_time = datetime.combine(date_obj, time_obj)
        times = keepCount()
        print(f"{times} times since 2024-05-01, 12:00:00")
        return current_date_time

    if condition == "n":
        with open('file.txt') as r:
            lines = r.readlines()

            date_line = lines[0].strip().split("=")
            time_line = lines[1].strip().split("=")

            date_obj = datetime.strptime(date_line[1], " %Y-%m-%d")
            time_obj = datetime.strptime(time_line[1], " %H:%M:%S").time()

            current_datetime = datetime.combine(date_obj, time_obj)

            count = int(lines[2].split("=")[1])
            print(f"{count} times since 2024-05-01, 12:00:00")

        return current_datetime


def calculateTime(datetime2):
    datetime1 = datetime.now()
    return datetime1 - datetime2


def doFormat(value):
    value = str(value)
    if "," in str(value):
        s = value.split(",")
        final = s[1].split(":")
        print(f"it was exactly {s[0]} {final[0]} hours and {final[1]} minutes ago")
    else:
        l = value.split(":")
        print(f"it was exactly {l[0]} hours {l[1]} minutes ago")


condition = input("is there any update? (y/n): ")
y = calculateTime(updateData(condition.lower()))
doFormat(y)
