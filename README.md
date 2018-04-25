# Another_Bitcoin_Predictor

A time series analysis using LSTM RNNs and ARIMA.

## How does it work?
After pulling from the API at [alphavantage.co](alphavantage.co) and preliminary cleaning, we see the raw Bitcoin values. 

![raw_1](https://user-images.githubusercontent.com/36013672/38142892-23cd6de0-340c-11e8-82d5-c9ebc5768bc0.png)

By adjusting for a weekly rolling average we barely see a change in shape, so it is too early for that adjustment.

![raw_2](https://user-images.githubusercontent.com/36013672/38142893-23e0c552-340c-11e8-9999-6ec0fdde6b03.png)
 
## Time Adjusted
by moving the window from the first day Bitcoin was launched to Oct 25, 2017 we have a far cleaner picture of its patterns. 

![after](https://user-images.githubusercontent.com/36013672/38142889-23b7b81a-340c-11e8-8ecc-797aa7d91ced.png)

This window change was picked as it:
- As to avoid giving more weight during which Bitcoin was worthless, which while it changes the data, but I felt it was relivant because it show the times during which Bitcoin truly existed.

- Bitcoin's very low value could be highly due to its nature being unknown to the majority of the public, after that arbitrary point, it became more well known and thus more active


## Autocorrelation
As in all time series analysis have a level of autocorrelation wherein today’s value is dependent yesterday’s. So we will look to see how heavily these data correlate with itself.

![ac_1](https://user-images.githubusercontent.com/36013672/38142886-239f0bd0-340c-11e8-834f-d95d29378d5d.png)


![ac_2](https://user-images.githubusercontent.com/36013672/38142888-23acd378-340c-11e8-8df2-3ce46d9690d2.png)



## Seasonal Decomposition

![season](https://user-images.githubusercontent.com/36013672/38142894-23ebed10-340c-11e8-86cf-67c16689e165.png)

Here we see:

- a clearer trend over time peaking in late Dec
- Evidence that Bitcoin does not seem to be heavily affected by seasonality, only +/- 100
- Residuals seem to make up the majority of variability, which makes sense consider how  bitcoins have stronger social driving factors rather than seasonal/global

## LSTM RNN
Using a Recurrent Neural Network with an architecture of:

- 36 Neuron Dense Layer
- 4 Memory LSTM Layer
- (0.1) Dropout Layer
- 1 Neuron Dense Layer
  - Batch : 16
  - Optimizer : adam
  - Activator : relu
  - Loss : mean absolute error
  - Epochs : 100

![lstm](https://user-images.githubusercontent.com/36013672/38142891-23c39f4a-340c-11e8-9495-b43548a037bd.png)

That was determined by grid-searching across variable layer depths and activators (Relu, Leaky Relu, & Sigmoid)

## Future Directions
- Reddit comments as another predictor.
- Non opening values as predictors
- ARIMA Modeling
