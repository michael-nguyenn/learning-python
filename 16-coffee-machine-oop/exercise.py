from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

# Accessing object attributes
table.align = "l"

print(table)
