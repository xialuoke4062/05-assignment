# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: false
import pandas as pd
df = pd.read_csv("wdi.csv")
#
#
#
#
#
#
#
#
#
#| echo: false
summary = df[['gdp_per_capita', 'gdp_growth_rate', 'life_expectancy']].describe()
print(summary)
#
#
#
#
#
#| echo: false
#| label: fig-bar
#| fig-cap: "Bar chart of GDP per Capita (Top 10 Countries)"
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.bar(df['country'][:10], df['gdp_per_capita'][:10])
plt.xlabel("Country")
plt.ylabel("GDP per Capita")
plt.title("GDP per Capita (Top 10)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("gdp_bar.png")
plt.show()
```
#
#
#
#
#
#| echo: false
#| label: fig-scatter
#| fig-cap: "Scatter plot comparing GDP Growth Rate and Life Expectancy"
plt.figure(figsize=(10,6))
plt.scatter(df['gdp_growth_rate'], df['life_expectancy'])
plt.xlabel("GDP Growth Rate")
plt.ylabel("Life Expectancy")
plt.title("GDP Growth Rate vs Life Expectancy")
plt.tight_layout()
plt.savefig("growth_vs_life.png")
plt.show()
```
#
#
#
#
#
#| echo: false
#| label: tbl-stats
#| tbl-cap: "Key statistics for selected indicators"
key_stats = df[['gdp_per_capita', 'gdp_growth_rate', 'life_expectancy']].agg(['mean', 'median', 'std'])
print(key_stats)
```
#
#
#
#
#
#
#
#
