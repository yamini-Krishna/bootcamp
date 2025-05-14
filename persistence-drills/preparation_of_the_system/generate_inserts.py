with open("insert_commands.sql", "w") as f:
    for i in range(1, 501):
        f.write(f'INSERT INTO COMPANIES VALUES ("Company_{i}", {i});\n')
