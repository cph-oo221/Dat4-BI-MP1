# Dat4-MP1

### Group:

- Lasse - Github: **[kotteletfisk](https://github.com/kotteletfisk)**
- Oskar - Github: **[cph-oo221](https://github.com/cph-oo221)**

[]()

## Stock Market

### Data Origin(s):

[Stock Market Dataset](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs?resource=download) - From Kaggle, txt file.

Dataset contains/provides historical daily data for US stocks and ETFs. The data is from NASDAQ, NYSE and NYSE MKT.

The given data has been loaded using our own TXT reader, then it has been cleaned, explored, and visualized in a Jupyter Notebook.

### Python files / Jupyter Notebook:

#### TXT Reader:

[txt-Reader](./txtreader.py)

#### Stock Market Notebook:

[Stock market notebook](./stocks.ipynb)

## Movies And Tv Shows

### Data Origin(s):

[Movies And Tv Shows Dataset](https://www.kaggle.com/datasets/crawlfeeds/movies-and-tv-shows-dataset) - From Kaggle, Json File.

Dataset for Movies and Tv Shows from streaming platfrom such as Netflix, Hulu, Prime Video, and so on.

The movie and tv show data has been loaded using our own JSON reader, then it has been cleaned, explored, and visualized via. models and graphs such as scatter plot, histogram, box plot, bar chart.

### Python files / Jupyter Notebook:

#### Json Reader:

[json-Reader](./jsonreader.py)

#### Movies And Tv Shows Notebook:

[Movies And Tv Shows Notebook](./movies.ipynb)

## Additional Util For Project:

[Meta Data Gathering](./meta.py)

## HTML reader

[Html Reader](./readhtml.py)

Methods for gathering html pages for analytical data, using http or https protocol urls.
consists of 2 functions, with one reading and preparing the data from an url, and the other to call the forementhioned recursively, and to return a pandas dataframe with the resulting data, consisting of the following columns:

[filetype, title, metadata, body, link0, link1, link2, link3, level]