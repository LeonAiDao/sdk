from fastapi import APIRouter
from src.modules.automation import AutomationModule

router = APIRouter()
automation = AutomationModule()

@router.get("/analyze")
def analyze():
    result = automation.run_task("Analyze Data")
    return {"result": result}
