"""
Proveedor de datos para el Workspace Grid
Obtiene información de qtile sobre workspaces y ventanas
"""

class WorkspaceDataProvider:
    """Clase que maneja la obtención y formateo de datos de workspaces"""
    
    def __init__(self, qtile):
        self.qtile = qtile
        self.icon_map = {
            'firefox': '󰈹', 'chrome': '󰈹', 'chromium': '󰈹', 'brave': '󰈹',
            'code': '󰨞', 'vscodium': '󰨞', 'nvim': '󰨞', 'vim': '󰨞',
            'alacritty': '󰆍', 'terminal': '󰆍', 'konsole': '󰆍',
            'discord': '󰭹', 'telegram': '󰭹', 'slack': '󰭹',
            'spotify': '󰎈', 'vlc': '󰎈', 'mpv': '󰎈',
            'nautilus': '󰉋', 'thunar': '󰉋', 'dolphin': '󰉋',
            'gimp': '󰽰', 'inkscape': '󰽰', 'blender': '󰽰'
        }
    
    def get_workspaces_info(self):
        """
        Retorna información completa de todos los workspaces
        """
        workspaces = []
        current_group = self.qtile.current_group.name
        
        for i in range(1, 9):  # Workspaces 1-8
            workspace_num = str(i)
            
            # Buscar el grupo correspondiente
            group = self._find_group_by_name(workspace_num)
            
            if group is None:
                # Grupo no existe, crear entrada vacía
                workspace_info = {
                    'number': workspace_num,
                    'name': f"Workspace {workspace_num}",
                    'is_active': False,
                    'is_occupied': False,
                    'window_count': 0,
                    'windows': [],
                    'state': 'empty'
                }
            else:
                # Obtener información del grupo
                windows_info = self._get_windows_info(group)
                is_active = group.name == current_group
                is_occupied = len(group.windows) > 0
                
                workspace_info = {
                    'number': workspace_num,
                    'name': f"Workspace {workspace_num}",
                    'is_active': is_active,
                    'is_occupied': is_occupied,
                    'window_count': len(group.windows),
                    'windows': windows_info,
                    'state': 'active' if is_active else ('occupied' if is_occupied else 'empty')
                }
            
            workspaces.append(workspace_info)
        
        return workspaces
    
    def get_current_workspace_preview(self):
        """
        Retorna información detallada del workspace actual para el preview
        """
        current_group = self.qtile.current_group
        windows_info = self._get_windows_info(current_group)
        
        return {
            'number': current_group.name,
            'name': f"Workspace {current_group.name}",
            'window_count': len(current_group.windows),
            'windows': windows_info,
            'is_empty': len(current_group.windows) == 0
        }
    
    def _find_group_by_name(self, name):
        """Busca un grupo por nombre"""
        for group in self.qtile.groups:
            if group.name == name:
                return group
        return None
    
    def _get_windows_info(self, group):
        """Obtiene información detallada de las ventanas en un grupo"""
        windows = []
        
        for window in group.windows:
            try:
                # Obtener información básica
                name = window.name or "Unknown Window"
                if len(name) > 30:
                    name = name[:27] + "..."
                
                # Obtener clase de ventana
                wm_class = self._get_window_class(window)
                
                # Obtener ícono
                icon = self._get_window_icon(wm_class)
                
                window_info = {
                    'name': name,
                    'class': wm_class,
                    'icon': icon,
                    'id': window.wid if hasattr(window, 'wid') else 0
                }
                
                windows.append(window_info)
                
            except Exception as e:
                # Si hay error obteniendo info de ventana, agregar placeholder
                windows.append({
                    'name': "Window",
                    'class': 'unknown',
                    'icon': '󰣆',
                    'id': 0
                })
        
        return windows
    
    def _get_window_class(self, window):
        """Obtiene la clase de una ventana de forma segura"""
        try:
            if window.get_wm_class():
                return window.get_wm_class()[0].lower()
            return 'unknown'
        except:
            return 'unknown'
    
    def _get_window_icon(self, window_class):
        """Obtiene el ícono apropiado para una clase de ventana"""
        for app_name, icon in self.icon_map.items():
            if app_name in window_class:
                return icon
        return '󰣆'  # Ícono por defecto
    
    def switch_to_workspace(self, workspace_number):
        """Cambia al workspace especificado"""
        try:
            workspace_name = str(workspace_number)
            if workspace_name in self.qtile.groups_map:
                self.qtile.groups_map[workspace_name].cmd_toscreen()
                return True
            return False
        except Exception as e:
            print(f"Error switching to workspace {workspace_number}: {e}")
            return False