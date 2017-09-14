# <center> PROJECT  OBJECTIVES <center>

Yelp has a secret society, Yelp Elite. Elite members bear special badges on their Yelp profiles, and they're invited to private events where up-and-coming restaurants and bars provide food and drinks for free.

However, Yelp is very mysterious in terms of how the company grants a reviewer Elite status. To satisfy community members curiosity, this project aims to use Machine Learning to uncover the secrets of Elite Squad Council and generates a checklist for aspring Elite users. 

In my discovery, Yelp is very strategic in its decision-making process. Users need to create high-quality, reliable reviews and direct traffic to the site in order to qualify for the membership.  
As you can see, votes and compliments ranked higher than review counts and other attributes indicate that Yelp value activities or time on sites heavily when considering for Elite Status, which is a good method to incentivize user engagement on Yelp Website.


**THE CHECKLIST**
 1) votes_useful                   0.167500
 2) compliments                    0.165000
 3) votes_cool                     0.157500
 4) votes_funny                    0.135000
 5) review_count                   0.086250
 6) average_stars                  0.083750
 7) n_friends                      0.080000
 8) yelping_period                 0.053750
 9) fans                           0.051250
10) tip_count                      0.020000

**Algorithms:**

- Logistic Regression

- Random Forest

- Gradient Boosting

- AdaBoost Classifier

- Support vector machines

- MultinomialNB

**Metrics Evaluation**



**WINNER: Random Forest**

 Accuracy: 98 % | Recall: 79% | Precision: 83% | f1: 81 % on USER INFO
 
Accuracy: 79% | Recall: 28%| Precision: 60% | f1: 39% on USER REVIEWS
 
 
 

---------------------------------------------------------------------------------------------------------------------------------------------
**Data Structure:**

Data Source : <https://www.yelp.com/dataset_challenge>

**Business:**
```js
{
    'type': 'business',
    'business_id': (encrypted business id),
    'name': (business name),
    'neighborhoods': [(hood names)],
    'full_address': (localized address),
    'city': (city),
    'state': (state),
    'latitude': latitude,
    'longitude': longitude,
    'stars': (star rating, rounded to half-stars),
    'review_count': review count,
    'categories': [(localized category names)]
    'open': True / False (corresponds to closed, not business hours),
    'hours': {
        (day_of_week): {
            'open': (HH:MM),
            'close': (HH:MM)
        },
        ...
    },
    'attributes': {
        (attribute_name): (attribute_value),
        ...
    },
}
```

**Review**
```js
{
    'type': 'review',
    'business_id': (encrypted business id),
    'user_id': (encrypted user id),
    'stars': (star rating, rounded to half-stars),
    'text': (review text),
    'date': (date, formatted like '2012-03-14'),
    'votes': {(vote type): (count)},
}
```

**User**
```js
{
    'type': 'user',
    'user_id': (encrypted user id),
    'name': (first name),
    'review_count': (review count),
    'average_stars': (floating point average, like 4.31),
    'votes': {(vote type): (count)},
    'friends': [(friend user_ids)],
    'elite': [(years_elite)],
    'yelping_since': (date, formatted like '2012-03'),
    'compliments': {
        (compliment_type): (num_compliments_of_this_type),
        ...
    },
    'fans': (num_fans),
}
```# Yelp-Reviews
# Yelp-Reviews
