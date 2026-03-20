Overview
The Stock Bot allows you to fetch historical stock data using the Polygon API. You can enter a stock ticker and a specific date (in MM-DD-YYYY format) to retrieve the stock's open, high, low, close, and volume data for that day. The data is displayed in a user-friendly table for easy reference.

Note The Current Release only Supports Windows Platform

How to Use
1. **Open the Program**
   - Double-click the `StockBot.exe` file to launch the program.

2. **Set Up Your API Key**
   - In the same folder as the `.exe` file, you will find a file named `api.env`.
   - Open `api.env` using a text editor (like Notepad).
   - Insert your Polygon API key in the file, like this:
     ```
     API_KEY="insert key here"
     ```
   - Save and close the file.

3. **Using the Program**
   - Enter the stock ticker symbol (e.g., `TSLA`) into the "Enter Ticker" box.
   - Enter the date you want to search for in the format `MM-DD-YYYY`.
   - Click the "Fetch Data" button.

4. **Viewing the Results**
   - The program will fetch the data and display it in the table.
   - The table will show Open, High, Low, Close, and Volume values for the selected day.

Troubleshooting
- If the program shows an error about missing data, make sure the ticker and date are correct.
- If the program cannot find the API key, ensure the `api.env` file is saved correctly with no extra spaces or quotes.

Notes
- The program will only work with valid Polygon API keys.
- If the stock market was closed on the selected date (e.g., weekends or holidays), no data will be available.
