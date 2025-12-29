import pytest
from hypella_indicators.indicators.sma import SMA
from tests.utils import load_candles
import pandas as pd

def test_sma_initialization():
    indicator = SMA(period=20)
    assert indicator.period == 20

def test_sma_calculation():
    candles = load_candles("candles.json")
    indicator = SMA(period=10)
    result = indicator.calculate(candles)
    
    # Manual verification
    closes = pd.Series([c.close for c in candles])
    expected = closes.rolling(window=10).mean().iloc[-1]
    
    assert round(result, 4) == round(expected, 4)
    assert result > 0

def test_sma_precise_value():
    """Test that SMA matches the expected value of 23.921 for the provided dataset."""
    candles = load_candles("candles.json")
    
    sma = SMA(period=9)
    result = sma.calculate(candles)
    
    # Check if result matches 23.921 with 3 decimal places precision
    assert round(result, 3) == 23.921