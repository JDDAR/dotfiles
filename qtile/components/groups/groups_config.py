"""
Configuración de grupos (workspaces) para Qtile - VERSIÓN CORREGIDA
Soluciona el problema de VS Code que se abre siempre en el grupo #3
"""

from libqtile.config import Group, Match, Rule
from libqtile.lazy import lazy

# Configuración básica
mod = "mod4"

def get_groups():
    """
    Retorna la lista de grupos configurados con reglas específicas
    """
    groups = [
        Group("1"),
        Group("2"),
        Group("3"), 
        Group("4"),
        Group("5"),
        Group("6"),
        Group("7"), 
        Group("8"),
        Group("9")
    ]
    
    return groups

def get_group_keys():
    """
    Retorna las teclas para navegar entre grupos
    """
    groups = get_groups()
    group_keys = []
    
    for i in groups:
        group_keys.extend([
            # Ir al grupo
            Key([mod], i.name, 
                lazy.group[i.name].toscreen(), 
                desc=f"Ir al grupo {i.name}"),
            
            # Mover ventana al grupo
            Key([mod, "shift"], i.name, 
                lazy.window.togroup(i.name), 
                desc=f"Mover ventana al grupo {i.name}"),
        ])
    
    return group_keys

def get_dgroups_app_rules():
    """
    Reglas para controlar dónde se abren las aplicaciones específicas
    Estas reglas SOLO se aplican si quieres que ciertas apps siempre vayan a grupos específicos
    """
    return [
        # Ejemplos comentados - descomenta si quieres forzar aplicaciones a grupos específicos
        # Rule(Match(wm_class=["firefox", "Firefox"]), group="2"),
        # Rule(Match(wm_class=["discord", "Discord"]), group="8"),
        # Rule(Match(wm_class=["spotify", "Spotify"]), group="9"),
        
        # Para VS Code - si quieres que SIEMPRE vaya al grupo 3, descomenta la siguiente línea:
        # Rule(Match(wm_class=["Code", "code-oss"]), group="3"),
    ]

# Variables principales para exportar
groups = get_groups()
group_keys = get_group_keys()  
dgroups_app_rules = get_dgroups_app_rules()

dgroups_key_binder = None  # Evita conflictos con tus keybindings personalizados
dgroups_apps_rules = dgroups_app_rules