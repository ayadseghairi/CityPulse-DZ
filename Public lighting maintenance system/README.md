# Proactive Public Lighting Maintenance System

A civic tech platform that transforms city lighting maintenance from reactive (fix when broken) to proactive (predict and prevent failures before they create safety hazards).

## 🎯 Features

- **Citizen Portal**: Report street lighting failures with GPS location and photos
- **Auto-Priority Scoring**: Intelligent prioritization based on population density, incident clustering, and proximity to sensitive areas
- **Admin Dashboard**: Live map with color-coded priority pins, analytics, and report management
- **Technician Mobile App**: View assigned orders, track progress, and upload resolution photos
- **Proactive Detection**: Automatic hotspot detection using DBSCAN clustering
- **Real-time Notifications**: Socket.IO integration for instant status updates

## 🏗️ Tech Stack

**Frontend**: React 18, Router v6, Axios, Leaflet, Bootstrap 5, Socket.IO Client
**Backend**: Flask, SQLAlchemy ORM, SQLite, JWT, Flask-SocketIO, APScheduler

## 📁 Project Structure

```
.
├── backend/                    # Flask REST API
│   ├── app/
│   │   ├── __init__.py        # App factory pattern
│   │   ├── config.py          # Configuration classes
│   │   ├── models/            # SQLAlchemy models
│   │   ├── routes/            # Blueprint routes
│   │   ├── services/          # Business logic
│   │   ├── schemas/           # Marshmallow validation
│   │   ├── utils/             # Helper functions
│   │   └── tasks/             # APScheduler jobs
│   ├── tests/
│   ├── run.py                 # Entry point
│   └── requirements.txt
├── frontend/                   # React SPA
│   ├── src/
│   │   ├── components/        # Shared components
│   │   ├── pages/             # Route pages
│   │   ├── context/           # React Context
│   │   ├── services/          # API calls
│   │   ├── hooks/             # Custom hooks
│   │   ├── utils/             # Utilities
│   │   ├── assets/            # Images, fonts
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── .env
├── .env.example
└── README.md
```

## 🚀 Quick Start

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp ../.env.example ../.env

# Run the Flask app with SocketIO
python run.py
```

Server runs at `http://localhost:5000`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

App runs at `http://localhost:3000`

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register` - Citizen registration
- `POST /api/auth/login` - User login
- `POST /api/auth/refresh` - Refresh JWT token

### Reports
- `GET /api/reports` - Get reports
- `POST /api/reports` - Create report
- `GET /api/reports/:id` - Get report details
- `PATCH /api/reports/:id/status` - Update status

### Priority
- `GET /api/priority/queue` - Get sorted priority queue
- `POST /api/priority/recalculate` - Recalculate all priorities

### Admin
- `GET /api/admin/reports` - All reports
- `GET /api/analytics/zone-stats` - Analytics
- `POST /api/admin/technicians/assign` - Assign technician

### Technician
- `GET /api/technician/orders` - My orders
- `PATCH /api/maintenance/:id/update` - Update order status

### Notifications
- `GET /api/notifications` - Get notifications
- `PATCH /api/notifications/:id/read` - Mark as read

## 🎨 Design System

**Colors**:
- Primary: `#1A2B4A` (Dark Navy)
- Accent: `#F5A623` (Amber)
- Success: `#27AE60`
- Warning: `#E67E22`
- Danger: `#E74C3C`

**Priority Levels**:
- 🔴 Critical (80-100)
- 🟠 High (60-79)
- 🟡 Medium (40-59)
- 🟢 Low (0-39)

## 🔒 Security

- JWT authentication with 15-min access tokens and 7-day refresh tokens
- Role-based access control (citizen, technician, admin)
- Input validation with Marshmallow
- File upload restrictions (JPEG/PNG, max 5MB)
- Rate limiting (5 reports/day per citizen)
- CORS whitelist

## 📝 License

MIT
