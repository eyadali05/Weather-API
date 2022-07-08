import os
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich import print_json, print
from random import choice
from data import get_data

console = Console()
emoji = [":cloud:", ":sun:"]


def display_menu():
    md = ""
    with open("menu.md") as menu:
        menu_list = menu.readlines()
        for line in menu_list:
            md += str(line)
    console.print(Markdown(md))
    return menu_list


def main():
    os.system("cls" if os.name == "nt" else "clear")
    display_menu()
    query = Prompt.ask(
        "[i]Enter City Name [bold cyan](eg: Cairo, New York)[/bold cyan][/i]"
    )
    # Current Weather
    parsed_data = get_data(query)

    print(f"{choice(emoji)} [i][cyan]Weather Report[cyan][/i][bold red]![/bold red]\n")

    print("[bold]Location[bold]:")
    print_json(data=parsed_data["request"]["query"])

    print("[bold]Time[bold]:")
    print_json(data=parsed_data["current"]["observation_time"])

    print("[bold]Temperature :thermometer:[bold]:")
    print_json(data=parsed_data["current"]["temperature"])

    print("[bold]Feels Like[bold]:")
    print_json(data=parsed_data["current"]["feelslike"])

    print("[bold]Weather Description[bold]:")
    print_json(data=parsed_data["current"]["weather_descriptions"])

    print("[bold]precip :rain:[bold]:")
    print_json(data=parsed_data["current"]["precip"])

    print("[bold]Humidity[bold]:")
    print_json(data=parsed_data["current"]["humidity"])

    print("[bold]Wind Speed[bold]:")
    print_json(data=parsed_data["current"]["wind_speed"])


main()
