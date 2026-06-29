# Project_School_Attendence_Management

**Flask-based Attendance Management REST API with Docker, PostgreSQL, and optional CI/CD deployment**

## Overview

This repository implements a lightweight, production-minded REST API for managing students and recording attendance. It demonstrates a simple data model, containerization with Docker, and a deployment-ready structure. The API is suitable for small school projects, demos, or as a starting point for a more fully featured attendance system.

Key features:
- ✅ REST API for students and attendance built with Flask
- ✅ Persistent storage using PostgreSQL
- ✅ Dockerized application and easy local development
- ✅ Clear environment-driven configuration for production readiness
- ✅ Example GitHub Actions workflow (optional) for CI/CD

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.11 |
| Framework | Flask |
| Database | PostgreSQL |
| Container | Docker |
| CI/CD | GitHub Actions (optional) |
| Deployment Targets | Docker / AWS ECS / any container platform |

## Repository Structure

```
Project_School_Attendence_Management/
├── .github/
│   └── workflows/
│       └── deploy.yml              # (optional) CI/CD workflow
├── app.py                          # Flask application & routes
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker image configuration
├── README.md                       # This file
├── migrations/                      # (optional) DB migration scripts (alembic)
└── docs/                           # (optional) diagrams, screenshots
```

## API Endpoints

### Health Check
GET /hello
Response:
```json
{ "status": "ok", "message": "Hello — Project_School_Attendence_Management" }
```

### Students
- GET /students
  - Returns list of students
  - Response example:
  ```json
  [
    {"id": 1, "name": "John Doe", "class": "10A"},
    {"id": 2, "name": "Jane Smith", "class": "10B"}
  ]
  ```

- POST /students
  - Create a new student
  - Request body (application/json):
  ```json
  { "name": "Alice Johnson", "class": "9B", "roll_number": 23 }
  ```
  - Response:
  ```json
  { "message": "Student added successfully", "student_id": 3 }
  ```

- GET /students/{id}
  - Get student details by ID

- PUT /students/{id}
  - Update a student's details

- DELETE /students/{id}
  - Remove a student

### Attendance
- GET /attendance
  - Returns attendance records (supports query params: date, student_id, class)

- POST /attendance/mark
  - Mark attendance for a student
  - Request body:
  ```json
  { "student_id": 1, "date": "2026-06-29", "status": "present" }
  ```
  - Response:
  ```json
  { "message": "Attendance recorded", "record_id": 55 }
  ```

- GET /students/{id}/attendance
  - Retrieve attendance history for a student

- GET /attendance/report?from=YYYY-MM-DD&to=YYYY-MM-DD&class=10A
  - Generate simple attendance report for a date range and optional class filter

## Architecture Diagram (Simplified)

```
Developer (git push) -> GitHub Repository
  └─> Docker build -> Docker image
         └─> PostgreSQL (RDS / local) <-> Flask app (container)
API Clients -> Flask API endpoints (/students, /attendance)
```

## Getting Started

### Prerequisites
- Python 3.11+
- Docker (for containerized runs)
- PostgreSQL (local or remote — AWS RDS suggested for production)
- (Optional) AWS account & GitHub Actions secrets for CI/CD

### Local Development

1. Clone the repository
```bash
git clone https://github.com/Benaniosam-hub/Project_School_Attendence_Management.git
cd Project_School_Attendence_Management
```

2. Create a virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Configure environment variables (example)
```bash
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=attendance_db
export DB_USER=postgres
export DB_PASSWORD=your_password
export FLASK_ENV=development
export SECRET_KEY=change_this_secret
```

4. Initialize the database
- If the project includes a migration tool (Alembic), run:
```bash
alembic upgrade head
```
- Otherwise start the app and it will create tables if implemented to do so.

5. Run the application locally
```bash
python app.py
```
The API will be available at http://localhost:5000

### Testing Locally

```bash
# Health check
curl http://localhost:5000/hello

# Get students
curl http://localhost:5000/students

# Add student
curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Student","class":"8A","roll_number":5}'
```

## Docker: Build & Run

```bash
# Build image
docker build -t attendance-api:latest .

# Run container (link to local PostgreSQL)
docker run -p 5000:5000 \
  -e DB_HOST=host.docker.internal \
  -e DB_PORT=5432 \
  -e DB_NAME=attendance_db \
  -e DB_USER=postgres \
  -e DB_PASSWORD=your_password \
  attendance-api:latest
```

## (Optional) CI/CD & Deployment

If you use GitHub Actions to build and deploy:
- Provide secrets in repository settings (e.g., DOCKERHUB_USERNAME, DOCKERHUB_TOKEN or AWS credentials)
- Include a workflow in .github/workflows/deploy.yml to build the image, run tests, push to registry, and deploy to your target.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| DB_HOST | localhost | PostgreSQL host |
| DB_PORT | 5432 | PostgreSQL port |
| DB_NAME | attendance_db | Database name |
| DB_USER | postgres | Database user |
| DB_PASSWORD | (none) | Database password |
| SECRET_KEY | (required) | Flask secret key |
| FLASK_ENV | development | Flask environment (development/production) |

## Security Considerations

- Never commit real credentials to the repository.
- Use environment variables or secrets manager (AWS Secrets Manager, HashiCorp Vault).
- Use strong, unique DB passwords and rotate them periodically.
- Limit DB access via network policies and security groups.
- Run the app behind HTTPS in production and enable authentication for endpoints before exposing sensitive data.

## Troubleshooting

- Database connection errors:
  - Check DB_HOST / DB_PORT and network access.
  - Verify DB user and password.
  - Ensure database exists and migrations ran successfully.

- Docker issues:
  - Confirm the image built successfully: docker images
  - Inspect container logs: docker logs <container-id>

- Application errors:
  - Check Flask logs on stdout.
  - Add logging to app.py for more diagnostics.

## Future Enhancements

- [ ] Add user authentication/authorization (JWT or OAuth)
- [ ] Add role-based access (admin, teacher, student)
- [ ] Add paginated endpoints and filters for large datasets
- [ ] Add database migrations (Alembic) if not already present
- [ ] Add unit and integration tests, and run them in CI
- [ ] Add Swagger/OpenAPI documentation
- [ ] Add export reports (CSV/PDF) and attendance analytics

## Contributing

Contributions are welcome — please:
1. Fork the repository
2. Create a feature branch (feature/...)
3. Commit changes and open a Pull Request
4. Ensure tests pass and include descriptive PR notes

## License

This project is open-source. Choose a license (e.g., MIT) and add it to the repository.

## Author

**Benaniosam** — [GitHub Profile](https://github.com/Benaniosam-hub)

## Support

For issues or questions, open an issue in this repository: https://github.com/Benaniosam-hub/Project_School_Attendence_Management/issues

---

**Last Updated:** June 2026  
**Version:** 1.0.0
