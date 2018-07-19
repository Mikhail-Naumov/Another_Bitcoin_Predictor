## Time Series Analysis using LSTM RNNs and ARIMA.

#### Repository Contents

| FILENAME |  DESCRIPTION |
|:---------:|:-----------:|
| [README](./README.md) | Repo Overview & Simple Time Series EDA |
| [LSTM README](./README_LSTM.md) | Explanation & Implementation of LSTM |
| [Time Series README](./README_TimeSeries.md) | Explanation & Implementation of ARIMA & Prophet |
| [LSTM Notebook](./BitCoin_LSTM.ipynb) | Notebook with Process & Model |
| [ARIMA & Prophet Notebook](./BitCoin_fbProphet.ipynb) | Notebook with Process and Model |


#### README Contents

- [What is Time Series](#what-is-time-series-analysis)
- [Seasonal Decomposition](#seasonal-decomposition)
- [Model Results](#model-results)
- [Project Concepts](#project-concepts)


### What is Time Series Analysis

Time Series Analysis is the process of interpreting trends from historical data. In this case we will the historical trends of Bitcoin to predict its future, additionally we will use the public perception of Bitcoin as a supplemental variable to facilitate that prediction.
The rationale behind that being, perception may likely affect the trend, and perception will have its own underlying trend.

- note: Public perception of Bitcoin will be determined using sentiment analysis in the Bitcoin & Cryptocurrency subreddit of Reddit. The choice being due to the fact that it is a very large and active community who's main topic of conversation will be Bitcoin.


#### Data Extraction

After pulling from the API at [alphavantage.co](alphavantage.co) and preliminary cleaning, we see the raw Bitcoin opening values. 

![raw_1](https://user-images.githubusercontent.com/36013672/38142892-23cd6de0-340c-11e8-82d5-c9ebc5768bc0.png)

Additionally by using the API [PRAW](https://github.com/praw-dev/praw) to facilitate Reddit Comment aggregation.


#### Rolling Average
*-----------*
Because of how much day to day values may vary, rolling average are used to look at the general trends by looking at the trends by day week month & year

![raw_2](https://user-images.githubusercontent.com/36013672/42914188-f7724a7e-8ac6-11e8-883a-9c2e257b0131.png)

The weekly or monthly rolling average seems to be the cleanest and will likely be used over the daily values. There is not enough years over which data has been collected for looking at a yearly trend to be something you might glean immediate value from.

#### Time Adjusted
Because of the dragging tail, we will move the window of observation from the first day Bitcoin was launched, to Oct 25, 2017 we have a far cleaner picture of its patterns. 

![screen shot 2018-07-18 at 8 17 08 pm](https://user-images.githubusercontent.com/36013672/42914301-a27f0d80-8ac7-11e8-9b9b-d99d21e171fd.png)

![after](https://user-images.githubusercontent.com/36013672/38142889-23b7b81a-340c-11e8-8ecc-797aa7d91ced.png)

This window change was picked as it:
- As to avoid giving more weight during which Bitcoin was worthless, which while it changes the data, but I felt it was relevant because it show the times during which Bitcoin truly existed.

- Bitcoin's very low value could be highly due to its nature being unknown to the majority of the public, after that arbitrary point, it became more well known and thus more active


Again, let us look at the rolling trends
![screen shot 2018-07-18 at 8 19 42 pm](https://user-images.githubusercontent.com/36013672/42914365-efb628fe-8ac7-11e8-8920-b2406b697df8.png)
Here we can see a goldilocks like selection of rolling average:
- Daily : Lots of observations, not very smooth
- Monthly : Very smooth, not many observations
- Weekly : Good balance of smooth & number of observations

##### It would make the most sense to use a Weekly average

#### Autocorrelation
As in all time series analysis have a level of autocorrelation,
"That is to say: today’s value is dependent yesterday’s value".
So we will look to see how heavily these data correlate with itself.

![ac_1](https://user-images.githubusercontent.com/36013672/38142886-239f0bd0-340c-11e8-834f-d95d29378d5d.png)

![ac_2](https://user-images.githubusercontent.com/36013672/38142888-23acd378-340c-11e8-8df2-3ce46d9690d2.png)

##### Each day is autocorrelated up to 2 timestamps


### Seasonal Decomposition

![season](https://user-images.githubusercontent.com/36013672/38142894-23ebed10-340c-11e8-86cf-67c16689e165.png)

Here we see:

- a clearer trend over time peaking in late Dec
- Evidence that Bitcoin does not seem to be heavily affected by seasonality, only +/- 100
- Residuals seem to make up the majority of variability, (>2500) which makes sense considering how bitcoin may have strong social factors driving its growth rather than seasonal/global

### Model Results

| FILENAME |  DESCRIPTION |
|:---------:|:-----------:|
| [LSTM README](./README_LSTM.md) | Explanation & Implementation of LSTM |
| [Time Series README](./README_TimeSeries.md) | Explanation & Implementation of ARIMA & Prophet |
| [LSTM Notebook](./BitCoin_LSTM.ipynb) | Notebook with Process & Model |
| [ARIMA & Prophet Notebook](./BitCoin_fbProphet.ipynb) | Notebook with Process and Model |

#### Univariate LSTM RNN

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

The training data consisted of all the data between the starting point (Oct-25-2017) and March-2018
The testing/predictive data extended past March and into April-25-2018

Our model on the training data
![training](https://user-images.githubusercontent.com/36013672/39268703-9986497a-489e-11e8-911d-44395225bae0.png)

Our model on the testing data
![testing](https://user-images.githubusercontent.com/36013672/39268704-99950546-489e-11e8-8b48-340966a306ed.png)

The LSTM RNN’s architecture was determined by grid-searching across variable layer depths and activators (Relu, Leaky Relu, & Sigmoid)

#### Prophet



### Future Directions
- Reddit comments as another predictor.
- Non opening values as predictors
- ARIMA Modeling

### Project Concepts

Data munging; time series; lstm neural networks, ARIMA, Prophet, Cryptocurrency, magic
