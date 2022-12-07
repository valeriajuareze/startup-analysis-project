# Startup Analysis Project

This is a project to analyze the startup ecosystem in the United States. Startups are companies created by entrepreneurs to develop a scalable business model. The goal of this project is to analyze the startup ecosystem in the United States and to identify the factors that contribute to the success of a startup. 

The project will be divided into two parts:

**1.** The first part will be an exploratory data analysis of the data set. 

**2.** The second part will be a predictive analysis of the data setThe predictive analysis will be used to identify the factors that contribute to the success of a startup.

## Background 

Startups are small companies created by a group of individuals to solve a specific problem or to bring something new to the market, in other words they do what the other companies don't<sup>1</sup>. Thanks to them we have new services or new ideas and with a capitalist economic structure this kind of projects are supported, not only that but in 2022 Jeremy Jurgens from the World Economic Forum declared that startups are crucial in creating societal change and driving economic recovery for the phenomenon that was Covid-19<sup>2</sup>. Some of the perks of having startups are: 

**1)** Innovation

**2)** Creating new jobs

**3)** Possibilities for people and lastly 

**4)** Productivity.

When somebody says startups the first think coming into mind is something like Facebook or uber but that ́s not always the case, generally the startups are small business like restaurants or health/Fitness locals, this are the common type of startups. In the last years there has been an increase in technological startups in different fields like cyber-security, digital-health, cloud platforms and others.

In everything there is risk and startups are not the exception, because startups are created for a specific problem sometimes they don ́t get enough funding, 90% of startups will fail, the major reason that they detected was no market need and run out of money. Other considerations startups face is where to open a new business, states have different regulations like permits, cost of living, taxes and more. Sophia Lanier made a ranking to see which states where friendlier or better to start, there was a tendency in which the states in the south had better opportunities for startups in different ways<sup>3</sup>.

## Presentation 

The link to our presentation is [here](https://docs.google.com/presentation/d/1Oyu_kEITHVKCCUWrZfj4mfKa47yleF4Zf7C6csSKTVY/edit?usp=sharing)

## Data

The data set used in this project was obtained from [Kaggle](https://www.kaggle.com/). More specifically, the [startup database](https://www.kaggle.com/datasets/manishkc06/startup-success-prediction) contains information of over **900** startups in the US that span across several industries and states. This data was then joined with another relevant [database](https://apps.bea.gov/itable/?ReqID=70&step=1#eyJhcHBpZCI6NzAsInN0ZXBzIjpbMSwyNCwyOSwyNSwzMSwyNiwyNywzMF0sImRhdGEiOltbIlRhYmxlSWQiLCI2MDAiXSxbIkNsYXNzaWZpY2F0aW9uIiwiTm9uLUluZHVzdHJ5Il0sWyJNYWpvcl9BcmVhIiwiMCJdLFsiU3RhdGUiLFsiMCJdXSxbIkFyZWEiLFsiWFgiXV0sWyJTdGF0aXN0aWMiLFsiMSJdXSxbIlVuaXRfb2ZfbWVhc3VyZSIsIlBlcmNlbnRDaGFuZ2UiXSxbIlllYXIiLFsiLTEiXV0sWyJZZWFyQmVnaW4iLCItMSJdLFsiWWVhcl9FbmQiLCItMSJdXX0=) which was comprised of the porcentual change of annual GDP in the 51 states of the US.

## Data Cleaning

The data set was cleaned to remove any missing values. The data set was also normalized to ensure that the data was in a format that could be used for the analysis. There were several variables in the data set that could not be used or that had to be processed for a machine learning model to understand. The following are the general changes that were made to the dataset:

- The **State_code** was replaced with a binary variable that indicated whether the startup was located in a state or not. However, other location variables such as **latitude**, **longitude**, **city**, and **Zip_code** were removed from the data set.
- The **name** of the startup was removed from the data set because it is a unique value for each startup and it would not be useful for the analysis.
- The **labels** variable was used as the target variable as it indicates whether a variable was acquired or closed.
- The time variables such as **founded_at** and **closed_at** **first_funding_at** and **last_funding_at** were converted to a readable date format since there were calculations made with these. These variables were all dropped but not before two new variables were created: **founded_first_funding_days_difference** and **first_last_funding_days_difference**. These two indicate the number of days between the founding of the startup and the first funding and the number of days between the first and last funding.
- There are variables related to the number of **milestones** that a startup has and the number of days since founding that they were reached. Some startups never reached these milestones and therefore a new variable was created as a binary variable that indicated whether a milestone was reached or not. This variable was called **Reached_milestone**. The original **Milestones** variable was processed so that the NaN values of startups that never reached a milestone were replaced with 999.
- The **relationships** variable explains how many key relationships a startup has with key players in the industry.
- The variables related to funding such as **funding_rounds**, **funding_total_usd**, and the hot encoded variables related to the type of funding were kept for the analysis.
- Another hot encoded variable was the **category_code** variable. This variable was hot encoded to indicate the type of industry that the startup was in and was dropped after the hot encoding.
- **is_top500** was a binary variable that indicated whether a startup was in the top 500 startups in the US or not. This variable was kept for the analysis.

The data set was then split into a training set and a test set.

The training set was used to train the model and the test set was used to test the model.

The data was obtained from Kaggle, which is in the public domain.


## Model Selection
----
The presence of Nas on our data was do to the nature of startups and randomness, sometimes they got bought or failed before the first milestone so we decided to fill them with value and we settled to go for 999 because we had real 0 in our dataset, putting them as equal will mean something really different from what they truly are and it will skew the model decision.

The ouptut we expected where 0 or 1, because of the behaviour of the data we needed a classifier for better results, 2 models where selected, Logistic Regression (LR) and Random Forest Classifier (RF). LR is an analogous to multiple linear regression with a binary output, due to its fast computational speed and structured model approach it is a popular method and a good way to start, and RF is created from several weak learners (decision trees) where the result will be the most repeated outcome between the trees, this reduces the chances of overfitting that comes with weak learners. 


We didn´t like the first result so we opted to create new models with less features selected from the random forest importances module in sklearn, with 13 features LR did better but still had a low recall score, because the importance of not missing even one 0 this model wasn´t our choice, we tried with neural networks with different hidden layers and activation functions with a 100% accuracy score for training and less than 75% test score we decided that neural networks didn´t work for us.



Another ensemble method we tried was Gradient Boosting, the difference between boosting and bagging is that while bagging reduces variance boosting focus in reducing bias which gives it an advantage at trying to match the training set. Another difference is that bagging tries to get the best result by "voting" between the weak learners and boosting tries to learn from each prediction to create "the best possible next model".
Gradient boosting being a non-parametric doesn´t need any type of distribution, they don´t seem affected by outliers and it has flexibility selecting the loss function. 

We tried Gradient Boosting with different learning rates and got a 81% test score with a 76% AUC and a 48% loss score so we opted that this was our model, then created a Random Grid Search to look for the best parameters, after some parameter tunning we decided to go for a slow learning rate of 0.05, max features of 8 and a max depth of 2, a minimum sample leaf of 0.1, the will be deviance, and lastly a subsample of 0.95


![report_score](/startup-project/Resources/model_selection/Gradient_boosting_score.png)


fig 1. report for gradient boosting classifier model




![AUC](/startup-project/Resources/model_selection/AUC_gradient_boosting.png)

fig 2. AUC score for our gradient boosting classifier model
