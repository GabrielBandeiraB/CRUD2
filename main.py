# %%
from proprietario_civil_crud import ProprietarioCivilCRUD
from proprietario_empresa_crud import ProprietarioEmpresaCRUD
from municipio_crud import MunicipioCRUD
from propriedade_crud import PropriedadeCRUD
from producao_crud import ProducaoCRUD
from esposa_crud import EsposaCRUD
from empregado_crud import EmpregadoCRUD

municipio_crud = MunicipioCRUD()
propriedade_crud = PropriedadeCRUD()
proprietario_civil_crud = ProprietarioCivilCRUD()
proprietario_empresa_crud = ProprietarioEmpresaCRUD()
producao_crud = ProducaoCRUD()
esposa_crud = EsposaCRUD()
empregado_crud = EmpregadoCRUD()


# %%
municipio_crud.ler_municipio()
propriedade_crud.ler_propriedade()
proprietario_civil_crud.ler_proprietario_civil()
producao_crud.ler_producao()
esposa_crud.ler_esposa()
empregado_crud.ler_empregado()

# %%
proprietario_civil_crud.inserir_proprietario_civil(
    "Proprietarioinserido", "ABC123", "12345678901", "1990-01-01", "1111111111", "2222222222", "3333333333")
proprietario_civil_crud.ler_proprietario_civil()
# %%
propriedade_crud.inserir_propriedade(
    8, "Propriedadeinserida", "2023-05-26", 10.5, 1, 100000.00, 20.5)
propriedade_crud.ler_propriedade()
# %%
producao_crud.inserir_producao(
    16, "Produtocriado", "2023-06-01", 100.0, 80.0, "2023-06-10")
esposa_crud.inserir_esposa(
    8, "Esposainserida", "12345678901", "1990-01-01", "2020-05-20", "ABC123")
empregado_crud.inserir_empregado(16, "Empregadoinserido", "1990-01-01")

# %%
municipio_crud.ler_municipio()
propriedade_crud.ler_propriedade()
proprietario_civil_crud.ler_proprietario_civil()
producao_crud.ler_producao()
esposa_crud.ler_esposa()
empregado_crud.ler_empregado()

# %%
proprietario_civil_crud.atualizar_proprietario_civil(
    8, "Novo Proprietario 1", "DEF456", "11122233344", "1995-05-05", "7777777777", "8888888888", "9999999999")
producao_crud.atualizar_producao(
    6, 16, "Novo Produto", "2023-06-02", 120.0, 100.0, "2023-06-11")


# %%
proprietario_civil_crud.excluir_proprietario_civil(8)
propriedade_crud.excluir_propriedade(16)


# %%
