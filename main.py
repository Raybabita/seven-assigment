import csv

with open("names.csv", mode="w") as newCsvfile:
    fieldNames = ["name", "city", "phone"]
    writer = csv.DictWriter(newCsvfile, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerow(
        {"name": "sree", "city": "hyderabad", "phone": "989384903"})
    writer.writerow({"name": "RAM", "city": "bengalore", "phone": "989384903"})
    writer.writerow(
        {"name": "ganesh", "city": "vadodara", "phone": "989384903"})
    writer.writerow({"name": "golu", "city": "bhopal", "phone": "989384903"})
    writer.writerow({"name": "brad", "city": "agra", "phone": "989384903"})
