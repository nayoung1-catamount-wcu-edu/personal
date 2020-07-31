# Comparing 3 Bedroom House Values in North Carolina from June 2019 and June 2020
By Nathan Young

30 July, 2020

I thought, due to COVID, it would be interesting to compare home values in North Carolina to see if COVID had any effect.  I wanted to see if home values in June 2020 decreased by a measurable amount due to COVID compared to home values in June 2019. This data is observational as we not testing anything.  

Due to my work at NC Data Dashboard, I know Zillow has data like this available to the public.  Therefore, I will use data from [Zillow](https://www.zillow.com/research/data/) and choose data that matches 3 Bedroom Home Value by County.  Then I will clean the data to only show counties in North Carolina followed by grabbing each month's respective data. Because the data has already been collected, I will not need to do any collecting and thus do not need to worry about subjects being aware, time of collection, or any other potential variable.

I chose to do a 2 sample z-interval because I felt this matched the data appropriately.  After solving for the means and standard deviations, I calculated the t-stat value.

Equation used:

    t-stat: (x1-x2-hypothesis) / sqrt[(s1^2/n1) + (s2^2/n2)]

With numbers:

    t-stat: (168524.67-175340.33-0) / sqrt[(58942.43^2/99) + (61623.93^2/99)]
            -6815.67 / sqrt[(35093029.50) + (38358674.95)]
            -6816.66 / 8570.396983
    t-stat = -.80

Following the t-stat, I solved for the p value:

Equation used:

    p = 2*tcdf(-1E99, t-stat, n-1)

With numbers:

    p = 2*tcdf(-1E99, -0.79525682, 98)
    p = 0.428386036

With p, I was able to test the hypothesis (`Ho: x1-x2 = 0, Ha: x1-x2 != 0`). I found that the p-value = 0.428 is greater than alpha = 0.05 thus I failed to reject the null hypothesis. There is not significant evidence to suggest that the mean home value of a 3 bedroom house in North Carolina in June 2019 and June 2020 is different. 

After testing the hypothesis, I solved for the confidence interval. 

Equation used:

    ci-upper: (x1-x2) + t*sqrt[(s1^2/n1) + (s2^2/n2)]
    ci-lower: (x1-x2) - t*sqrt[(s1^2/n1) + (s2^2/n2)]

With numbers:

    ci-upper: (168524.67-175340.33) + 1.9845*sqrt[(58942.43^2/99) + (61623.93^2/99)]
              -6815.67 + 1.9845*sqrt[(35093029.50) + (38358674.95)]
              -6815.67 + 1.9845*8570.396983
              -6815.67 + 17007.95281
    ci-upper = 10192.29
              
    ci-lower: (168524.67-175340.33) - 1.9845*sqrt[(58942.43^2/99) + (61623.93^2/99)]
              -6815.67 - 1.9845*sqrt[(35093029.50) + (38358674.95)]
              -6815.67 - 1.9845*8570.396983
              -6815.67 - 17007.95281
    ci-lower = -23823.62281

With everything solved, I am 95% confident that the difference in price of a 3 bedroom house in North Carolina in June 2019 and June 2020 is between `-$23,823.62` and `$10,192.29`.  However, because 0 exists in the interval, there is a possiblity that there is no difference between the two months.

Although COVID did a number to America's economy, values of homes, especially 3 bedroom homes in North Carolina, according to my findings, did not suffer as much loss as I had imagined. 

However, this is just a small portion of data relating to North Carolina only.  A better test to see if there was a major effect would be to test every county in every state in the entire country.  