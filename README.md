# Another_Bitcoin_Predictor

A time series analysis using LSTM RNNs and ARIMA.

## How does it work?
After pulling from the API at [alphavantage.co](alphavantage.co) and preliminary cleaning, we see the raw Bitcoin values. 
<p align="center">
  <img src=“examples/raw_1.png" width="400">
</p>

By adjusting for a weekly rolling average we barely see a change in shape, so it is too early for that adjustment.
<p align="center">
  <img src=“examples/raw_2.png" width="400">
</p>
 
## Autocorrelation
As in all time series trends have a level of autocorrelation where today’s value is dependent yesterday’s. So we will look to see how heavily these data correlate with itself (auto)
<p align="center">
  <img src=“examples/ac_1.png" width="400">
</p>

<p align="center">
  <img src=“examples/ac_2.png" width="400">
</p>

## Time Adjusted
by moving the window from the first day Bitcoin was launched to Oct 25, 2017 we have a far cleaner picture of its patterns. 

<p align="center">
  <img src=“examples/after.png" width="400">
</p>

This window change was picked as it:
As to avoid giving more weight during which Bitcoin was worthless, which while it changes the data, but I felt it was relivant because it show the times during which Bitcoin truly existed.

Bitcoin's very low value could be highly due to its nature being unknown to the majority of the public, after that arbitrary point, it became more well known and thus more active



## Seasonal Decomposition

<p align="center">
  <img src=“examples/season.png" width="400"> 
</p>

Here we see:

a clearer trend over time peaking in late Dec
Evidence that Bitcoin does not seem to be heavily affected by seasonality, only +/- 100
Residuals seem to make up the majority of variability, which makes sense consider how  bitcoins have stronger social driving factors rather than seasonal/global

## LSTM RNN
Using a Recurrent Neural Network with an architecture of:

36 Neuron Dense Layer
4 Memory LSTM Layer
(0.1) Dropout Layer
1 Neuron Dense Layer
Batch : 16
Optimizer : adam
Activator : relu
Loss : mean absolute error
Epochs : 100

That was determined by grid-searching across variable layer depths and activators (Relu, Leaky Relu, & Sigmoid)

## Future Directions
Reddit comments as another predictor.
Non opening values as predictors
ARIMA Modeling
