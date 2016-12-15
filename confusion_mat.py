
def show_confusion_matrix(C,class_labels=['0','1']):
    """
    C: ndarray, shape (2,2) as given by scikit-learn confusion_matrix function
    class_labels: list of strings, default simply labels 0 and 1.

    Draws confusion matrix with associated metrics.
    Source: http://notmatthancock.github.io/2015/10/28/confusion-matrix.html
    """
    import matplotlib.pyplot as plt
    import numpy as np
    
    assert C.shape == (2,2), "Confusion matrix should be from binary classification only."
    
    # true negative, false positive, etc...
    tn = C[0,0]; fp = C[0,1]; fn = C[1,0]; tp = C[1,1];

    NP = fn+tp # Num positive examples
    NN = tn+fp # Num negative examples
    N  = NP+NN

    fig = plt.figure(figsize=(8,8))
    ax  = fig.add_subplot(111)
    ax.imshow(C, interpolation='nearest', cmap=plt.cm.gray)

    # Draw the grid boxes
    ax.set_xlim(-0.5,2.5)
    ax.set_ylim(2.5,-0.5)
    ax.plot([-0.5,2.5],[0.5,0.5], '-k', lw=2)
    ax.plot([-0.5,2.5],[1.5,1.5], '-k', lw=2)
    ax.plot([0.5,0.5],[-0.5,2.5], '-k', lw=2)
    ax.plot([1.5,1.5],[-0.5,2.5], '-k', lw=2)

    # Set xlabels
    ax.set_xlabel('Predicted Label', fontsize=16)
    ax.set_xticks([0,1,2])
    ax.set_xticklabels(class_labels + [''])
    ax.xaxis.set_label_position('top')
    ax.xaxis.tick_top()
    # These coordinate might require some tinkering. Ditto for y, below.
    ax.xaxis.set_label_coords(0.34,1.06)

    # Set ylabels
    ax.set_ylabel('True Label', fontsize=16, rotation=90)
    ax.set_yticklabels(class_labels + [''],rotation=90)
    ax.set_yticks([0,1,2])
    ax.yaxis.set_label_coords(-0.09,0.65)


    # Fill in initial metrics: tp, tn, etc...
    ax.text(0,0,
            'True Neg: %d\n(Num Neg: %d)'%(tn,NN),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    ax.text(0,1,
            'False Neg: %d'%fn,
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    ax.text(1,0,
            'False Pos: %d'%fp,
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))


    ax.text(1,1,
            'True Pos: %d\n(Num Pos: %d)'%(tp,NP),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    # Fill in secondary metrics: accuracy, true pos rate, etc...
    ax.text(2,0,
            'False Pos Rate: %.2f'%(fp / (fp+tn+0.)),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    ax.text(2,1,
            'True Pos Rate: %.2f'%(tp / (tp+fn+0.)),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    ax.text(2,2,
            'Accuracy: %.2f'%((tp+tn+0.)/N),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    ax.text(0,2,
            'Neg Pre Val: %.2f'%(1-fn/(fn+tn+0.)),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    ax.text(1,2,
            'Pos Pred Val: %.2f'%(tp/(tp+fp+0.)),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))


    plt.tight_layout()
    plt.show()







'TOPIC MODELING'

def get_user_reviews(user_id):
    review_index = review['user_id'] == user_id
    user_review = review[review_index]
    good = user_review.ix[user_review['stars'] > 3.5]
    bad = user_review.ix[user_review['stars'] <= 3.5]
    return user_review.text,good.text, bad.text


def categorize_reviews(business_id):
    business_index = restaurant_review['business_id'] == business_id # get the business index
    one_restaurant = restaurant_review[business_index]
    good = one_restaurant.ix[one_restaurant['stars'] > 3.5]
    bad = one_restaurant.ix[one_restaurant['stars'] <= 3.5]
    good = good.reset_index()
    bad = bad.reset_index()
    return good.text,bad.text


def vectorizer(X):
    x = []
    for doc in X:
        x.append(clean_text(doc))
    tfidf = TfidfVectorizer(stop_words='english')
    x = tfidf.fit_transform(x)
    indices = np.argsort(tfidf.idf_)[::-1]
    features = tfidf.get_feature_names()
    top_features = [features[i] for i in indices[:50]]
    return top_features

def lda_tm(X):
    x = [clean_text(x) for x in X]
    tfidf = TfidfVectorizer(stop_words='english')
    x = tfidf.fit_transform(x)
    lda = LatentDirichletAllocation(n_topics=15,
                                max_iter=5,
                                learning_method='online',
                                learning_offset=50.)
    terms = tfidf.get_feature_names()
    lda.fit(x)
    C = lda.components_
    for topic,term in enumerate(C):
        top_indices = np.argsort(C)[topic][::-1][:20]
        term_ranking = [terms[i] for i in top_indices]
        print("Topic {}: {}".format(topic+1, ", ".join(term_ranking)))

        
def nmf_tm(x):
    tfidf = TfidfVectorizer(stop_words='english')
    x = tfidf.fit_transform(x)
    nmf = NMF(init="nndsvd",
            n_components=15,
            max_iter=200)
    terms = tfidf.get_feature_names()
    nmf.fit(x)
    W = nmf.fit_transform(x)
    H = nmf.components_
    for topic,term in enumerate(H):
        top_indices = np.argsort(H)[topic][::-1][:10]
        term_ranking = [terms[i] for i in top_indices]
        print("Topic {}: {}".format(topic+1, ", ".join(term_ranking)))
    