"""
Modellpaket für das ERP-System.

Dieses Paket enthält alle Datenbankmodelle, die die Grundlage für das ERP-System bilden.
"""

# Base aus database importieren
from backend.db.database import Base

# Importiere Basismodelle
from .base import *
from .user import User, Role, UserRole
from .settings import Setting, SettingCategory, SettingValue
from .tenant import Tenant, TenantConfig, TenantStatus

# Exportiere Basismodelle
__all__ = [
    'Base',
    
    # user.py
    'User', 'Role', 'UserRole',

    # settings.py
    'Setting', 'SettingCategory', 'SettingValue',

    # tenant.py
    'Tenant', 'TenantConfig', 'TenantStatus'
]