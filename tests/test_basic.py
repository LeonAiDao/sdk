from src.core.engine import LeonEngine

def test_engine():
    engine = LeonEngine()
    result = engine.process("test")
    assert result["status"] == "success"
