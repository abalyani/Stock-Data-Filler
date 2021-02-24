def FillStocks(df,fill = True):
    # importing pandas
    import pandas as pd
  
    # r for range of correct date values (all days of the provided interval in the given dataframe)
    r = pd.date_range(start=df.index.min(), end=df.index.max())
    
    # reindexing the dates of the dataframe
    df = df.reindex(r).rename_axis('Date')
    
    # counting the maximum number of subsequent NAN values in our stock dataframe
    col = df.columns[0]
    max_NANs = max(df[col].isnull().astype(int).groupby(df[col].notnull().astype(int).cumsum()).sum())
    
    if(fill == True):
        # filling the NANs using 'pad' or 'ffill' A.K.A. 'feed values forward'
        df = df.fillna(method = 'pad')
    
    # simple print and return
    print("The highest number of subsequent days without data was \""+str(max_NANs)+"\". If the nubmer is 3 or less than you're good to go!")
    return df
