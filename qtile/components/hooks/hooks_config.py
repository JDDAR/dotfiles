"""
Configuración de hooks y eventos para Qtile
"""

import os
import subprocess
import time
from libqtile import hook
from components.background.background_config import configure_background
from components.display.display_config import configure_displays

def setup_hooks():
    """
    Configura todos los hooks del sistema
    """
    
    # ====== [HOOK: CONFIGURACIÓN DE FONDO] ======
    # Este hook ya está configurado en background_config, solo lo llamamos
    configure_background()
    
    # ====== [HOOK: STARTUP] ======
    @hook.subscribe.startup
    def startup_hook():
        """
        Se ejecuta cada vez que Qtile inicia (incluyendo recargas)
        Útil para configuraciones que deben aplicarse siempre
        """
        print("🚀 Qtile startup - Configurando pantallas...")
        configure_displays()
        time.sleep(1)  # Pequeño delay para estabilizar
        print("✅ Configuración de pantallas completada")
    
    # ====== [HOOK: STARTUP_ONCE] ======
    @hook.subscribe.startup_once
    def autostart():
        """
        Se ejecuta SOLO una vez al iniciar Qtile (no en recargas)
        Ideal para lanzar aplicaciones de inicio
        """
        home = os.path.expanduser("~")
        autostart_script = f"{home}/.config/qtile/autostart.sh"
        
        print("🔧 Qtile startup_once - Ejecutando autostart...")
        
        # Verificar que el script existe y es ejecutable
        if os.path.exists(autostart_script):
            try:
                subprocess.Popen([autostart_script])
                print(f"✅ Autostart ejecutado: {autostart_script}")
            except Exception as e:
                print(f"❌ Error ejecutando autostart: {e}")
        else:
            print(f"⚠️  Advertencia: {autostart_script} no existe")
    
    # ====== [HOOK: CLIENT_NEW] ======
    @hook.subscribe.client_new
    def client_new(client):
        """
        Se ejecuta cuando se abre una nueva ventana
        Útil para configuraciones específicas por aplicación
        """
        # Ejemplos de configuraciones automáticas por aplicación:
        
        # Hacer que ciertos diálogos sean siempre flotantes
        if client.name and "dialog" in client.name.lower():
            client.floating = True
        
        # Configuraciones específicas para ciertas aplicaciones
        if client.get_wm_class():
            wm_class = client.get_wm_class()[0].lower()
            
            # Aplicaciones que deben abrir en grupos específicos
            if wm_class in ["firefox", "chromium", "google-chrome"]:
                client.togroup("2")  # Navegadores al grupo 2
            elif wm_class in ["code", "vscodium", "nvim"]:
                client.togroup("3")  # Editores al grupo 3
            elif wm_class in ["discord", "telegram", "slack"]:
                client.togroup("9")  # Chat al grupo 9
    
    # ====== [HOOK: CLIENT_FOCUS] ======
    @hook.subscribe.client_focus
    def client_focus(client):
        """
        Se ejecuta cuando una ventana recibe el foco
        """
        # Opcional: Registrar qué aplicación tiene el foco
        # print(f"🎯 Foco en: {client.name}")
        pass
    
    # ====== [HOOK: LAYOUT_CHANGE] ======
    @hook.subscribe.layout_change
    def layout_change(layout, group):
        """
        Se ejecuta cuando cambia el layout
        """
        # Opcional: Notificar cambio de layout
        # print(f"📐 Layout cambiado a: {layout.name}")
        pass
    
    # ====== [HOOK: GROUP_WINDOW_ADD] ======
    @hook.subscribe.group_window_add
    def group_window_add(group, window):
        """
        Se ejecuta cuando se agrega una ventana a un grupo
        """
        # Opcional: Cambiar automáticamente al grupo donde se abre la ventana
        # group.cmd_toscreen()
        pass

    print("🔧 Hooks configurados correctamente")

def get_qtile_settings():
    """
    Retorna configuraciones adicionales de Qtile
    """
    settings = {
        # ====== [CONFIGURACIONES GENERALES] ======
        "dgroups_key_binder": None,
        "dgroups_app_rules": [],
        "auto_fullscreen": True,
        "focus_on_window_activation": "smart",
        "reconfigure_screens": True,
        "auto_minimize": True,
        "wl_input_rules": None,
        "wmname": "LG3D",  # Compatibilidad con aplicaciones Java
    }
    
    return settings

# Exportamos las configuraciones
qtile_settings = get_qtile_settings()