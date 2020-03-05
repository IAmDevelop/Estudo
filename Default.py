import Conexao
print("\n Conexao com o MySql - Primeiro Modo \n")
Conexao.ConectarMySQL2("u355583042_studio", "asenhaestacerta")
print("\n Conexao com o MySql - Segundo Modo \n")
Conexao.ConectarMySQL("u355583042_studio", "asenhaestacerta")
print("\n Conexao com o SQLServer \n")
Conexao.ConectarSQLServer('sa', 'sahnes10')
