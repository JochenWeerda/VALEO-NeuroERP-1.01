# VALEO - Die NeuroERP Version 1.01

Ein umfassendes ERP-System für Großhandel, hier als Kundenprojekt für einen Landhandel, das speziell auf die Anforderungen der Landwirtschaftsbranche zugeschnitten ist.

## Projektübersicht

Das ERP-System besteht aus mehreren Komponenten:

- **Frontend**: React-basierte Single-Page-Application
- **Backend**: FastAPI-basierte Microservices
- **Finance-Service**: Eigenständiger Microservice für Finanzen und Buchhaltung
- **Observer-Service**: Überwachungsdienst für Systemperformance

## Starten der Anwendung

### Frontend starten

```powershell
# PowerShell-Skript für einfachen Start
.\start_frontend.ps1
```

oder manuell:

```powershell
cd frontend
npm run dev
```

Das Frontend ist dann unter http://localhost:3001 verfügbar.

### Finance-Service starten

```powershell
.\start_finance_311.ps1
```

Der Finance-Service ist dann unter http://localhost:8007 verfügbar.

### Beleg-Service starten

```powershell
.\start_beleg_service_311.ps1
```

Der Beleg-Service ist dann unter http://localhost:8005 verfügbar.

## Projektstruktur

Das Projekt ist in mehrere Hauptkomponenten aufgeteilt:

```
AI_driven_ERP/
├── frontend/               # React-Frontend (Vite)
│   ├── src/                # Quellcode
│   ├── public/             # Statische Dateien
│   ├── package.json        # Frontend-Abhängigkeiten
│   └── vite.config.js      # Vite-Konfiguration
├── backend/                # FastAPI-Backend
│   ├── app/                # Backend-Anwendung
│   ├── tests/              # Tests
│   └── requirements.txt    # Python-Abhängigkeiten
├── database/               # Datenbankdateien
├── scripts/                # Hilfsskripte
│   ├── start_frontend.ps1  # Frontend-Starter (PowerShell)
│   ├── van-frontend-validator.ps1  # VAN-Modus Validator
│   └── start_backend.ps1   # Backend-Starter (PowerShell)
└── memory-bank/            # Projektwissen und Dokumentation
    ├── tasks.md            # Aktuelle Aufgaben
    ├── systemPatterns.md   # Architekturmuster
    └── activeContext.md    # Aktiver Entwicklungskontext
```

## VAN-Modus: Validierung vor der Entwicklung

**WICHTIG:** Vor dem Start der Frontend-Entwicklung sollte immer der VAN-Modus (Validation and Navigation) ausgeführt werden, um eine korrekte Entwicklungsumgebung sicherzustellen:

```powershell
# VAN-Modus Frontend-Validator ausführen
./scripts/van-frontend-validator.ps1
```

Der VAN-Modus Validator prüft:
- Korrekte Verzeichnisstruktur
- Vorhandensein aller benötigten Konfigurationsdateien
- JSX-Konfiguration in vite.config.js
- Installierte Abhängigkeiten
- PowerShell-Kompatibilität
- Portverfügbarkeit

Bei Problemen korrigiert der Validator automatisch viele typische Fehler oder gibt spezifische Anweisungen zur Behebung.

## Frontend-Entwicklung

### Voraussetzungen

- Node.js (v18 oder höher)
- npm (v7 oder höher)
- PowerShell 5.1 oder höher (für Windows)

### Entwicklungsumgebung einrichten

1. **Frontend-Abhängigkeiten installieren**:
   ```powershell
   cd frontend
   npm install
   ```

2. **Frontend-Entwicklungsserver starten**:
   ```powershell
   # Option 1: PowerShell-Skript verwenden (EMPFOHLEN)
   ./scripts/start_frontend.ps1
   
   # Option 2: Direkter Befehl im frontend-Verzeichnis
   cd frontend
   npm start
   ```

   Die Anwendung wird unter http://localhost:5173 verfügbar sein (oder einem alternativen Port, falls 5173 bereits belegt ist).

### Frontend-Entwicklung: PowerShell-Besonderheiten

Bei der Entwicklung unter Windows mit PowerShell sind folgende Besonderheiten zu beachten:

1. **Kein `&&` für Befehlsverkettung**
   ```powershell
   # FALSCH:
   cd frontend && npm start
   
   # RICHTIG:
   cd frontend
   npm start
   
   # ODER als einzeilige Alternative mit Semikolon:
   cd frontend; npm start
   ```

2. **Pfade mit Leerzeichen benötigen Anführungszeichen**
   ```powershell
   cd "C:\Mein Pfad\mit Leerzeichen\frontend"
   ```

3. **Umgebungsvariablen setzen (temporär)**
   ```powershell
   $env:PORT=5000
   npm start
   
   # Oder in einer Zeile:
   $env:PORT=5000; npm start
   ```

### Typische Fehler und Lösungen

#### "Missing script: start"
- **Problem**: Das Skript kann nicht gefunden werden
- **Lösung**: 
  1. Sicherstellen, dass man im `frontend/`-Verzeichnis ist: `cd frontend`
  2. Überprüfen, ob `package.json` die notwendigen Skripte enthält
  3. VAN-Modus-Validator ausführen: `../scripts/van-frontend-validator.ps1`

