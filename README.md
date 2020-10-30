# AlgotradingTest

## BacktraderTest

Tests out the Backtrader python framework. This allows you to test out and carry out algorithmic trading strategies.

### TiingoFeed.py
Currently am using Tiingo API as my datasource. As a result, I've created a Tiingo Data Feed to be used with Backtrader.
TiingoFeed file contains the Tiingo Data Feed class as well as functions to pull data from Tiingo API.

### app.py
Contains the actual backtrader implementation. Currently it does nothing but log the price at close.

