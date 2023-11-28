from crud import Crud

table = Crud(
    user = 'postgres',
    password = 'bmsce61911',
    host = '127.0.0.1',
    port = '5432',
    dbname = 'postgres',
    table = 'users',
    primarykey = 'u_id'
)

table.connect()


table.insert(
    u_id = '1',
    name = 'Mahesh'
)


table.insert_many(
    columns = ('u_id', 'name'),
    rows = [
        ['2', 'Lex'],
        ['3', 'Chad']
    ]
)

table.delete(
    primaryKey_value = '1'
)

table.select(
    columns = ['name']
)



table.update(
    column = 'name',
    column_value = 'Ahmed',
    primaryKey_value = '3'
)


# table.update_multiple_columns(
#     columns = ['city', 'address'],
#     columns_value = ['qena', 'upperEgypt'],
#     primaryKey_value = 'luxor'
# )

# table.delete_all()

table.commit()

table.close("commit")




