import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")

#diamonds = sns.load_dataset("diamonds")
diamonds = pd.read_csv('/Users/Zamalutdinov/Desktop/diamonds.csv')

f, ax = plt.subplots(figsize=(6.5, 6.5))
plt.title('Diamonds plot')
cut_ranking = ["Ideal", "Premium", "Very Good", "Good", "Fair"]
sns.scatterplot(x="carat", y="price",
                hue="cut",
                palette="flare",
                hue_order=cut_ranking, s=6,
                linewidth=0,
                data=diamonds, ax=ax)
#plt.show()
plt.savefig('Task3.png')
