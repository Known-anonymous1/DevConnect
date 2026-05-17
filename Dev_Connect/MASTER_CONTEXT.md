# DEVCONNECT MASTER CONTEXT

## Project Overview
DevConnect is a developer networking platform similar to LinkedIn but focused on developers, freelancers, recruiters, and businesses.

The platform includes:
- User profiles
- Posts and feeds
- Follow system
- Job portal
- Freelancer marketplace
- Vendor services
- Membership plans
- Notifications
- Admin dashboard
- Chat system

---

# Tech Stack

## Backend
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Django Signals
- Celery (future)

## Frontend
- React
- Tailwind CSS
- Axios
- Redux Toolkit

---

# Backend Architecture

## Apps Structure

### authentication
Handles:
- login
- signup
- JWT tokens
- password reset
- email verification

### users
Handles:
- profiles
- followers/following
- social links
- developer info

### posts
Handles:
- posts
- likes
- comments
- feeds

### jobs
Handles:
- job posting
- applications
- recruiters

### freelancers
Handles:
- freelancer profiles
- gigs
- earnings

### memberships
Handles:
- paid plans
- subscriptions
- permissions

---

# Coding Standards

- Use class-based DRF views
- Use serializers properly
- Keep business logic in services
- Avoid fat views
- Use environment variables
- Follow REST naming conventions

---

# Authentication Flow

- JWT authentication
- Access token + refresh token
- Protected routes
- Role-based permissions

---

# Current Status

## Completed
- Basic project setup
- PostgreSQL setup
- Initial authentication
- Frontend initialization

## In Progress
- JWT authentication
- Profile system

## Pending
- Notifications
- Chat
- Memberships
- Payment integration

---

# Folder Naming Rules

- snake_case for backend
- camelCase for frontend components

---

# AI Instructions

Always:
- follow existing architecture
- do not rewrite unrelated files
- maintain modularity
- avoid duplicate logic
- create reusable components
- write production-ready code

Never:
- hardcode secrets
- break existing APIs
- generate unnecessary files

---

# Git Workflow

Commit after every feature.

Example:
git commit -m "completed JWT authentication module"

Branches:
- main = production
- dev = development
- feature/* = new features