import subprocess
import time

def get_connected_monitors():
    """Obtiene monitores conectados con su estado real"""
    try:
        output = subprocess.check_output(["xrandr", "--query"]).decode("utf-8")
        monitors = []
        for line in output.splitlines():
            if " connected" in line:
                name = line.split()[0]
                status = "connected" if " connected" in line else "disconnected"
                monitors.append((name, status))
        return monitors
    except Exception as e:
        print(f"Error getting monitors: {e}")
        return [("eDP1", "connected")]  # Fallback a pantalla principal

def configure_displays():
    """Configura automáticamente las pantallas detectadas"""
    try:
        monitors = get_connected_monitors()
        primary = "eDP1"
        external = None
        
        # Buscar monitor externo conectado
        for name, status in monitors:
            if name != primary and status == "connected":
                external = name
                break
        
        # Configurar pantallas
        if external:
            subprocess.run([
                "xrandr", 
                "--output", external,
                "--auto", 
                "--right-of", primary
            ])
            print(f"Configurado {external} como extensión derecha de {primary}")
        else:
            # Apagar todas las salidas excepto la principal
            for name, _ in monitors:
                if name != primary:
                    subprocess.run(["xrandr", "--output", name, "--off"])
            print("Solo usando pantalla principal")
            
    except Exception as e:
        print(f"Error configuring displays: {e}")