"""
Configuración de grupos (workspaces) para Qtile
"""

from libqtile.config import Group, Key
from libqtile.lazy import lazy

# Configuración básica
mod = "mod4"

def get_groups():
    """
    Retorna la lista de grupos configurados
    """
    # Crear grupos del 1 al 9
    groups = [Group(i) for i in "123456789"]
    
    return groups

def get_group_keys():
    """
    Retorna las teclas para navegar entre grupos
    Estas teclas se agregarán a la lista principal de keys
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

# Exportamos para usar en config.py
groups = get_groups()
group_keys = get_group_keys()