# monsys
 Simple system monitoring application
## Docker Compose File
```
version: '3.8'

services:
  db:
    image: postgres:latest
    container_name: monsys_postgres_db
    environment:
      POSTGRES_DB: monsys_postgres_db
      POSTGRES_USER: monsys-admin
      POSTGRES_PASSWORD: monsys1
    volumes:
      - monsys-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U monsys-admin -d monsys_postgres_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  web:
    image: ghcr.io/ewsmyth/monsys:latest
    ports:
      - "7337:7337"
    environment:  # ← was spelled wrong: "enviroment"
      SECRET_KEY: aabbccddeeffgghhiijjkkll  # ← you had 2 SECRET_KEYs; removed one
      ADMIN_PASSWORD: password
    depends_on:
      - db

volumes:
  monsys-data:
```