from fastapi import APIRouter
import services.analyzer as analyzer

router = APIRouter()

@router.get("/logs/count")
def get_logs_count():
    
    log_series = analyzer.get_log_type_count()
    return [{"level": k, "count": v} for k, v in log_series.items()]

@router.get("/logs/frequency")
def get_frequency_log():
    log_series = analyzer.get_log_frequency_by_level()
    return [{"message":k, "count":v} for k,v in log_series.items()]