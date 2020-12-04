#!/usr/bin/env python
# coding: utf-8

# # Predicting Trees
#
# ***

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Imports" data-toc-modified-id="Imports-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Data" data-toc-modified-id="Data-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Data</a></span></li><li><span><a href="#Process-Data" data-toc-modified-id="Process-Data-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Process Data</a></span></li><li><span><a href="#Visualize-Data" data-toc-modified-id="Visualize-Data-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Visualize Data</a></span></li><li><span><a href="#Split-data" data-toc-modified-id="Split-data-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Split data</a></span></li><li><span><a href="#Binary-Classification-using-LogisticRegression" data-toc-modified-id="Binary-Classification-using-LogisticRegression-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Binary Classification using LogisticRegression</a></span></li><li><span><a href="#Automated-Binary-Classification-using-LogisticRegression" data-toc-modified-id="Automated-Binary-Classification-using-LogisticRegression-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Automated Binary Classification using LogisticRegression</a></span></li><li><span><a href="#Binary-Classification-using-RandomForestClassifier" data-toc-modified-id="Binary-Classification-using-RandomForestClassifier-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Binary Classification using RandomForestClassifier</a></span></li><li><span><a href="#Automated-Binary-Classification-using-RandomForestClassifier" data-toc-modified-id="Automated-Binary-Classification-using-RandomForestClassifier-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Automated Binary Classification using RandomForestClassifier</a></span></li><li><span><a href="#Extra:-Binary-Classification-using-KNeighborsClassifier" data-toc-modified-id="Extra:-Binary-Classification-using-KNeighborsClassifier-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Extra: Binary Classification using KNeighborsClassifier</a></span></li><li><span><a href="#Extra:-Automated-Binary-Classification-using-KNeighborsClassifier" data-toc-modified-id="Extra:-Automated-Binary-Classification-using-KNeighborsClassifier-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Extra: Automated Binary Classification using KNeighborsClassifier</a></span></li></ul></div>

# ***

# ## Imports

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler


# Utilizing code from the textbook, we can include the function that will build our decision boundary plots.  We will be referencing back to this function later, so running it here helps up to maintain clean code.

# In[2]:


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):

    # setup marker generator and color map
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution)
    )
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.8,
            c=colors[idx],
            marker=markers[idx],
            label=cl,
            edgecolor="black",
        )

    # highlight test examples
    if test_idx:
        # plot all examples
        X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(
            X_test[:, 0],
            X_test[:, 1],
            c="",
            edgecolor="black",
            alpha=1.0,
            linewidth=1,
            marker="o",
            s=100,
            label="test set",
        )


# ***

# ## Data

# I am interested in predicting types of trees, based on certain features.  When looking for data, I stumbled upon a US Department of Agriculture research "data catalog".  In this catalog, there was [data](https://www.fs.usda.gov/rds/archive/Catalog/RDS-2020-0051) regarding tree surveys of the [Umatilla National Forest](https://www.fs.usda.gov/detail/umatilla/?cid=FSEPRD498952) completed in 2020.
#
# This data source contains columns as follows:
#
# | Column Name | Column Description |
# | :- | :- |
# | OID | internal feature number |
# | IDTRSD | join field of township, range, and section number |
# | TreeSpecie | tree species |
# | TreeDia | tree diameter at breast height (inches) |
# | TreeDist | distance to a corner in links (a link is one-hundredth of a chain and since a chain is 66 feet, then one link is 0.66 feet) |
#

# In[3]:


# Read data
trees_df = pd.read_csv("./Data/corner_trees.csv")
trees_df.head()


# In[4]:


trees_df.TreeSpecie.unique()


# In[5]:


trees_df.columns


# `OID` and `IDTRSD` don't provide much value, at least not for this classification project.  We will drop the columns.

# In[6]:


# Drop columns we do not need
trees_df = trees_df.drop(columns=["OID", "IDTRSD"], axis=1)
trees_df.head()


# After we have dropped the columns, we will check the data to see if there are any missing values in the form of `NaN` values.

# In[7]:


# Check for NaN values and count all instance of NaN
trees_df.isna().any().sum()


# There are no `NaN` values so we can move forward with processing the data.
#
# ***

# ## Process Data

# The first thing we have to do is change `TreeSpecie` to numerical values.  We can do this by changing the string values to numbers using `pd.get_dummies()`.  This will replace string values with `0` and `1` where `0 = False` and `1 = True`.

# In[8]:


# Create dummies
species_dummies = pd.get_dummies(trees_df["TreeSpecie"])

