import psutil
import random

random.seed()

seed = int(psutil.cpu_percent(0)*psutil.virtual_memory()[1])
random.seed(seed)
nahodne = random.random()

print(f"Vygenerovaný semínko: {seed}")
print(f"Vygenerované náhodné číslo: {nahodne}")


