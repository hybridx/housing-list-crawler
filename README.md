# Product Lifecycle - Comprehensive Project Report

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture & Technology Stack](#architecture--technology-stack)
3. [Project Structure](#project-structure)
4. [Applications Deep Dive](#applications-deep-dive)
5. [Database Schema](#database-schema)
6. [Deployment & Infrastructure](#deployment--infrastructure)
7. [Development Workflow](#development-workflow)
8. [Configuration Management](#configuration-management)
9. [How to Make Changes](#how-to-make-changes)
10. [API Documentation](#api-documentation)
11. [Testing Strategy](#testing-strategy)
12. [Troubleshooting Guide](#troubleshooting-guide)

---

## Project Overview

The **Product Lifecycle** project is a comprehensive monorepo built using **Nx workspace** that serves as the **single source of truth** for managing product lifecycle data for Red Hat's **Product Experience (PE) team**. 

### Core Purpose
- Centralized management of product lifecycle information
- Streamlined data control for the PE team
- Multi-environment deployment support (dev, qa, stage, beta, prod)
- Microservices architecture with shared libraries

### Project Version
- **Current Version**: 1.8.1
- **Node.js Version**: 18+ (specified in .nvmrc)
- **Workspace Type**: Nx Monorepo

---

## Architecture & Technology Stack

### Frontend Technologies
- **React**: 16.14.0
- **TypeScript**: 4.6.2
- **Vite**: Build tool and dev server
- **PatternFly**: UI component library
- **Redux Toolkit**: State management
- **React Router**: Navigation
- **i18next**: Internationalization (supports en, zh_CN, ja, ko)

### Backend Technologies
- **Node.js**: 18+
- **Express.js**: Web framework
- **TypeScript**: Programming language
- **Prisma**: Database ORM
- **MariaDB**: Database
- **JWT**: Authentication
- **Swagger**: API documentation

### Development Tools
- **Nx**: Monorepo management
- **ESLint**: Code linting
- **Prettier**: Code formatting
- **Husky**: Git hooks
- **Commitizen**: Conventional commits
- **Jest**: Testing framework

### Deployment
- **OpenShift**: Container orchestration
- **Podman/Docker**: Containerization
- **Tekton**: CI/CD pipelines

---

## Project Structure

```
lifecycle/
├── apps/                           # Applications
│   ├── lifecycle-api/             # Backend API service
│   ├── lifecycle-ui/              # Frontend user interface
│   └── lifecycle-admin/           # Admin dashboard
├── libs/                          # Shared libraries
│   └── lifecycle-libs/            # Common utilities and interfaces
├── config/                        # Environment configurations
│   ├── cert/                      # SSL certificates
│   ├── key/                       # Security keys
│   ├── default.js                 # Default config
│   ├── dev.js                     # Development config
│   ├── qa.js                      # QA config
│   ├── beta.js                    # Beta config
│   └── prod.js                    # Production config
├── .openshift/                    # OpenShift deployment configs
├── .tekton/                       # CI/CD pipeline definitions
├── dist/                          # Build output
├── Containerfile.*                # Docker build files
├── package.json                   # Root dependencies
├── nx.json                        # Nx workspace configuration
└── tsconfig.base.json             # TypeScript base config
```

---

## Applications Deep Dive

### 1. lifecycle-api (Backend Service)

**Location**: `apps/lifecycle-api/`

**Purpose**: RESTful API service providing all backend functionality

**Key Components**:
```
src/
├── controllers/           # Business logic handlers
│   ├── productController.ts       (40KB - Main product logic)
│   ├── userController.ts          (10KB - User management)
│   ├── versionController.ts       (Version management)
│   ├── phaseController.ts         (Phase management)
│   ├── productGroupController.ts  (Product grouping)
│   ├── appStreamController.ts     (App stream handling)
│   └── [other controllers]
├── routes/               # API endpoint definitions
├── services/             # Business services
├── middlewares/          # Express middlewares
├── validators/           # Input validation
├── utils/               # Utility functions
├── types/               # TypeScript definitions
├── i18n/                # Internationalization
├── db/                  # Database utilities
├── docs/                # API documentation
├── prisma.ts            # Database client
├── env.ts               # Environment variables
└── index.ts             # Application entry point
```

**Database**: 
- Uses Prisma ORM with MariaDB
- Schema located in `prisma/schema.prisma`
- Supports migrations in `prisma/migrations/`

**Key Features**:
- JWT authentication with RSA256
- Swagger API documentation at `/api-docs/v1`
- i18n support (en, zh_CN, ja, ko)
- HTTPS with custom CA certificates
- Comprehensive error handling

### 2. lifecycle-ui (Frontend Application)

**Location**: `apps/lifecycle-ui/`

**Purpose**: Main user interface for viewing and interacting with product lifecycle data

**Key Components**:
```
src/
├── components/          # Reusable UI components
├── containers/          # Page-level components
├── locales/            # Translation files
├── utils/              # Frontend utilities
├── legacy/             # Legacy code compatibility
├── epics/              # Redux epics for side effects
├── css/                # Styling files
├── App.jsx             # Main application component
└── index.tsx           # Application entry point
```

**Build Configuration**:
- Vite-based build system
- TypeScript support
- Development proxy for API calls
- Hot module replacement

### 3. lifecycle-admin (Admin Dashboard)

**Location**: `apps/lifecycle-admin/`

**Purpose**: Administrative interface for managing product lifecycle data

**Key Components**:
```
src/
├── components/          # Admin-specific components
├── containers/          # Admin page containers
├── store/              # Redux store configuration
├── hooks/              # Custom React hooks
├── utils/              # Admin utilities
├── constants/          # Application constants
├── css/                # Admin-specific styles
├── App.tsx             # Main admin application
└── index.tsx           # Admin entry point
```

**Special Features**:
- Advanced data management capabilities
- User role management
- Bulk operations support
- Advanced filtering and search

### 4. lifecycle-libs (Shared Library)

**Location**: `libs/lifecycle-libs/`

**Purpose**: Common utilities, interfaces, and components shared across applications

**Structure**:
```
src/
├── interfaces/          # TypeScript interfaces
├── utils/              # Shared utility functions
└── index.ts            # Library exports
```

---

## Database Schema

**Database Type**: MariaDB  
**ORM**: Prisma  
**Schema Location**: `apps/lifecycle-api/prisma/schema.prisma`

**Key Entities** (based on controllers):
- **Products**: Core product information
- **Versions**: Product version tracking
- **Phases**: Lifecycle phases (GA, EOL, etc.)
- **Users**: User management and permissions
- **Roles**: Role-based access control
- **Tiers**: Product tier classifications
- **ProductGroups**: Product categorization
- **AppStreams**: Application stream management
- **Activities**: Activity logging
- **History**: Change tracking

**Database Connection**:
```
Default Local Configuration:
- Host: localhost
- Port: 3306
- Database: lifecycle
- User: root
- Password: redhat123
```

---

## Deployment & Infrastructure

### Container Images

**1. lifecycle-api**
- File: `Containerfile.lifecycle-api`
- Base: UBI8 Node.js 18
- Build: Compiles TypeScript, installs dependencies
- Runtime: Starts API server

**2. lifecycle-ui**
- File: `Containerfile.lifecycle-ui`
- Base: UBI8 Node.js 18
- Build: Vite production build
- Runtime: Serves static files

**3. lifecycle-admin**
- File: `Containerfile.lifecycle-admin`
- Base: UBI8 Node.js 18
- Build: Admin-specific build process
- Runtime: Serves admin interface

**4. MariaDB (Local Development)**
- File: `Containerfile.local.mariadb`
- Purpose: Local database setup

### OpenShift Environments

**Available Environments**:
- **dev**: Development environment
- **qa**: Quality assurance testing
- **stage**: Staging environment
- **beta**: Beta testing
- **prod**: Production environment

**Deployment Files Location**: `.openshift/`
- Each environment has dedicated YAML files for each service
- Configurations include resource limits, environment variables, routes

### CI/CD Pipeline

**Location**: `.tekton/`
- Tekton-based CI/CD pipelines
- Automated build and deployment processes
- Integration with OpenShift

---

## Development Workflow

### Local Setup Process

1. **Prerequisites**:
   ```bash
   node --version  # Should be 18+
   npm --version   # Latest
   ```

2. **Installation**:
   ```bash
   git clone <repository-url>
   cd lifecycle
   nvm use  # Use correct Node version
   npm install  # Install dependencies
   ```

3. **Database Setup**:
   ```bash
   # Option 1: Local MariaDB
   # Configure .env with database credentials
   
   # Option 2: Podman/Docker
   podman build -t custom-mariadb -f Containerfile.local.mariadb
   podman run -d --name mariadb_container -p 3306:3306 custom-mariadb
   ```

4. **Start Development**:
   ```bash
   npm run start  # Starts all services
   # OR individually:
   npm run start:lifecycle-api:dev
   npm run start:lifecycle-ui
   npm run start:lifecycle-admin
   ```

### Available Scripts

**Build Commands**:
```bash
npm run build                    # Build all projects
npm run build:lifecycle-libs     # Build shared library
npm run build:lifecycle-api      # Build API only
npm run build:lifecycle-admin    # Build admin only
npm run build:lifecycle-ui       # Build UI only
```

**Development Commands**:
```bash
npm run start                    # Start all services
npm run start:lifecycle-api:dev  # Start API in dev mode
npm run start:lifecycle-ui       # Start UI dev server
npm run start:lifecycle-admin    # Start admin dev server
```

**Database Commands**:
```bash
npm run db:generate              # Generate Prisma client
```

**Testing Commands**:
```bash
npm run test                     # Run all tests
```

### Git Workflow

**Commit Standards**:
- Uses Conventional Commits
- Commitizen integration (`npm run commit`)
- Automated changelog generation

**Pre-commit Hooks**:
- ESLint checking and auto-fixing
- Prettier code formatting
- Automatic staging of formatted files

---

## Configuration Management

### Environment Configuration

**Structure**: Config files in `/config/`
- `default.js`: Base configuration
- `dev.js`: Development overrides
- `qa.js`: QA environment
- `beta.js`: Beta environment
- `prod.js`: Production settings

**Key Configuration Areas**:
- Database connection settings
- JWT public keys
- Port configurations
- SSL certificate paths
- Logging levels

### Environment Variables

**Key Variables** (from `apps/lifecycle-api/src/env.ts`):
- `DB_HOST`: Database host
- `DB_PORT`: Database port
- `DB_NAME`: Database name
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password
- `NODE_ENV`: Environment (dev/qa/stage/beta/prod)

---

## How to Make Changes

### 1. Adding New Features

**Backend API Changes**:

1. **Add Controller**:
   ```typescript
   // apps/lifecycle-api/src/controllers/newFeatureController.ts
   export const getNewFeature = async (req: Request, res: Response) => {
     // Implementation
   };
   ```

2. **Add Routes**:
   ```typescript
   // apps/lifecycle-api/src/routes/newFeatureRoutes.ts
   import { Router } from 'express';
   import { getNewFeature } from '../controllers/newFeatureController';
   
   const router = Router();
   router.get('/new-feature', getNewFeature);
   export default router;
   ```

3. **Update Main Routes**:
   ```typescript
   // apps/lifecycle-api/src/routes/routes.ts
   import newFeatureRoutes from './newFeatureRoutes';
   router.use('/new-feature', newFeatureRoutes);
   ```

**Frontend Changes**:

1. **Add Components**:
   ```typescript
   // apps/lifecycle-ui/src/components/NewFeature.tsx
   import React from 'react';
   export const NewFeature: React.FC = () => {
     return <div>New Feature</div>;
   };
   ```

2. **Add to Routing**:
   ```typescript
   // Update routing configuration
   ```

### 2. Database Schema Changes

1. **Update Prisma Schema**:
   ```prisma
   // apps/lifecycle-api/prisma/schema.prisma
   model NewEntity {
     id    Int    @id @default(autoincrement())
     name  String
     // ... other fields
   }
   ```

2. **Generate Migration**:
   ```bash
   cd apps/lifecycle-api
   npx prisma migrate dev --name add_new_entity
   ```

3. **Update Types**:
   ```bash
   npm run db:generate
   ```

### 3. Adding New Environment

1. **Create Config File**:
   ```javascript
   // config/newenv.js
   module.exports = {
     // Environment-specific configuration
   };
   ```

2. **Create OpenShift Deployment**:
   ```yaml
   # .openshift/lifecycle-api-deploy-newenv.yml
   # Copy and modify existing deployment file
   ```

### 4. UI/UX Changes

**Styling**:
- Use PatternFly components for consistency
- CSS files in respective `css/` directories
- Follow existing naming conventions

**Internationalization**:
- Add translations in `apps/lifecycle-ui/src/locales/`
- Support for en, zh_CN, ja, ko languages

### 5. Testing Changes

**Unit Tests**:
- Jest configuration in each application
- Test files alongside source code
- Run: `npm run test`

**Integration Tests**:
- API endpoint testing
- Database integration tests

---

## API Documentation

### Base URL Structure
- **Local Development**: `http://127.0.0.1:8848/v1`
- **Swagger UI**: `http://127.0.0.1:8848/api-docs/v1`

### Key Endpoints

**Products**:
- `GET /v1/products/` - Get all products
- `GET /v1/products/{id}` - Get product by ID
- `POST /v1/products/` - Create product
- `PUT /v1/products/{id}` - Update product
- `DELETE /v1/products/{id}` - Delete product

**Versions**:
- `GET /v1/versions` - Get all versions
- `GET /v1/versions/{id}` - Get version by ID

**Phases**:
- `GET /v1/phases` - Get all phases
- `GET /v1/phases/{id}` - Get phase by ID

**Authentication**:
- JWT-based authentication
- RSA256 algorithm
- Public key configuration in config files

---

## Testing Strategy

### Test Structure
- **Unit Tests**: Individual component/function testing
- **Integration Tests**: API endpoint testing
- **E2E Tests**: Full application workflow testing

### Test Configuration
- **Framework**: Jest
- **Configuration**: `jest.config.js` in each application
- **Coverage**: Automated coverage reporting

### Running Tests
```bash
npm run test                 # All tests
nx run lifecycle-api:test    # API tests only
nx run lifecycle-ui:test     # UI tests only
nx run lifecycle-admin:test  # Admin tests only
```

---

## Troubleshooting Guide

### Common Issues

**1. Database Connection Issues**:
```bash
# Check database status
podman ps | grep mariadb

# Restart database
podman restart mariadb_container

# Check database logs
podman logs mariadb_container
```

**2. Build Failures**:
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Clear Nx cache
nx reset

# Rebuild everything
npm run build
```

**3. Port Conflicts**:
- API: Default port 8848
- UI: Check `vite.config.ts` for port
- Admin: Check `vite.config.ts` for port

**4. Prisma Issues**:
```bash
# Regenerate Prisma client
npm run db:generate

# Reset database (development only)
cd apps/lifecycle-api
npx prisma migrate reset
```

### Log Locations
- **API Logs**: Console output with structured logging
- **UI Logs**: Browser developer console
- **Build Logs**: Terminal output during build process

### Development Server URLs
- **API**: http://localhost:8848
- **UI**: http://localhost:4200 (typical Vite default)
- **Admin**: http://localhost:4201 (typical secondary port)
- **Swagger**: http://localhost:8848/api-docs/v1

---

## Maintenance & Updates

### Regular Maintenance Tasks

1. **Dependency Updates**:
   ```bash
   npm audit                 # Check for vulnerabilities
   npm update               # Update dependencies
   npm audit fix            # Fix vulnerabilities
   ```

2. **Database Maintenance**:
   ```bash
   # Backup database (production)
   # Apply migrations
   # Monitor performance
   ```

3. **Security Updates**:
   - Monitor for CVEs in dependencies
   - Update certificates in `/config/cert/`
   - Review JWT configurations

### Version Management
- Semantic versioning (major.minor.patch)
- Automated changelog generation
- Git tag-based releases

---

## Conclusion

This Product Lifecycle project is a well-structured, enterprise-grade monorepo application designed for managing product lifecycle data. The architecture supports scalability, maintainability, and multi-environment deployments.

**Key Strengths**:
- Modern technology stack
- Comprehensive CI/CD pipeline
- Multi-environment support
- Internationalization support
- Strong typing with TypeScript
- Comprehensive API documentation

**For any changes or enhancements**, follow the established patterns and conventions outlined in this report. Always test changes locally before deploying to higher environments, and ensure proper documentation is maintained.

---

**Report Generated**: $(date)  
**Project Version**: 1.8.1  
**Last Updated**: Based on current codebase analysis 
