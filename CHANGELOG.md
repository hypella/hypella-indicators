# Changelog

All notable changes to this project will be documented in this file.

## [1.2.0] - 2025-12-31

### Added
- **Stateful Indicators**: Introduced `update(candle)` and `seed(candles)` methods to the `Indicator` base class to support $O(1)$ incremental updates.
- **Incremental Logic**: Optimized all core indicators (`SMA`, `EMA`, `RSI`, `ATR`, `ADX`, `BB`, `VolumeSMA`, `RSISMA`) for low-latency live trading.
- **Incremental Consistency Tests**: Added rigorous testing to ensure stateful updates match batch calculations.

## [1.1.0] - 2025-12-29

### Added
- **ADX**: ADX indicator with Wilder's Smoothing.
- **ATR**: ATR indicator with Wilder's Smoothing.

## [1.0.1] - 2025-12-29

### Added
- **GitHub Actions**: Added GitHub Actions for release and publish to PyPI.

### Changed
- **Registry**: Added `label` to indicator arguments.

## [1.0.0] - 2025-12-29

### Added
- **Initial Release** of Hypella Indicators library.
- **RSI**: Relative Strength Index with Wilder's Smoothing.
- **RSI SMA**: Simple Moving Average of RSI.
- **SMA**: Simple Moving Average.
- **EMA**: Exponential Moving Average.
- **Volume SMA**: Simple Moving Average of Volume.
- **Bollinger Bands**: Full implementation with Upper, Middle, Lower bands and %B.
- **Registry**: Immutable indicator registry system (`registry.yaml`).
- **Tests**: Comprehensive test suite with standard market data.
