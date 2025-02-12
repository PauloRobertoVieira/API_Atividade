from fastapi import APIRouter
from app.utils.logger import logger

router = APIRouter()

@router.get("/log")
async def log_check():
    logger.debug("Debug log")
    logger.info("Info log")
    logger.warning("Warning log")
    logger.error("Error log")
    logger.critical("Critical log")
    return {"message": "Verifique o log para ver os registros."}