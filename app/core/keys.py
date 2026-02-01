from datetime import timedelta

JWT_ISSUER = "auth-playground"
JWT_AUDIENCE = "auth-playground-api"
JWT_EXPIRATION = timedelta(minutes=15)

JWT_SECRET = "dev-secret-change-me"
JWT_ALGORITHM = "HS256"
