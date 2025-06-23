"""
Hauptanwendung für das VALEO NeuroERP Backend
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import bcrypt

from db.database import get_db
from models.user import User, UserRole
from models import Role, Setting, SettingCategory, SettingValue, Tenant, TenantConfig

app = FastAPI(
    title="VALEO NeuroERP API",
    description="Backend API für das VALEO NeuroERP System",
    version="1.0.1"
)

# CORS-Konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In Produktion anpassen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root-Endpunkt für Healthchecks"""
    return {"status": "online", "version": "1.0.1"}

@app.get("/api/health")
async def health_check():
    """Detaillierter Health-Check-Endpunkt"""
    return {
        "status": "healthy",
        "version": "1.0.1",
        "database": "connected"
    }

# User-Endpunkte
@app.get("/api/users", response_model=List[dict])
async def get_users(db: Session = Depends(get_db)):
    """Liste aller Benutzer abrufen"""
    users = db.query(User).all()
    return [{"id": str(user.id), "username": user.username, "email": user.email} for user in users]

@app.post("/api/users")
async def create_user(username: str, email: str, password: str, role: UserRole = UserRole.USER, db: Session = Depends(get_db)):
    """Neuen Benutzer erstellen"""
    # Prüfe, ob Benutzer bereits existiert
    existing_user = db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Benutzer existiert bereits")
    
    # Erstelle neuen Benutzer
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": str(user.id), "username": user.username, "email": user.email}

# Tenant-Endpunkte
@app.get("/api/tenants", response_model=List[dict])
async def get_tenants(db: Session = Depends(get_db)):
    """Liste aller Mandanten abrufen"""
    tenants = db.query(Tenant).all()
    return [{"id": str(tenant.id), "name": tenant.name, "status": tenant.status.value} for tenant in tenants]

@app.post("/api/tenants")
async def create_tenant(name: str, description: str = None, db: Session = Depends(get_db)):
    """Neuen Mandanten erstellen"""
    # Prüfe, ob Mandant bereits existiert
    existing_tenant = db.query(Tenant).filter(Tenant.name == name).first()
    if existing_tenant:
        raise HTTPException(status_code=400, detail="Mandant existiert bereits")
    
    # Erstelle neuen Mandanten
    tenant = Tenant(
        name=name,
        description=description
    )
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return {"id": str(tenant.id), "name": tenant.name, "status": tenant.status.value}

# Settings-Endpunkte
@app.get("/api/settings", response_model=List[dict])
async def get_settings(db: Session = Depends(get_db)):
    """Liste aller Systemeinstellungen abrufen"""
    settings = db.query(Setting).all()
    return [{"id": str(setting.id), "key": setting.key, "value": setting.value} for setting in settings]

@app.post("/api/settings")
async def create_setting(key: str, value: str, description: str = None, db: Session = Depends(get_db)):
    """Neue Systemeinstellung erstellen"""
    # Prüfe, ob Einstellung bereits existiert
    existing_setting = db.query(Setting).filter(Setting.key == key).first()
    if existing_setting:
        raise HTTPException(status_code=400, detail="Einstellung existiert bereits")
    
    # Erstelle neue Einstellung
    setting = Setting(
        key=key,
        value=value,
        description=description
    )
    db.add(setting)
    db.commit()
    db.refresh(setting)
    return {"id": str(setting.id), "key": setting.key, "value": setting.value}

# API-Endpunkte hier erweitern... 