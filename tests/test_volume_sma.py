import pytest
from hypella_indicators.indicators.volume_sma import VolumeSMA
from tests.utils import load_candles
import pandas as pd

def test_volume_sma_initialization():
    indicator = VolumeSMA(period=20)
    assert indicator.period == 20

def test_volume_sma_calculation():
    candles = load_candles("candles.json")
    indicator = VolumeSMA(period=10)
    result = indicator.calculate(candles)
    
    # Manual verification
    volumes = pd.Series([c.volume for c in candles])
    expected = volumes.rolling(window=10).mean().iloc[-1]
    
    assert round(result, 4) == round(expected, 4)
    assert result > 0

def test_volume_sma_precise_value():
    """Test that Volume SMA matches the expected value of 197187 for the provided dataset."""
    candles = load_candles("candles.json")
    
    sma = VolumeSMA(period=20)
    result = sma.calculate(candles)
    
    # Check if result matches 197187
    assert round(result, 0) == 197187