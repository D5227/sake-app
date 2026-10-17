# sake-app
Japanese sake sweetness and dryness prediction app

## Overview
This web application predicts the approximate sweetness or dryness of Japanese sake using a machine learning model trained on sake ingredient data.

## Technologies
- Python
- Streamlit
- pandas
- scikit-learn
- Random Forest Regressor

## Dataset and License
This application uses data from the following dataset:
- Dataset: [sake_dataset](https://github.com/yoichi1484/sake_dataset)
- License: MIT License
- Copyright: Copyright (c) 2020 Yoichi Ishibashi

The model is trained using selected features from the dataset. Sake meter value is excluded from the prediction inputs.
The original dataset's license is available in the [LICENSE.txt file](https://github.com/yoichi1484/sake_dataset/blob/master/LICENSE.txt).

## Disclaimer
Predictions are estimates for reference only and do not guarantee the actual taste of sake.