#### JSX-Syntax-Fehler
- **Problem**: "The JSX syntax extension is not currently enabled"
- **Lösung**:
  1. `vite.config.js` überprüfen und sicherstellen, dass die esbuild-Konfiguration korrekt ist:
     ```javascript
     esbuild: {
       loader: { '.js': 'jsx', '.ts': 'tsx' },
       jsxFactory: 'React.createElement',
       jsxFragment: 'React.Fragment'
     }
     ```
  2. PowerShell-Skript `./scripts/start_frontend.ps1` verwenden, das dies automatisch korrigiert

#### TypeScript-Fehler
- **Problem**: "Cannot find module 'typescript'"
- **Lösung**: 
  1. TypeScript installieren: `npm install typescript --save-dev`
  2. PowerShell-Skript `./scripts/start_frontend.ps1` verwenden, das dies automatisch erkennt und korrigiert

#### Port-Konflikte
- **Problem**: Der Standardport ist bereits belegt
- **Lösung**:
  1. Anderen Port angeben: `npm start -- --port 5000`
  2. Oder das PowerShell-Skript `./scripts/start_frontend.ps1` verwenden, das automatisch einen freien Port findet

#### PowerShell-Befehlsverkettung
- **Problem**: `&&` für Befehlsverkettung führt zu Fehlern
- **Lösung**:
  1. Befehle nacheinander ausführen:
     ```powershell
     cd frontend
     npm start
     ```
  2. Oder mit Semikolon trennen: `cd frontend; npm start`
  3. Oder das PowerShell-Skript `./scripts/start_frontend.ps1` verwenden

## Backend-Entwicklung

### Voraussetzungen

- Python 3.10 oder höher
- FastAPI
- PostgreSQL (optional, für Produktionsumgebung)

### Entwicklungsumgebung einrichten

1. **Python-Abhängigkeiten installieren**:
   ```powershell
   cd backend
   pip install -r requirements.txt
   ```

2. **Backend-Server starten**:
   ```powershell
   # Option 1: PowerShell-Skript verwenden
   ./scripts/start_backend.ps1
   
   # Option 2: Direkter Befehl
   cd backend
   uvicorn app.main:app --reload
   ```

   Die API wird unter http://localhost:8000 verfügbar sein.
   Die API-Dokumentation ist unter http://localhost:8000/docs erreichbar.

## Fehlerbehebung und Notfallmaßnahmen

### Notfall-Frontendstart bei anhaltenden Problemen

Wenn alle anderen Methoden fehlschlagen, kann das Frontend mit einem einfachen HTTP-Server gestartet werden:

```powershell
# Wechsle ins Frontend-Verzeichnis
cd frontend

# Starte einen einfachen HTTP-Server
npx http-server -p 8080 .
```

### Portbelegung überprüfen

Um zu prüfen, welche Ports bereits belegt sind:

```powershell
# Zeige alle offenen TCP-Verbindungen an
Get-NetTCPConnection -State Listen | Sort-Object -Property LocalPort | Format-Table LocalPort, OwningProcess, State

# Prozess-ID zu Name auflösen
Get-Process -Id <PID>
```

### Fehlerhafte Konfigurationsdateien zurücksetzen

Bei hartnäckigen Problemen mit Konfigurationsdateien:

```powershell
# Führe VAN-Modus-Validator mit -reset Parameter aus
./scripts/van-frontend-validator.ps1 -reset
```

## Projektdokumentation

Die Projektdokumentation wird in der `memory-bank/` verwaltet und enthält:

- **tasks.md**: Aktuelle Aufgaben und Fortschritte
- **systemPatterns.md**: Architekturmuster und Designentscheidungen
- **activeContext.md**: Aktiver Entwicklungskontext und wichtige Hinweise
- **archive/archive-frontend-startup-problem.md**: Dokumentation zu den Frontend-Startproblemen und deren Lösung

## Deployment

Anweisungen zum Deployment finden Sie in der `deployment.md` im Projektverzeichnis.

## Theme-Modul

Das ERP-System verfügt über ein flexibles Theme-System, das verschiedene Darstellungsmodi und Designvarianten unterstützt:

### Theme-Demo starten

Um die Theme-Demo zu starten und alle verfügbaren Designs zu testen:

```powershell
# Option 1: npm-Skript verwenden
npm run theme-demo

# Option 2: PowerShell-Skript direkt ausführen
./start_theme_demo.ps1
```

### Verfügbare Themes

Das Theme-System unterstützt folgende Modi:
- **Hell** (Standard): Helles Design für normale Verwendung
- **Dunkel**: Augenfreundliches dunkles Design
- **Hoher Kontrast**: Barrierefreies Design mit verstärktem Kontrast

Zusätzlich sind verschiedene Designvarianten verfügbar:
- **Default**: Standarddesign
- **Modern**: Modernes, flaches Design
- **Classic**: Klassisches, strukturiertes Design
- **Odoo**: An Odoo-ERP angelehnte Designvariante

