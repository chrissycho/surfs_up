# Chrissy Cho's Surfs_Up
### Table of Contents
[ 1. Project Overview ](#desc)<br /> 
[ 2. Resources ](#resc)<br /> 
[ 3. Objectives ](#obj)<br /> 
[ 4. Summary ](#sum)<br /> 
[ 5. Challenge Overview ](#chal)<br /> 
[ 6. Challenge Summary ](#chalsum)<br /> 
[ 7. Challenge Findings ](#find)<br />

<a name="desc"></a>
## Project Overview
In this module, we've learned building database on local computer using SQLite and SQLAlchemy. For a hypothetical investor, W.Avy, we have analyzed weather data of a location in Hawaii to open up a new surf and ice cream store. W.Avy asked us to present data on the weather of the location.

<a name="resc"></a>
## Resources
- Data Source: [climate_analysis.ipynb](https://github.com/chrissycho/surfs_up/blob/master/climate_analysis.ipynb), [hawaii.sqlite](https://github.com/chrissycho/surfs_up/blob/master/hawaii.sqlite)
- Software: Flask, Jupyter Notebook, Python, SQLite

<a name="obj"></a>
## Objectives
- Explain the structures, interactions, and types of data of a provided dataset.
- Differentiate between SQLite and PostgreSQL databases.
- Use SQLAlchemy to connect to and query a SQLite database.
- Use statistics like minimum, maximum, and average to analyze data.
- Design a Flask application using data.

<a name="sum"></a>
## Summary
We have learned Python to SQLite database using SQLAlchemy. We've also performed exploratory climate analysis on precipitation data from August 23, 2016 to August 23, 2017. We have plotted precipitation data by date to investigate whether there are certain days that have more rain than other days. We also have used weather data for various stations to capture minimum, maximum, and average temperature of the area. The station with the highest weather recordings was examined further on the frequency of temperatures. For visualizations, we've used a histogram for the frequency of certian temperature information.

<a name="chal"></a>
## Challenge Overview
In this challenge, you will be finding a few key aspects of Oahu’s seasonal weather data. The investors want to ensure you’ve hit all of the key points before opening the surf shop.

### Challenge Objective
- Determine key statistical data about the month of June.
- Determine key statistical data about the month of December.
- Compare your findings between the month of June and December.
- Make 2 or 3 recommendations for further analysis.
- Share your findings in the Jupyter Notebook.

<a name="chalsum"></a>
## Challenge Summary
For the purpose of the challenge, we have determined minimum, average and maximum temperature of all stations in June and December throughout 2015-2017. We also examined the precipitation data on count, mean, std, min, 25%, 50%, 75%, and max precipitation across all stations in June and December through 2015-2017. We have found interesting findings (See below).

<a name="find"></a>
## Challenge Findings
1) Key Differences in Weather Between June and December
The statistical analysis on the precipitation weather data for June throughtout 2015 to 2017 suggests that the maximum precipitation goes down as the year increases. However, the average precipitation is around 0.12-0.2 in both June and December regardless of year. However, the average temperature throughout December is much lower than that of June regardless of year.

2) Recommendations for further analysis
Although looking at particular months is a great way to start investigating factors that might be affecting the business, I'd recommend investigating all of the months from January to December using a pie chart to see which month in general has higher precipitation percentage. I would also recommend using line graphs for temperatures throughout months for all the years so that we can easily visualize and compare three different years at the same time for each month. 

Most importantly, we need to further investigate on the sales of surfing equipment and ice cream of different stations as there are many factors contributing to the sales. We can start by looking at the profits for each store, highest month of sales, and location of the station. It is important to note that every piece of information is crucial only when we know what we are looking for. Along with the weather data, the sales data can help us decide where and when to open up the new surf and ice cream store. 