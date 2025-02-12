from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, status

security = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials):
    if credentials.credentials != "secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
        )