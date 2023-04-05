import pandas as pd
import matplotlib.pyplot as plt 
def Data():
    
    # Read the dataset into a Pandas dataframe
    df = pd.read_csv("Dataset1.csv")
    df.columns = ["Country Name", "Country Code", "Indicator Name", "Indicator Code", "1960",	"1961",	"1962",	"1963",	"1964",	"1965",	"1966",	"1967",	"1968",	"1969",	"1970",	"1971",	"1972",	"1973",	"1974",	"1975",	"1976",	"1977",	"1978",	"1979",	"1980", "1981",	"1982",	"1983",	"1984",	"1985",	"1986",	"1987",	"1988",	"1989",	"1990",	"1991",	"1992",	"1993",	"1994",	"1995",	"1996",	"1997",	"1998",	"1999",	"2000",	"2001",	"2002",	"2003",	"2004",	"2005",	"2006",	"2007",	"2008",	"2009",	"2010",	"2011",	"2012",	"2013",	"2014", "2015",	"2016",	"2017",	"2018",	"2019",	"2020",	"2021"]
    
    # Line Plot
    df.plot(x="Country Code", y=["1960",	"1961",	"1962",	"1963",	"1964",	"1965",	"1966",	"1967",	"1968",	"1969",	"1970",	"1971",	"1972",	"1973",	"1974",	"1975",	"1976",	"1977",	"1978",	"1979",	"1980", "1981",	"1982",	"1983",	"1984",	"1985",	"1986",	"1987",	"1988",	"1989",	"1990",	"1991",	"1992",	"1993",	"1994",	"1995",	"1996",	"1997",	"1998",	"1999",	"2000",	"2001",	"2002",	"2003",	"2004",	"2005",	"2006",	"2007",	"2008",	"2009",	"2010",	"2011",	"2012",	"2013",	"2014", "2015",	"2016",	"2017",	"2018",	"2019",	"2020",	"2021"])
    plt.title("Year On Year Climate Change Throughout Countries")
    plt.xlabel("Countries")
    plt.ylabel("Climate Change")
    plt.show()
    
    # Use the melt function to transform the dataframe
    df_melted = pd.melt(df, id_vars=['Country Name', 'Indicator Name'], var_name='Year', value_name='Value')
    
    # Separate the melted dataframe into two dataframes: one with years as columns and one with countries as columns
    df_by_year = df_melted.set_index(['Country Name', 'Indicator Name', 'Year']).apply(pd.to_numeric, errors='coerce')
    df_by_country = df_melted.set_index(['Indicator Name', 'Country Name', 'Year']).apply(pd.to_numeric, errors='coerce')
    
    # Line Plot for IND
    india_data = df_by_year.loc['India']
    india_data.plot()
    plt.title("Climate Change Trends in IND")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.show()

    # Line Plot for UK
    india_data = df_by_year.loc['United Kingdom']
    india_data.plot()
    plt.title("Climate Change Trends in UK")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.show()

    # Line Plot for US
    india_data = df_by_year.loc['United States']
    india_data.plot()
    plt.title("Climate Change Trends in US")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.show()

    return df_by_year, df_by_country

# Example usage of the function to read and transform the dataset
df_by_year, df_by_country = Data()

# Perform basic analysis on the dataframe
print(df_by_country.loc['Population growth (annual %)'].describe())
print(df_by_country.loc['Energy use (kg of oil equivalent per capita)'].describe())

# Calculate correlation between two indicators
population_growth = df_by_country.loc['Population growth (annual %)', :, :]
energy_use = df_by_country.loc['Energy use (kg of oil equivalent per capita)', :, :]
corr = population_growth['Value'].corr(energy_use['Value'])

# Scatter Plot
plt.scatter(population_growth['Value'], energy_use['Value'])
plt.title("Correlation between Population growth and Energy use")
plt.xlabel("Population growth")
plt.ylabel("Energy use")
plt.show()


print(f"Correlation between Population growth and Energy use: {corr}")