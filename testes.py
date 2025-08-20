import itertools
import time

from rich.progress import Progress
import time

# def print_animation(items, interval=0.2):
#     for item in itertools.cycle(items):
#         print(f"\r{item}", end="")
#         time.sleep(interval)

# print("Aguarde...")
# animation_chars = ['-', '\\', '|', '/']
# print_animation(animation_chars)
# time.sleep(3)
# print("\rOperação concluída!  ")




with Progress() as progress:
    task1 = progress.add_task("[cyan]Carregando...", total=100)
    for i in range(100):
        time.sleep(0.05)
        progress.update(task1, advance=1)
print("[green]Operação concluída!")