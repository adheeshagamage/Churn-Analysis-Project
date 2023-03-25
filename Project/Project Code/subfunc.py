import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def add_numbers(x, y):
    return x + y


def create_plot(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('My Plot')
    plt.show()

def plot_categorical_churn_info(features,churn_df_final):

    fig = plt.figure(figsize=(13, 5*len(features)))


    for i in range(len(features)):

        churn_data_counts = churn_df_final[features[i]].value_counts()
        churn_data_count_dic = churn_data_counts.to_dict()
        churn_data_counts_keys = list(churn_data_count_dic.keys())
        churn_data_counts_values = list(churn_data_count_dic.values())
        colors = ['#3498DB','#F4D03F','#2AAF26','#CB5335']


        
        ax1 = fig.add_subplot(len(features), 2,2*i+1)
        ax1.pie(churn_data_counts_values,colors=colors,labels=churn_data_counts_keys,autopct='%1.1f%%', startangle=90)
        ax1.set_title(features[i]+" Distribution")
        ax1.legend(title = features[i],loc='center left', bbox_to_anchor=(1, 1))


        ax2 = fig.add_subplot(len(features), 2, (i+1)*2)
        prop_by_independent = pd.crosstab(churn_df_final[features[i]], churn_df_final['Churn']).apply(lambda x: x/x.sum()*100, axis=1)
        prop_by_independent.plot(kind='bar', ax=ax2,width=0.3, stacked=True,rot=0, color=['#4FBF3B','#B9963A'])
        ax2.set_title("Churn Based on "+features[i])
        ax2.legend(title = features[i],loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()


def plot_numerical_churn_info(features,churn_df_final):

    fig = plt.figure(figsize=(13, 5 * len(features))) 

    for i in range(len(features)):
        print(features[i])
        churn_data_counts = churn_df_final[features[i]].value_counts()
        churn_data_count_dic = churn_data_counts.to_dict()
        churn_data_counts_keys = list(churn_data_count_dic.keys())
        churn_data_counts_values = list(churn_data_count_dic.values())
        colors = ['#3498DB','#F4D03F']


        ax1 = fig.add_subplot(len(features), 2, 2*i+1)
        churn_df_final[churn_df_final['Churn']=='No'][features[i]].plot(kind='hist', ax=ax1, density=True, alpha=0.5, color=colors[0], label='No')
        churn_df_final[churn_df_final['Churn']=='Yes'][features[i]].plot(kind='hist', ax=ax1, density=True,alpha=0.5, color=colors[1], label='Yes')
        ax1.set_title("Churn Based on "+features[i])
        ax1.set_xlabel(features[i])
        ax1.set_ylabel('Frequency')
        ax1.legend(title = 'Churn',loc='upper right')


        ax2 = fig.add_subplot(len(features), 2, (i+1)*2)
        sns.boxplot(x='Churn',y=features[i],data=churn_df_final[['Churn',features[i]]])
        ax2.set_title("Churn Based on "+features[i])


    plt.tight_layout()
    plt.show()

         
        