# Join old dataframe with dummies and drop `TreeSpecie` column
new_trees_df = trees_df.join(species_dummies)
new_trees_df = new_trees_df.drop(columns="TreeSpecie", axis=1)


# In[9]:


# Keep only a few columns
new_trees_df = new_trees_df[["TreeDia", "TreeDist", "FIR", "PINE"]]


# When fitting the data the first time, we get a `ValueError` because there seems to be values as '`---`' in both the `TreeDia` and `TreeDist` columns.  Because '`---`' is not a `NaN` value, it was not removed earlier.  We can remove it with a few filters here.

# In[10]:


# Clean columns
new_trees_df = new_trees_df[new_trees_df["TreeDia"] != "---"]
new_trees_df = new_trees_df[new_trees_df["TreeDist"] != "---"]

new_trees_df = new_trees_df[new_trees_df["TreeDist"] != "3?"]


# In[11]:


# Change dtypes
new_trees_df["TreeDia"] = new_trees_df["TreeDia"].astype(int)
new_trees_df["TreeDist"] = new_trees_df["TreeDist"].astype(int)


# ***

# ## Visualize Data

# In[12]:


# Plot TreeDia v TreeDist
sns.pairplot(new_trees_df, vars=["TreeDia", "TreeDist"], diag_kind="kde", height=5)


# ***

# ## Split data

# In[13]:


# Create target variable
x_vals = ["TreeDia", "TreeDist"]
y_vals = ["FIR"]

X = new_trees_df[x_vals]
y = new_trees_df[y_vals].values.ravel()


# In[14]:


# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=0, stratify=y
)


# In[15]:


# Scale data
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))


# ***

# ## Binary Classification using LogisticRegression

# Dr. Penland suggested I try to use Binary Classification to predict the type of tree based on tree diameter and distance.  Let's look at a Logistic Regression model to see how it works on this data.
#
# When fitting data, a `DataConversionWarning`is raised.  Instead of suppressing the warning by ignoring it, I wanted to avoid it.  We can do that by using `.values.ravel()` when fitting X and y, converting the value raising a warning, converting the value to a 1d array.  Ravel documentation [here](https://www.geeksforgeeks.org/numpy-ravel-python/).

# In[16]:


from sklearn.linear_model import LogisticRegression


# In[17]:


# Build LogisticRegression model
lr = LogisticRegression(random_state=1, multi_class="ovr").fit(X_train, y_train)


# Now that the model has been created and fit, let's see how well it did on the data.  In classification, one way to tell how well the model did is too look at a confusion matrix.  This will show how well the model can make predictions.

# In[18]:


confusion_matrix(y, lr.predict(X))


# The position of values in Confusion Matrix's are as follows:
#
# ||
# |-|-|
# |True Negatives|False Positives|
# |False Negatives|True Positives|
#
# Reading this matrix down, we see that there are:
#
# - 12802 true negative predictions.  The model predicted the first 12802 zeros (0) correctly.
# - 7348 false negative predictions.  The model predicted zeros (0) wrong 7348 times.
# - 1 false positive prediction.  The model predicted zero (0) wrong once.
# - 1 true positive prediction.  The model predicted one (1) correctly once.
#
# To get a better understanding of these values, let's plot the confusion matrix.

# In[19]:


# Build confusion_matrix object
cm = confusion_matrix(y, lr.predict(X))

# Plot confusion_matrix
sns.heatmap(cm, annot=True, fmt="d")


# Of course, the heat map shares the same information, but seeing it in color helps to show just how drastic the values are.
#
# Thanks to code from the course textbook, we can plot results using decision boundaries. Let's do that now.

# In[20]:


plot_decision_regions(X=X_combined_std, y=y_combined, classifier=lr)


# ## Automated Binary Classification using LogisticRegression

# In[21]:


