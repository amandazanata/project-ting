def exists_word(word, instance):

    return aux_search(word, instance, include_content=False)


def search_by_word(word, instance):

    return aux_search(word, instance)


def aux_search(word, instance, include_content=True):
    def create_occurrence(index, line):
        occurrence = {"linha": index}
        if include_content:
            occurrence["conteudo"] = line
        return occurrence

    def has_word(line):
        return word.casefold() in line.casefold()

    new_instance = [
        {
            "palavra": word,
            "arquivo": dictionary["nome_do_arquivo"],
            "ocorrencias": [
                create_occurrence(index + 1, line)
                for index, line in enumerate(dictionary["linhas_do_arquivo"])
                if has_word(line)
            ]
        }
        for dictionary in instance.data
        if any(has_word(line) for line in dictionary["linhas_do_arquivo"])
    ]

    return new_instance
