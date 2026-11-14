
import os
from pathlib import Path
from dotenv import load_dotenv

from usage_logger import UsageLogger

env_path = Path(__file__).resolve().parent / ".env"

load_dotenv(dotenv_path=env_path, override=True)

print("MongoDB URI found:", bool(os.getenv("MONGODB_URI")))

logger = UsageLogger()

try:
    logger.log_call({
        "provider": "Test",
        "model": "test-model",
        "input_tokens": 10,
        "output_tokens": 20,
        "total_tokens": 30,
        "latency_ms": 100,
        "estimated_cost_usd": 0,
        "status": "success",
        "attempts": 1
    })

    print("MongoDB test completed!")

finally:
    logger.close()
