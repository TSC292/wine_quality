"""
This .py file forms the source of refactored python code used in Tom Shaw Carveth's wine quality exploration and classification project.
"""

import plotly.express as px, plotly.graph_objects as go, matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.metrics import roc_curve, plot_precision_recall_curve, average_precision_score

def box_plots_hist(df, group, cols=None, title_box='', title_hist=''):
    """
    README
    df - Pandas DataFrame
    group - column name containing unique values to group by
    cols - list of column names to focus on. If None then it uses all columns.
    title_box - string to add to the title of the column name
    """
    list_colours = ['red','green','blue','yellow','orange','black'] ## This custom list is used because of preference over colours
    
    if cols is None:
        cols = list(df.columns)
    group_vals = df[group].unique()
    
    for i in cols:
        fig = go.Figure(layout=go.Layout(height=600, width=800, title=i+title_box, yaxis_title=i))
        for n, val in enumerate(group_vals):
            fig.add_trace(go.Box(y=df.loc[df[group]==val][i], name=val, marker_color = list_colours[n], opacity=0.75))
        fig.update_layout(title_x=0.5)
        fig.show();
        
        fig = px.histogram(df, i, histnorm='percent', color=group, width=800, height=600, title=i+title_hist, color_discrete_sequence = list_colours[0:len(group_vals)], opacity=0.4)
        fig.update_layout(barmode='overlay', title_x=0.5)
        fig.show();
