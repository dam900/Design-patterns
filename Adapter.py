
# The goal of this project is to present the skill of implementation
# and using Adapter design pattern

# class that operates on dictionaries
# Target
class DictClass:

    def print_dict(self, dictionary: dict) -> None:
        i = 0
        for key, item in dictionary.items():
            print(f'Element {i} in dictionary -> {key, item}')
            i += 1


# class that operates on lists
# Adaptee
class ListClass:

    def print_list(self, ls: list[tuple]) -> None:
        i = 0
        for item in ls:
            print(f'Element {i} in list -> {item[0], item[1]}')
            i += 1


class Adapter(DictClass, ListClass):

    def print_dict(self, dictionary) -> None:
        pass
        if isinstance(dictionary, dict):
            DictClass.print_dict(self, dictionary)
        elif isinstance(dictionary, list):
            dc_from_ls = {item[0]: item[1] for item in dictionary}
            DictClass.print_dict(self, dc_from_ls)


def some_function(operator: "DictClass", colection) -> None:
    operator.print_dict(colection)


if __name__ == '__main__':
    items_dict = {'color': 'black', 'number': 123, 123: 'one_two_three'}
    items_list = [('color', 'black'), ('number', 123), (123, 'one_two_three')]

    dict_operator = DictClass()
    list_operator = ListClass()
    adapter = Adapter()

    print('-' * 20, 'DictClass', '-' * 20)
    some_function(dict_operator, items_dict)
    print('-' * 20, 'Adapter', '-' * 20)
    # dict_operator.print_dict(items_list) raises error
    some_function(adapter, items_list)
    print('-' * 20, 'Adapter', '-' * 20)
    some_function(adapter, items_dict)
    print('-' * 20, 'ListClass', '-' * 20)
    list_operator.print_list(items_list)
