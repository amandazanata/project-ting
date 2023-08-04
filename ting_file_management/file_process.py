from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):

    for dictionary in instance.data:
        if dictionary["nome_do_arquivo"] == path_file:
            return None
    list = txt_importer(path_file)
    new_dictionary = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list),
        "linhas_do_arquivo": list
    }
    instance.enqueue(new_dictionary)
    print(new_dictionary)


def remove(instance):

    if len(instance) == 0:
        print("Não há elementos")
    else:
        clear = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {clear} removido com sucesso")


def file_metadata(instance, position):

    try:
        dictionary = instance.search(position)
        print(dictionary)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
