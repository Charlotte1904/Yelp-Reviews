# Yelp Elite User Prediction 


### Goal: Trying to predict user status basing on user information and review texts 

**Algorithms:**

-Logistic Regression

-Random Forest

-Gradient Boosting

-AdaBoost Classifier

-Support vector machines

-MultinomialNB

**Metrics Evaluation**



**WINNER: Random Forest **

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
