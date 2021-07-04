# datasci-tools
Functions I use for data analysis which are too painful to do by hand. Check the Python notebook for examples and usage.

## Functions so far

### corr_matrix(data, significance=False, decimals=3)

Generates a correlation matrix with p values, just like SPSS. It takes the following parameters:

- data: pandas.DataFrame to calculate correlations
- significance: bool that determines whether to include asterisks to correlations. Default: False.
- decimals: int used to round values. Default: 3.

### pie(values, labels=None, title='', slices=None, percent_only=False, explode=True, color='white')

Useful pie plot with matplotlib. It has the following parameters:

- values (mandatory): `list` or `pandas.Series()` of unique values. Using `value_counts()` is highly recommended.
- labels: if `None`, indices of `values` will be used. Default: None.
- title: header for the plot. Default: ''.
- slices: set a number of slices, to avoid clutter. Default: None.
- percent_only: if False it will show count and percent. Default: False.
- explode: slightly separate the slice with the highest value. Default: True.
- color: text color. Default: 'white'.