def tree_pred_binary_log(data, cols_to_drop, target):
    """
    Inputs
    ------
    data : data file
    cols_to_drop : columns to drop
    target : target tree to predict

    Output
    ------
    cm : confusion_matrix
    plot_decision_regions() : plot results
    """

    # read data
    data_frame = pd.read_csv(data)

    # drop junk columns
    for column in cols_to_drop:
        data_frame = data_frame.drop(column, axis=1)

    # check for null values
    for value in data_frame.columns.values:
        sum_nulls = data_frame[value].isna().any().sum()
    if sum_nulls == 0:
        pass
    else:
        print("There are null values.")

    # create dummies
    species_dummies = pd.get_dummies(data_frame["TreeSpecie"])

    # join old dataframe with dummies and drop `TreeSpecie` column
    new_data_frame = data_frame.join(species_dummies)
    new_data_frame = new_data_frame.drop("TreeSpecie", axis=1)

    # clean columns
    new_data_frame = new_data_frame[new_data_frame["TreeDia"] != "---"]
    new_data_frame = new_data_frame[new_data_frame["TreeDist"] != "---"]
    new_data_frame = new_data_frame[new_data_frame["TreeDist"] != "3?"]

    # split data
    x_vals = ["TreeDia", "TreeDist"]
    y_vals = [target]

    X = new_data_frame[x_vals]
    y = new_data_frame[y_vals].values.ravel()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.7, random_state=1
    )

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))

    # build Logistic Classifier model
    lr = LogisticRegression(random_state=1, multi_class="ovr").fit(X_train, y_train)

    cm = confusion_matrix(y, lr.predict(X))

    dr = plot_decision_regions(X=X_combined_std, y=y_combined, classifier=lr)

    return print(
        "True Negatives:",
        cm[0, 0],
        "\nFalse Negatives:",
        cm[-1, 0],
        "\n\nFlase Positives:",
        cm[0, 1],
        "\nTrue Positives:",
        cm[1, -1],
    )


# In[22]:


tree_pred_binary_log(
    data="./Data/corner_trees.csv", cols_to_drop=["OID", "IDTRSD"], target="RED FIR"
)


# ***

# ## Binary Classification using RandomForestClassifier

# In[23]:


from sklearn.ensemble import RandomForestClassifier


# In[24]:


# Build SupportVectorMachine model
rfc = RandomForestClassifier(n_estimators=1000, n_jobs=100, random_state=1).fit(
    X_train, y_train
)


# In[25]:


confusion_matrix(y, rfc.predict(X))


# In[26]:


# Build confusion_matrix object
cm = confusion_matrix(y, rfc.predict(X))

# Plot confusion_matrix
sns.heatmap(cm, annot=True, fmt="d")


# In[27]:


plot_decision_regions(X=X_combined_std, y=y_combined, classifier=rfc)


# ***

# ## Automated Binary Classification using RandomForestClassifier

# In[28]:


def tree_pred_binary_rfc(data, cols_to_drop, target):
    """
    Inputs
    ------
    data : data file
    cols_to_drop : columns to drop
    target : target tree to predict

    Output
    ------
    cm : confusion_matrix
    plot_decision_regions() : plot results
    """

    # read data
    data_frame = pd.read_csv(data)

    # drop junk columns
    for column in cols_to_drop:
        data_frame = data_frame.drop(column, axis=1)

    # check for null values
    for value in data_frame.columns.values:
        sum_nulls = data_frame[value].isna().any().sum()
    if sum_nulls == 0:
        pass
    else:
        print("There are null values.")

    # create dummies
    species_dummies = pd.get_dummies(data_frame["TreeSpecie"])

    # join old dataframe with dummies and drop `TreeSpecie` column
    new_data_frame = data_frame.join(species_dummies)
    new_data_frame = new_data_frame.drop("TreeSpecie", axis=1)

    # clean columns
    new_data_frame = new_data_frame[new_data_frame["TreeDia"] != "---"]
    new_data_frame = new_data_frame[new_data_frame["TreeDist"] != "---"]
    new_data_frame = new_data_frame[new_data_frame["TreeDist"] != "3?"]

    # split data
    x_vals = ["TreeDia", "TreeDist"]
    y_vals = [target]

    X = new_data_frame[x_vals]
    y = new_data_frame[y_vals].values.ravel()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.7, random_state=1
    )

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))

    # build RandomForest Classifier model
    rfc = RandomForestClassifier(n_estimators=1000, n_jobs=100, random_state=1).fit(
        X_train, y_train
    )

    cm = confusion_matrix(y, rfc.predict(X))

    dr = plot_decision_regions(X=X_combined_std, y=y_combined, classifier=rfc)

    return print(
        "True Negatives:",
        cm[0, 0],
        "\nFalse Negatives:",
        cm[-1, 0],
        "\n\nFlase Positives:",
        cm[0, 1],
        "\nTrue Positives:",
        cm[1, -1],
    )


# In[29]:


tree_pred_binary_rfc(
    data="./Data/corner_trees.csv", cols_to_drop=["OID", "IDTRSD"], target="FIR"
)


# ***

# ## Extra: Binary Classification using KNeighborsClassifier

# In[30]:


from sklearn.neighbors import KNeighborsClassifier


# In[31]:


knn = KNeighborsClassifier()


