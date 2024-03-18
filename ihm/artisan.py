import os, argparse, ast, re

PAGES_DIR = "src/pages/"
COMPONENTS_DIR = "src/components/"


def main():
    parser = argparse.ArgumentParser(description="CLI tool for project management.")
    parser.add_argument("command", choices=["make:page", "update"], help="Command to execute")
    parser.add_argument("--name", type=str, help="Name of the resource")

    args = parser.parse_args()

    if args.command == "make:page":
        if args.name:
            create_page(args.name.capitalize())
        else:
            print("Please provide a name for the page.")
    elif args.command == "update":
            update_main()

def update_main():
    PAGES_MODULE_NAME = "src.pages"
    imports = set()
    routes = {}

    # Collect all the pages for the imports and routes
    for filename in os.listdir(PAGES_DIR):
        if filename.endswith(".py"):
            imports.add(filename.split(".")[0])
            # Open the file and search for route in the __init__ method
            with open(PAGES_DIR + filename, "r") as file:
                python_code = file.read()
                # Regular expression pattern to match __init__ with route argument
                pattern = r"__init__\(.*?\n\s*route\s*=\s*\"(.*?)\""
                matches = re.findall(pattern, python_code)
                routes[filename.split(".")[0]] = matches[0]


    with open("main.py", "r") as file:
        main_ast = ast.parse(file.read(), "main.py")

    print(ast.dump(main_ast, indent=4))

    # for node in main_ast.body:
    #     if isinstance(node, ast.ImportFrom):
    #         if node.module == "src.pages":
    #             print(node.names)

    new_import_statements = f"from {PAGES_MODULE_NAME} import {', '.join(imports)}\n"


    print()
    print("main.py updated successfully.")


def generate_page(page_name):
    class_name = page_name.capitalize() + "Page"
    code = f"""import flet as ft

    class {class_name}(ft.View):

    def __init__(self, page: ft.Page):
        super({class_name}, self).__init__(
            route="/{page_name.lower()}",
        )
        self.page = page
        self.page.title = "{page_name} page"

        self.controls = [
            ft.Container(
                content=ft.Text("{page_name}", size=30),
                padding=ft.padding.symmetric(vertical=50),
            )
        ]"""

    return code


def save_to_file(code, page_name):
    filename = f"{page_name}.py"
    with open(filename, "w") as file:
        file.write(code)
    print(f"Page '{page_name}' generated successfully as '{filename}'.")


def create_page(page_name):
    code = generate_page(page_name)
    save_to_file(code, PAGES_DIR + page_name)


if __name__ == "__main__":
    main()
