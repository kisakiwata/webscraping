
### Project Summary
The project's goal was to understand the large picture of plant-based product market.
My main interest came from the news headlines we frequently encounter these days that meat alternatives and other bio-engineered alternatives are on the rise (30% growth of sales from 2018) and that large fast-food chains such as Burger King offer meat-less burgers at the stores now. Originally, I wanted to understand the reasons why people buy those products - such as for health reasons (diabetes, etc.) or for personal reasons. Yet due to lack of reviews on the website that was available to web-scrape, I limited the scope and focused more to understand the plant-based product market from the wholesaler perspective.

### Web-scraped website
I web-scraped the website of grocery supermarket called "Freshdirect.com".
It markets itself as kosher, glute-free, and organic, and caters towards consumers who buy into those items, which I thought would be a good place to start to analyze the market trend for those who choose to buy vegetarian or vegan items.
 
### Exploratory Data Analysis
First, I checked top brands (by product count) and interestingly most of brands were from dairy category. So, I created a bar chart by large category types and small category types.
(See the first bar plot in jupyter notebook)

These clearly displayed that 80% of plant-based items are dairy products and inside these items, alternative milk covered the shelf most.

The pie chart explains better:
(See the pie chart in jupyter notebook)

Even after I remove the outlier plant-based milk category from the chart, pantry (bulk milk items) and other dairy (cream, cheese, yogurt, etc.) were high up.
(See the chart "Products by Category #1 and #2) in jupyter notebook)

Now shifting the gear towards more about the popularity rather than the sheer count, the boxplot by major category type (dairy, grocery, and frozen) showed interesting results. Frozen category had the highest median popularity score, although it had the smallest share in the variety.
(See the box plot in jupyter notebook) 

If you drill down into smaller category type, interestingly, plant-based milk product popularity was not that high, compared with the product coverage. See below:
(See the bar plot "Category #2" in jupter notebook)

On the other hand, cream, creamers, cheese, ice cream, and yogurt were very popular - although dairy alternatives in general are pretty sought out, the popularity is pretty divided inside them. It is worth it to mention that meat alternatives ranked really low for both product coverage and popularity. 
Chart with even further detailed category:
(See the last bar plot "Category #3" in jupyter notebook)

### Conclusion and Next Step
From both popularity and product count perspectives, meat alternatives have not still reached their highest potential yet despite of all the heat in the news.
If you are a new seller in the food industry - especially in the vegan/vegetarian market, there is still a lot of room to learn from or probably wiggle in the dairy section such as alternative milk, creamers, cheese, yogurt, ice cream etc. Ice cream market is quite small, yet very popular, which could open up a lot of doors if somebody wants to step into the industry.
It should be noted that since the "popularity" ranking was defined by the Freshdirect and no reviews are provided on the website, the next step would be to explore websites with customer reviews and understand why some products are more popular than others - how factors such as price or taste boost or limit the sales - would be the next question to be asked for this data analysis project.