# In[32]:


parameters = {
    "n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 100],
    "weights": ("uniform", "distance"),
    "n_jobs": [-1],
}


# In[33]:


grid_search = GridSearchCV(knn, parameters).fit(X_train, y_train)


# In[34]:


grid_search_data = pd.DataFrame(grid_search.cv_results_)


# In[35]:


best_model = grid_search_data.loc[:"mean_test_score"].max()
best_model


# In[36]:


best_knn = KNeighborsClassifier(
    n_jobs=best_model.param_n_jobs,
    n_neighbors=best_model.param_n_neighbors,
    weights=best_model.param_weights,
).fit(X_train, y_train)


# In[37]:


confusion_matrix(y, best_knn.predict(X))


# In[38]:


# Build confusion_matrix object
cm = confusion_matrix(y, best_knn.predict(X))

# Plot confusion_matrix
sns.heatmap(cm, annot=True, fmt="d")


# In[39]:


plot_decision_regions(X=X_combined_std, y=y_combined, classifier=best_knn)


# ***

# ## Extra: Automated Binary Classification using KNeighborsClassifier

# In[40]:


def tree_pred_binary_neighbors(data, cols_to_drop, target, neighbors):
    """
    Inputs
    ------
    data : data file
    cols_to_drop : columns to drop
    target : target tree to predict
    neighbors : max range of n_neighbors to build a model on

    Output
    ------
    cm : confusion_matrix
    plot_decision_regions() : plot results
    """

    # read data
    data_frame = pd.read_csv(data)

    # drop junk columns
    for column in cols_to_drop:
        data_frame = data_frame.drop(column, axis=1)

    # check for null values
    for value in data_frame.columns.values:
        sum_nulls = data_frame[value].isna().any().sum()
    if sum_nulls == 0:
        pass
    else:
        print("There are null values.")

    # create dummies
    species_dummies = pd.get_dummies(data_frame["TreeSpecie"])

    # join old dataframe with dummies and drop `TreeSpecie` column
    new_data_frame = data_frame.join(species_dummies)
    new_data_frame = new_data_frame.drop("TreeSpecie", axis=1)

    # clean columns
    new_data_frame = new_data_frame[new_data_frame["TreeDia"] != "---"]
    new_data_frame = new_data_frame[new_data_frame["TreeDist"] != "---"]
    new_data_frame = new_data_frame[new_data_frame["TreeDist"] != "3?"]

    # split data
    x_vals = ["TreeDia", "TreeDist"]
    y_vals = [target]

    X = new_data_frame[x_vals]
    y = new_data_frame[y_vals].values.ravel()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.7, random_state=1
    )

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))

    # Find best model
    knn = KNeighborsClassifier()

    parameters = {
        "n_neighbors": [n for n in neighbors],
        "weights": ("uniform", "distance"),
        "n_jobs": [-1],
    }

    grid_search = GridSearchCV(knn, parameters).fit(X_train, y_train)

    grid_search_data = pd.DataFrame(grid_search.cv_results_)

    best_model = grid_search_data.loc[:"mean_test_score"].max()

    # build best model
    best_knn = KNeighborsClassifier(
        n_jobs=best_model.param_n_jobs,
        n_neighbors=best_model.param_n_neighbors,
        weights=best_model.param_weights,
    ).fit(X_train, y_train)

    cm = confusion_matrix(y, best_knn.predict(X))

    dr = plot_decision_regions(X=X_combined_std, y=y_combined, classifier=best_knn)

    return best_model, print(
        "True Negatives:",
        cm[0, 0],
        "\nFalse Negatives:",
        cm[-1, 0],
        "\n\nFlase Positives:",
        cm[0, 1],
        "\nTrue Positives:",
        cm[1, -1],
    )


# In[41]:


tree_pred_binary_neighbors(
    data="./Data/corner_trees.csv",
    cols_to_drop=["OID", "IDTRSD"],
    target="FIR",
    neighbors=np.arange(1, 100),
)


# ***

# # References

# [Binary Classification](https://stackabuse.com/classification-in-python-with-scikit-learn-and-pandas/#:~:text=%20Binary%20Classification%20%201%20Logistic%20Regression.%20Logistic,fit%20multiple%20Decision%20Trees%20on%20subsets...%20More%20)

# Powell, David C.; Hanberry, Brice B. 2020. Historical tree surveys of the Umatilla National Forest. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS-2020-0051
#
# Raschka, S. and Mirjalili, V., 2019. Python Machine Learning. 3rd ed. Birmingham, UK: Packt.
#
