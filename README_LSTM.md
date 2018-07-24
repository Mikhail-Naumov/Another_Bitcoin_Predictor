# LSTM (Uni & Multivariate)

An explaination of:
- [What are LSTM RNNs](#what-are-lstm-rnns)
- [Implimentation of Multi vs Univariate models](#implimentation-of-multi-vs-univariate-models)
- [Usage in predicting Bitcoin Values](#usage-in-predicting-bitcoin-values)

### What are LSTM RNNs

### Implimentation of Multi vs Univariate models

### Usage in predicting Bitcoin Values

![split](https://user-images.githubusercontent.com/36013672/43160377-f8cac122-8f52-11e8-8421-35539b278923.png)

### Univariate Model

![uni_train_history](https://user-images.githubusercontent.com/36013672/43160378-f8dcd268-8f52-11e8-9b0c-db3f65c083a6.png)

![uni_pred](https://user-images.githubusercontent.com/36013672/43160380-f8fe16b2-8f52-11e8-9034-48d7eb5f7721.png)
* Left: Predicted values compared to True
* Right: Comparing that difference between predicted percent variation from Prediction and True, closer to 0 means closer to actual daily variation exhibited by True BTC values

### Multivariate Model

![multi_train_history](https://user-images.githubusercontent.com/36013672/43160376-f8a9d584-8f52-11e8-85cd-e98ec0daa74f.png)
![multi_pred](https://user-images.githubusercontent.com/36013672/43160379-f8eb714c-8f52-11e8-84aa-c64772cdae3b.png)
* Left: Predicted values compared to True
* Right: Comparing that difference between predicted percent variation from Prediction and True, closer to 0 means closer to actual daily variation exhibited by True BTC values

### Model Comparision

![compare_pred](https://user-images.githubusercontent.com/36013672/43160382-f964664c-8f52-11e8-8502-a47f5d16ee44.png)
* Left: Predicted values compared to True
* Right: Comparing that difference between predicted percent variation from Prediction and True, closer to 0 means closer to actual daily variation exhibited by True BTC values

![mae](https://user-images.githubusercontent.com/36013672/43160381-f92fbdfc-8f52-11e8-8905-6c1e10caffe4.png)
