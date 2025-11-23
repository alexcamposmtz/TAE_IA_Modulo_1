"""
Lab 4: Decorators - Lab 2: Access Control Decorator
Advanced Python - CINVESTAV Guadalajara
Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro

Este módulo implementa un decorador de control de acceso que verifica
permisos de administrador antes de ejecutar funciones sensibles.
"""


def require_admin(func):
    """
    Decorador que verifica si el usuario tiene permisos de administrador.
    
    Este decorador comprueba si se pasó el argumento keyword 'role' con
    valor 'admin'. Si no es así, niega el acceso a la función.    
    Args:
        func: La función a decorar        
    Returns:
        wrapper: La función envuelta con control de acceso
    """
    def wrapper(*args, **kwargs):
        """
        Función wrapper que implementa el control de acceso.        
        Args:
            *args: Argumentos posicionales pasados a la función
            **kwargs: Argumentos keyword pasados a la función            
        Returns:
            El resultado de la función original si tiene permisos,
            None en caso contrario
        """
        # Verificar si el argumento 'role' existe y es 'admin'
        user_role = kwargs.get('role', None)
        
        if user_role == 'admin':
            print(f"[ACCESS GRANTED] User with role '{user_role}' can access '{func.__name__}'")
            # Remover 'role' de kwargs antes de llamar la función
            # para evitar TypeError si la función no lo espera
            kwargs_clean = {k: v for k, v in kwargs.items() if k != 'role'}
            return func(*args, **kwargs_clean)
        else:
            print(f"[ACCESS DENIED] User with role '{user_role}' cannot access '{func.__name__}'")
            print(f"[ACCESS DENIED] Admin privileges required for '{func.__name__}'")
            return None
    
    return wrapper


@require_admin
def delete_user(username):
    """
    Elimina un usuario del sistema (requiere permisos de admin).    
    Args:
        username: Nombre del usuario a eliminar        
    Returns:
        Mensaje de confirmación de eliminación
    """
    return f"User '{username}' has been successfully deleted from the system."


@require_admin
def modify_permissions(username, permissions):
    """
    Modifica los permisos de un usuario (requiere permisos de admin).    
    Args:
        username: Nombre del usuario
        permissions: Lista de permisos a asignar        
    Returns:
        Mensaje de confirmación
    """
    return f"Permissions for '{username}' updated to: {permissions}"


@require_admin
def view_sensitive_data(data_type):
    """
    Visualiza datos sensibles del sistema (requiere permisos de admin).    
    Args:
        data_type: Tipo de datos sensibles a visualizar        
    Returns:
        Datos sensibles solicitados
    """
    sensitive_data = {
        'users': ['Agustín', 'Alex', 'Juan'],
        'passwords': ['***encrypted***'],
        'logs': ['2025-11-15: System started', '2025-11-15: User logged in']
    }
    return f"Sensitive data ({data_type}): {sensitive_data.get(data_type, 'Not found')}"


def main():
    """
    Función principal que demuestra el uso del decorador require_admin.
    """
    print("=" * 70)
    print("Lab 4: Decorators - Lab 2: Access Control Decorator")
    print("=" * 70)
    print()
    
    # Prueba 1: Eliminar usuario SIN permisos de admin
    print("Test 1: delete_user('juan_bananas') - WITHOUT admin role")
    print("-" * 70)
    result1 = delete_user('juan_bananas')
    print(f"Result: {result1}")
    print()
    
    # Prueba 2: Eliminar usuario CON permisos de admin
    print("Test 2: delete_user('juan_bananas', role='admin') - WITH admin role")
    print("-" * 70)
    result2 = delete_user('juan_bananas', role='admin')
    print(f"Result: {result2}")
    print()
    
    # Prueba 3: Rol de usuario normal
    print("Test 3: delete_user('san_blas_crazy_woman', role='user') - WITH user role")
    print("-" * 70)
    result3 = delete_user('san_blas_crazy_woman', role='user')
    print(f"Result: {result3}")
    print()
    
    # Prueba 4: Modificar permisos sin ser admin
    print("Test 4: modify_permissions('coco_loco', ['read', 'write']) - WITHOUT admin")
    print("-" * 70)
    result4 = modify_permissions('coco_loco', ['read', 'write'])
    print(f"Result: {result4}")
    print()
    
    # Prueba 5: Modificar permisos siendo admin
    print("Test 5: modify_permissions('coco_loco', ['read', 'write'], role='admin')")
    print("-" * 70)
    result5 = modify_permissions('coco_loco', ['read', 'write'], role='admin')
    print(f"Result: {result5}")
    print()
    
    # Prueba 6: Ver datos sensibles sin permisos
    print("Test 6: view_sensitive_data('passwords') - WITHOUT admin")
    print("-" * 70)
    result6 = view_sensitive_data('passwords')
    print(f"Result: {result6}")
    print()
    
    # Prueba 7: Ver datos sensibles con permisos
    print("Test 7: view_sensitive_data('logs', role='admin') - WITH admin")
    print("-" * 70)
    result7 = view_sensitive_data('logs', role='admin')
    print(f"Result: {result7}")
    print()
    
    print("=" * 70)
    print("Lab 2 Complete!")
    print("=" * 70)


if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Solo se ejecuta cuando el script se ejecuta directamente.
    """
    main()