### KI-Assistent für Theme-Anpassungen

Der integrierte KI-Assistent ermöglicht die Anpassung des Designs durch natürlichsprachliche Befehle wie:
- "Wechsle zum dunklen Modus"
- "Ändere die Akzentfarbe zu Blau"
- "Erhöhe den Kontrast"

### Theme-Einstellungen

Die Theme-Einstellungen sind über die ThemeSettings-Komponente zugänglich und erlauben die manuelle Anpassung von:
- Farbschema
- Schriftarten
- Abstände und Radien
- Animationen und Übergänge

### Dokumentation

Eine detaillierte Dokumentation des Theme-Moduls finden Sie in der Datei `frontend/README_THEME.md`.

## Lizenz

Dieses Projekt ist urheberrechtlich geschützt und nur für die interne Verwendung bei Folkerts Landhandel bestimmt.

## Hauptfunktionen

### Theme-System

Das System bietet ein flexibles Theme-System, das verschiedene Erscheinungsbilder unterstützt:

- **Theme-Modi**: Hell, Dunkel und Hoher Kontrast für Barrierefreiheit
- **Theme-Varianten**: Default, Odoo-Stil, Modern und Classic
- **Anpassbare Parameter**: Schriftgröße, Abstände, Farbschemata und mehr
- **Natürlichsprachliche Steuerung**: Änderung des Themes durch einfache Befehle

Demo starten:
```bash
npm run theme-demo
```

## Module

### Theme-System
- Flexibles Theme-System mit verschiedenen Modi (Hell, Dunkel, Hoher Kontrast)
- Verschiedene Theme-Varianten (Default, Modern, Classic, Odoo)
- Natürlichsprachliche Steuerung über LLM-Interface
- Umfassende Barrierefreiheitsfunktionen

### Artikel-Stammdaten
- Erweitertes Datenmodell für umfassende Artikel-Stammdaten
- KI-Unterstützung für Stammdatenpflege:
  - Automatische Klassifikation von Artikeln
  - Preisempfehlungen basierend auf Marktdaten
  - Generierung von Produktbeschreibungen und SEO-Texten
  - Anomalieerkennung in Artikeldaten
- Mehrseitiger Editor für verschiedene Stammdatenbereiche
- Integration mit bestehenden Artikeldaten

# KI-gesteuertes ERP-System

Ein modernes, KI-gesteuertes ERP-System mit asynchroner Aufgabenverarbeitung durch Redis und Celery.

## Hauptkomponenten

### Backend

- **FastAPI Server**: RESTful API für Geschäftsprozesse und Datenoperationen
- **Redis & Celery**: Asynchrone Aufgabenverarbeitung für rechenintensive Operationen
- **SQLAlchemy**: ORM für Datenbankoperationen
- **Prometheus**: Monitoring und Metriken

### Frontend

- **React**: UI-Framework für das Frontend
- **Material-UI**: Komponenten-Bibliothek für ein modernes Design
- **TypeScript**: Statisch typisiertes JavaScript für robusteren Code

## Neue Funktionen: Redis und Celery Integration

Die Integration von Redis und Celery ermöglicht die asynchrone Verarbeitung von rechenintensiven Aufgaben im ERP-System. Die Implementierung umfasst:

1. **Redis** als Message Broker und Result Backend für Celery
2. **Celery** für die asynchrone Verarbeitung von Tasks
3. **Flower** für das Monitoring von Celery-Tasks
4. **API-Endpunkte** zur Interaktion mit Celery-Tasks
5. **PowerShell-Skripte** zum Starten aller Komponenten

### Systemarchitektur

- **Redis (Port 6379)**: Message Broker und Result Backend
- **Celery Worker**: Verarbeitet Tasks aus verschiedenen Queues (default, reports, imports, exports, optimization)
- **Flower (Port 5555)**: Monitoring-Web-Interface für Celery
- **Demo-Server (Port 8003)**: Einfacher Server mit Celery-Integration

### Installation und Start

#### Redis-Installation (Windows)
1. Redis für Windows von https://github.com/microsoftarchive/redis/releases herunterladen
2. Dateien in das Verzeichnis `redis` im Projektverzeichnis extrahieren
3. Redis mit `redis\redis-server.exe` starten

#### Python-Abhängigkeiten
```bash
python scripts/python_deps_install.py
```

#### Starten des Systems
```powershell
.\scripts\start_system_improved.ps1
```

### API-Dokumentation

Nach dem Start des Servers kann die Swagger-Dokumentation unter http://localhost:8003/docs aufgerufen werden.

## Detaillierte Dokumentation

- [Redis und Celery Integration](memory-bank/archive/redis_celery_implementation.md)
- [Projektfortschritt](memory-bank/progress.md)
- [Aktive Aufgaben](memory-bank/tasks.md)

## Nächste Schritte

1. Robuste Fehlerbehandlung für Tasks implementieren
2. Erweiterung um weitere Task-Typen (Import/Export, Optimierung)
3. Persistente Redis-Konfiguration für Produktionsumgebungen
4. Implementierung von Sicherheitsfeatures
5. Docker-Compose-Setup für die Entwicklungsumgebung
