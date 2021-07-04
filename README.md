# datasci-tools
Functions I use for data analysis which are too painful to do by hand. Check the Python notebook for examples and usage.

## Functions so far

### corr_matrix(data, significance=False, decimals=3)

Generates a correlation matrix with p values, just like SPSS. It takes the following parameters:

- data: pandas.DataFrame to calculate correlations
- significance: bool that determines whether to include asterisks to correlations.
- decimals: int used to round values.

### pie(values, labels=None, title='', slices=None, percent_only=False, explode=True, color='white')

Useful pie plot with matplotlib. It has the following parameters:

- values: `list` or `pandas.Series()` of unique values. Using `value_counts()` is highly recommended.
- labels: if `None`, indices of `values` will be used.
- title: header for the plot.
- slices: set a number of slices, to avoid clutter.
- percent_only: if False it will show count and percent.
- explode: slightly separate the slice with the highest value.
- color: text color.
