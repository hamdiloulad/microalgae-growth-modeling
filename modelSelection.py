import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor
import lightgbm as lgb
import xgboost as xgb

def selection(X_validation, y_validation, X_train, y_train):
    results = []
    models = ["XGBoost", "CatBoost", "LightGBM"]

    aic_scores = []
    r_squared_values = []

    for model_type in models:
        # Create and train the model
        if model_type == "XGBoost":
            model = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.3, learning_rate=0.1,
                                     max_depth=5, alpha=10, n_estimators=10)
        elif model_type == "CatBoost":
            model = CatBoostRegressor(iterations=50, depth=6, learning_rate=0.1, loss_function='RMSE')
        elif model_type == "LightGBM":
            model = lgb.LGBMRegressor(objective='regression', metric='mse', boosting_type='gbdt',
                                      num_leaves=40, learning_rate=0.05, num_boost_round=100)

        model.fit(X_train, y_train)

        # Make predictions on the validation set
        y_pred_validation = model.predict(X_validation)

        # Calculate mean squared error
        mse = mean_squared_error(y_validation, y_pred_validation)

        # Get the number of model parameters
        num_params = model.n_features_in_ if hasattr(model, 'n_features_in_') else len(model.feature_importances_)

        # Calculate AIC
        n = len(y_validation)
        AIC = -2 * np.log(mse) + 2 * num_params
        aic_scores.append(AIC)  # Take the absolute value of AIC scores

        # Calculate R-squared
        r_squared = r2_score(y_validation, y_pred_validation)
        if r_squared < 0:
            r_squared = 0
        r_squared_values.append(r_squared)

    x = np.arange(len(models))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8.4, 3.9))  # Set the desired width and height of the plot
    modelss = ["XGBoost", "CatBoost", "LightGBM"]

    # AIC scores
    bar1 = ax.bar(x - width / 2, aic_scores, width, color='#E85D35', alpha=1, label='AIC', zorder=2)
    ax.set_xlabel('Models')
    ax.set_ylabel('AIC Scores')

    # Adjusted R-squared values
    ax2 = ax.twinx()  # Create a twin axes sharing the x-axis
    bar2 = ax2.bar(x + width / 2, r_squared_values, width, color='#70CAC6', alpha=1, label='R-squared', zorder=1)
    ax2.set_ylabel('R-squared Values')

    ax.set_xticks(x)
    ax.set_xticklabels(modelss, fontdict={'fontsize': 6})

    ax.yaxis.grid(True, linestyle='dashed', color='grey', alpha=0.4, zorder=0)  # Set dashed grey grid lines for y-axis
    ax.set_yticks(np.linspace(ax.get_yticks()[0], ax.get_yticks()[-1], len(ax2.get_yticks())))
    # Add values above the AIC score bars
    for rect in bar1:
        height = rect.get_height()
        ax.annotate(f'{int(height)}', xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom', fontsize=8)

    # Add values above the R-squared value bars
    for rect in bar2:
        height = rect.get_height()
        ax2.annotate(f'{height:.2f}', xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3),
                     textcoords="offset points", ha='center', va='bottom', fontsize=8)

    fig.tight_layout()
    fig.legend(loc='upper right', bbox_to_anchor=(1, 1))
    fig.subplots_adjust(right=0.8)
    plt.savefig('D:\\DataProject\\venv\\inrhMicroalgae\\result\\modelSelection.png')
    plt.show()
