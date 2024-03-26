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


def generate_page(page_name):
    class_name = page_name.capitalize() + "Page"
    code = f"""import flet as ft

    class {class_name}(ft.View):

    def __init__(self, page: ft.Page):
        super({class_name}, self).__init__()
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
    with open(PAGES_DIR + filename, "w") as file:
        file.write(code)
    print(f"Page '{page_name}' generated successfully as '{filename}'.")


def create_page(page_name):
    code = generate_page(page_name)
    save_to_file(code, page_name)


if __name__ == "__main__":
    main()
