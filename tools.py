import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

pd.options.display.max_colwidth = 540  # show more characters when printing tables
pd.options.display.max_rows = 50

# copy the following in any new notebook: %matplotlib inline

def corr(data, significance=False, decimals=3):
    '''Generates a correlation matrix with p values and sample size, just like SPSS. 
	
    Args:
        data (pandas.DataFrame): Data for calculating correlations.
        significance (bool): Determines whether to include asterisks in correlations.
        decimals (int): Used to round values.
	
	Returns:
		pandas.DataFrame: SPSS-like correlation matrix.
    '''
	# (adapted from https://stackoverflow.com/questions/25571882/pandas-columns-correlation-with-statistical-significance)
    # generate matrices (r, p vals, sample size)
    rs = data.corr(method=lambda x, y: pearsonr(x,y)[0]).round(decimals)
    pvals = data.corr(method=lambda x, y: pearsonr(x,y)[1]).round(decimals)
    ns = data.corr(method=lambda x, y: len(x)).replace(1, np.nan).round(decimals)  # sample size = 1 would be misleading

    if(significance):
        p = pvals.applymap(lambda x: ''.join(['*' for t in [0.001, 0.01, 0.05] if x <= t]))  # matrix with asterisks
        rs = rs.astype(str) + p
    
	# (adapted from https://stackoverflow.com/questions/58282538/merging-pandas-dataframes-alternating-rows-without-soritng-rows)
    # create new index level enumerating the number of columns
    s1 = rs.assign(_col = np.arange(len(rs))).set_index('_col', append=True)
    s2 = pvals.assign(_col = np.arange(len(pvals))).set_index('_col', append=True)
    s3 = ns.assign(_col = np.arange(len(ns))).set_index('_col', append=True)

    # merge these matrices
    corr_matrix = (pd.concat([s1, s2, s3], keys=('Pearson\'s r','p value', 'Sample size'))  # new index with each indicator
                    .sort_index(kind='merge', level=2)  # sort index, so names in previous line are important
                    .reset_index(level=2, drop=True)  # drop _col index
                    .swaplevel(0,1))  # invert index levels
    
    return corr_matrix

def pie(values, labels=None, title='', slices=None, percent_only=False, explode=True, color='white'):
    '''Display a pie plot.
	
    Args:
        values (list): list or pandas.Series of unique values. Using value_counts() is highly recommended.
        labels (list): if None, indices of values will be used.
        title (str): header for the plot.
        slices (int): set a number of slices, to avoid clutter.
        percent_only (bool): if False it will show count and percent.
        explode (bool): slightly separate the slice with the highest value.
        color (str): text color.
    '''
    if isinstance(values, list):
        values = pd.Series(values)
    
    if slices:  # debug
        other = values[slices:]
        values = values[:slices]
        values.index = values.index.astype(str)  # avoid problems with CategoricalIndex
        values['Other'] = other.sum()

    if not labels:
        labels = values.index
        if labels.dtype == 'O':
            labels = labels.str.capitalize()
    
    def show_value_and_percent(x):
        if not(percent_only):
            return '{:.1f}%\n({:.0f})'.format(x, total*x/100)
        else:
            return '{:.0f}%'.format(x, total*x/100)
    
    explode = [0.1] + [0 for l in range(len(labels)-1)] if explode else [0 for l in range(len(labels))]
    total = sum(values)
    
    fig, ax = plt.subplots()
    a, b, autotexts = ax.pie(values, labels=labels, explode=explode, autopct=show_value_and_percent, shadow=True, startangle=90)
    plt.setp(autotexts, **{'color': color, 'fontsize': 12.5})
    ax.set_title(title, fontweight='bold')
    plt.show()

