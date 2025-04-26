import os
import subprocess

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip()

print("📂 Cambiando al directorio del proyecto...")
os.chdir(os.path.dirname(__file__))

print("🔍 Verificando cambios pendientes...")
status = run("git status --porcelain")

if not status:
    print("✅ No hay cambios para hacer commit.")
else:
    print("📁 Archivos modificados detectados.")
    print("📝 Añadiendo archivos al staging...")
    run("git add .")

    mensaje = input("✏️ Escriba el mensaje de commit: ").strip()
    if not mensaje:
        mensaje = "Actualización automática"

    print(f"💾 Haciendo commit con mensaje: '{mensaje}'")
    run(f'git commit -m "{mensaje}"')

    print("🚀 Haciendo push al repositorio remoto...")
    push_output = run("git push")

    print("✅ Cambios enviados a GitHub.")
    print(push_output)