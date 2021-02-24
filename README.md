
# Stock Data Filler
Simple script to fill in stock's data on weekends and other days where the market is down and no sales have been made.
## Motivation
When using stock data you'll notice that some rows are missing. That's due to the fact that the stock market doesn't operate every day of the week. On the weekend the stock market closes, and with that no one can sell or buy stocks. So when accessing data of a certain stock you'll find that only a maximum of 5 or 6 subsequent days are available and then a 2-3 day jump.
This can be problematic when plotting a stock's data alongside another piece of data that's not constrained by weekends.
As you'll be faced with a mismatch error due to the days of the stocks being less then whatever other data you're using.
## Use
First download the stock data you'd want. I highly recommend the Yahoo Finance library `yfinance`. 
Here's a quick demonstration on how to do so.
```python 
import yfinance as yf
aapl_df = yf.download('AAPL', 
                      start='2020-01-01', 
                      end='2020-12-31', 
                      progress=False)
```
After obtaining the stock data and storing it in a variable if you'd display the elements you'd notice the absence of the mentioned days.
```python 
aapl_df.head(10)
# will result in:
```

![Table representing Apple's stocks from 2019/12/31-2020/01/14](https://i.imgur.com/jzQImtS.jpg)
As you can easily observe in under the highlighted days there appears to be a 2 day jump.
Now let's import the script and apply it to our dataframe of apple's stock.
```python 
from StockFiller import FillStocks
aapl_df_filled = FillStocks(aapl_df,fill=False)
aapl_df_filled.head(10)
# will result in:
```
![Table representing Apple's stocks from 2019/12/31-2020/01/14, but with the missing days added](https://i.imgur.com/oXEmRN4.jpg)
Great! Now we have the missing days... but unfortunately that's not gonna fix our problem if we're wishing to plot this. If we were to plot the "Open" price using `matplotlib` here's what we'll get.
```python
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
ax.plot(aapl_df_filled.index,aapl_df_filled['Open'])
```
![Bad apple stock representation](https://i.imgur.com/SYK1kLt.png)
What an absolute mess right? Luckily the script was never intended to be used like this. If you recall in the earlier snippet of code in the call of my script `StockFiller` we set the `fill` parameter to `False` just for the sake of showing what the script does without too much confusing. But, now let's get in to it.
```python
from StockFiller import FillStocks
aapl_df_filled = FillStocks(aapl_df,fill=True)
aapl_df_filled.head(10)
# will result in:
```
![Table representing Apple's stocks from 2019/12/31-2020/01/14, but with the missing days added and, values filled](https://i.imgur.com/JkB8iSI.jpg)
The empty slots were filled by feeding the value from the previous day (Which intuitively makes perfect sense, as the price hasn't changed over the weekend due to the simple fact that no is buying or selling).
Now if we were to plot it we would get a very clear representation of the change in stock price.
```python
ax.plot(aapl_df_filled.index,aapl_df_filled['Open'])
# will result in:
```
![Fixed plot of the stock](https://i.imgur.com/EGsOl4w.jpg)
