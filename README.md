# -Netflix-Dataset-Analysis-End-to-End-Data-Cleaning-EDA
This project performs a complete exploratory data analysis (EDA) on the Netflix Movies &amp; TV Shows dataset. It includes data cleaning, handling duplicates, missing values, date transformations, feature engineering, visualization and answering business-level analytical questions.

🚀 Project Highlights
✔️ Data Cleaning

Removed duplicate records

Identified and handled missing values

Converted Release_Date into Date_N and extracted Year

Separated Duration into numeric Minutes and Unit (Season/Minutes)

✔️ Feature Engineering

Created new columns:

Date_N — parsed date

Year — integer year

Minutes and Unit — extracted from Duration

✔️ Exploratory Data Analysis (EDA)

Answered multiple business questions including:

How many Movies vs TV Shows are available?

Which year has the most releases?

Which country produces the most TV shows?

What are the top 10 directors?

List TV Shows released in India

Count of Movies with “TV-14” rating in Canada

TV Shows with “R” rating after 2018

Maximum duration of Movies & Shows

Movies released in a particular year

✔️ Visualizations

Bar charts

Countplots

Heatmap for missing values

📁 Tech Stack

Python

Pandas

NumPy

Matplotlib

Seaborn

📂 Project Structure
Netflix-EDA/
│
├── netflix.csv
├── netflix_analysis.ipynb
├── README.md
├── visuals/
│   ├── category_count.png
│   ├── year_distribution.png
│   └── country_tvshows.png

📌 Key Insights

The United States contributes the highest number of TV shows.

Netflix has released movies & shows from 2008 to 2021.

Majority of content is rated TV-MA.

Raúl Campos & Jan Suter directed the highest number of shows/movies.

📝 Conclusion

This project demonstrates real-world data cleaning and EDA skills often tested in Data Analyst / Data Scientist roles.
It shows proficiency in filtering, grouping, date parsing, visualization, and answering business-ready analytical questions.
