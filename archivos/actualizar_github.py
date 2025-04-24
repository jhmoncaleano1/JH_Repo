import subprocess
from datetime import datetime

# Mensaje de commit con la fecha y hora actual
mensaje = f"Actualización automática {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Comandos Git
comandos = [
    ["git", "add", "."],
    ["git", "commit", "-m", mensaje],
    ["git", "push"]
]

# Ejecutar los comandos
for comando in comandos:
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print(f"\n$ {' '.join(comando)}")
    print(resultado.stdout)
    if resultado.stderr:
        print("⚠️ Error:", resultado.stderr)
