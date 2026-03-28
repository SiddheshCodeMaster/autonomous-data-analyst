from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import time

console = Console()


def show_header():
    console.print(
        Panel.fit(
            "[bold green]AUTONOMOUS DATA ANALYST[/bold green]\n[white]Get it analyzed for you[/white]"
        )
    )


def log_info(message):
    console.print(f"[cyan][INFO][/cyan] {message}")


def log_agent(agent_name):
    console.print(f"[yellow][AGENT][/yellow] {agent_name} started...")


def log_success(message):
    console.print(f"[green][SUCCESS][/green] {message}")


def log_error(message):
    console.print(f"[red][ERROR][/red] {message}")


def simulate_delay(seconds=1):
    time.sleep(seconds)
