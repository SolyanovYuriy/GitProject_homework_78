def get_extension(file_name: str) -> str:
    """
    Возвращает расширение файла в виде строки
    :param file_name (str): строка, название файла
    :return:
            str: строка, расширение файла
    """
    file_list = file_name.split(".")
    if len(file_list) <= 1:
        raise Exception(f"Файл '{file_list}' не имеет расширения!")
    else:
        return file_list[-1]


def execute_application():
    file_name = input("Введите название файла с расширением: ")
    try:
        extension = get_extension(file_name)
        print(f"Файл '{file_name}' имеет расширение '{extension}'")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    execute_application()
