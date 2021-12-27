from jsonreader import jsonreader_from_dict
import json
import os
import re


# PATH_CWD = os.getcwd().replace("\\",'/')
PATH_NOW = os.path.dirname(os.path.realpath(__file__)).replace("\\", '/')
JSON_FILE = "data.json"
JSON_PATH = PATH_NOW+"/"+JSON_FILE


def json_reader() -> dict:
    with open(JSON_PATH, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    return data


def findWord(word, source) -> bool:
    return True if re.search(r'\b({0})\b'.format(word), source, flags=re.IGNORECASE) else False


def sbT_decorator(func):
    def inner_decorator(arg_mt):
        books_collection = func(arg_mt)
        for i in books_collection:
            print("\n\nBook Title : {} \nBook ISBN : {} \nBook Authors : {} \nBook Categories : {} \n"
                  .format(i["title"], i["isbn"], ", ".join(i["authors"]),", ".join( i["categories"])))
        return books_collection
    return inner_decorator

def sbI_decorator(func):
    def inner_decorator(arg_mt):
        books_collection = func(arg_mt)
        for i in books_collection:
            print("\n\nBook Title : {} \nBook ISBN : {} \nBook Authors : {} \nBook Categories : {} \nBook Description : {} \n"
                  .format(i["title"], i["isbn"], ", ".join(i["authors"]),", ".join( i["categories"]), i["shortDescription"]))
        return books_collection
    return inner_decorator

def sbA_decorator(func):
    def inner_decorator(arg_mt):
        books_collection = func(arg_mt)
        for i in books_collection:
            print("\n\nBook Title : {} \nBook ISBN : {} \nBook Authors : {} \nBook Categories : {} \n"
                  .format(i["title"], i["isbn"], ", ".join(i["authors"]),", ".join( i["categories"])))
        return books_collection
    return inner_decorator

def sbC_decorator(func):
    def inner_decorator(arg_mt):
        books_collection = func(arg_mt)
        for i in books_collection:
            print("\n\nBook Title : {} \nBook ISBN : {} \nBook Authors : {} \nBook Categories : {} \n"
                  .format(i["title"], i["isbn"], ", ".join(i["authors"]),", ".join( i["categories"])))
        return books_collection
    return inner_decorator

@sbT_decorator
def searcbyTitle(json_str):
    input_t = str(input("Input Book Title : "))
    books_collection = []
    for i in json_str:
        if findWord(input_t, i["title"]):
            books_collection.append(i)
    return books_collection

@sbI_decorator
def searcbyISBN(json_str):
    input_t = str(input("Input Book ISBN : "))
    books_collection = []
    for i in json_str:
        if input_t == i["isbn"]:
            books_collection.append(i)
    return books_collection

@sbA_decorator
def searcbyAuthors(json_str):
    input_t = str(input("Input Book Authors : "))
    books_collection = []
    for i in json_str:
        if input_t.casefold() in (authors.casefold() for authors in i["authors"]):
            books_collection.append(i)
    return books_collection

@sbC_decorator
def searcbyCategories(json_str):
    input_t = str(input("Input Book Categories : "))
    books_collection = []
    for i in json_str:
        if input_t.casefold() in (categories.casefold() for categories in i["categories"]):
            books_collection.append(i)
    return books_collection


def main():
    #json_result  = jsonreader_from_dict(json_reader())
    json_result = json_reader()
    flh = True
    while flh:
        print("Welcome to Simple Books Search Engine \n")
        print("1. Search Books By Title")
        print("2. Search Books By ISBN")
        print("3. Search Books By Authors")
        print("4. Search Books By Categories")
        print("5. Exit")
        input_menu = input("Select Menu : ")
        if input_menu == "1":
            searcbyTitle(json_result)
        elif input_menu == "2":
            searcbyISBN(json_result)
        elif input_menu == "3":
            searcbyAuthors(json_result)
        elif input_menu == "4":
            searcbyCategories(json_result)
        elif input_menu == "5":
            flh = False
            exit()
        else:
            pass


if __name__ == "__main__":

    main()
