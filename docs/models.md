# Model overview
**Author:** Felix Fischer (GitHub @felix0097) \
**Date:** 12.06.2023

## TabNet model
* Based on https://arxiv.org/abs/1908.07442
* Implementation: `TabnetClassifier` class under `cellnet/models.py` 
* Trained with cross-entropy loss
* Input features: 19331 protein coding genes
* Feature normalization: Normalize each cell to have 10000 counts + log1p transform
* Output: class probabilities


## Linear model
* Linear model (single fully connected layer) trained with cross-entropy loss
* Implementation: `LinearClassifier` class under `cellnet/models.py` 
* Input features: 19331 protein coding genes
* Feature normalization: Normalize each cell to have 10000 counts + log1p transform
* Output: class probabilities


## MLP model
* Multi-layer perceptron (MLP) model trained with cross-entropy loss
* Implementation: `MLPClassifier` class under `cellnet/models.py` 
* Input features: 19331 protein coding genes
* Feature normalization: Normalize each cell to have 10000 counts + log1p transform
* Output: class probabilities


## XGBoost model
* Based on official XGBoost model: https://xgboost.readthedocs.io/en/stable/ (version 1.6.2)
* Trained with `multi:softprob` objective
* Input features:
  * 256 PCA components (calculated based on all protein coding genes / 19331 genes)
  * PCA is computed based on training data
  * Each cell is normalized to have 10000 counts + log1p transformed before computing PCA
* Output: class probabilities
