"""Processor module for computing volatility-based backtest results.

This module validates incoming messages and computes a backtest signal
or metric based on volatility analysis. All operations are logged for observability.
"""

from typing import Any, Dict

from app.utils.setup_logger import setup_logger
from app.utils.types import ValidatedMessage
from app.utils.validate_data import validate_message_schema

logger = setup_logger(__name__)


def validate_input_message(message: dict[str, Any]) -> ValidatedMessage:
    """
    Validate the incoming raw message against the expected schema.

    Parameters:
        message (dict[str, Any]): The raw message payload.

    Returns:
        ValidatedMessage: A validated message object.
    """
    logger.debug("🔍 Validating message schema...")
    if not validate_message_schema(message):
        logger.error("❌ Message schema invalid: %s", message)
        raise ValueError("Invalid message format")
    return message  # type: ignore[return-value]


def compute_volatility_signal(message: ValidatedMessage) -> dict[str, Any]:
    """
    Compute a volatility-based signal from the validated input message.

    This function is a placeholder for real volatility-based backtest logic.
    It can use metrics such as standard deviation, ATR, or Bollinger Bands.

    Parameters:
        message (ValidatedMessage): A validated message containing historical data.

    Returns:
        dict[str, Any]: A dictionary with the signal and metadata.
    """
    logger.debug("📊 Computing volatility signal for: %s", message.get("symbol", "N/A"))

    # Placeholder logic
    price = message.get("price", 0.0)
    volatility = message.get("volatility", 0.0)
    signal = "buy" if volatility < 0.2 else "sell"

    result = {
        "symbol": message.get("symbol"),
        "signal": signal,
        "price": price,
        "volatility": volatility,
        "strategy": "volatility-backtest",
    }

    logger.info("✅ Computed signal: %s", result)
    return result
