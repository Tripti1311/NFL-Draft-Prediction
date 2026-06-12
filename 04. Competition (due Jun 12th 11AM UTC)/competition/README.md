# [README] Competition: NFL Draft Prediction

## GCI World 2026 April

### Competition Starts: April 29th 12PM UTC

### Competition Ends: ~~June 10th 11AM UTC~~ June 12th 11AM UTC (date corrected on May 12th)

### Ranking Announcement: July 8th (Session 14)


## Where To Submit



Omnicampus:

https://edu.omnicamp.us/courses/137/

## Overview



In this competition, your goal is to build a classification model that predicts whether an athlete will be selected in the **National Football League (NFL)** Draft ("Drafted" vs. "Not Drafted") using data such as physical performance test results and position information.



### What Is the NFL Draft?



The NFL is the top professional American football league, and the **Draft** is its annual player selection event. Each of the 32 NFL teams takes turns choosing from a pool of eligible college players, acquiring the rights to sign them as professional athletes. Being drafted is a major milestone — it means a player has been recognized as talented enough to compete at the highest level.



Teams evaluate players based on many factors: athletic ability (speed, strength, agility), playing position, college performance, and more. Generally, **players who demonstrate stronger physical performance and skills are more likely to be drafted**, but the final decision involves many considerations.



![NFL Draft](https://www.nytimes.com/athletic/live-blogs/nfl-draft-2025-live-updates-picks-trades-grades-round-1/dEflNpexDSoU/)



Image Source: https://www.nytimes.com/athletic/live-blogs/nfl-draft-2025-live-updates-picks-trades-grades-round-1/dEflNpexDSoU/

In this competition, you will use features such as performance metrics (e.g., Sprint_40yd, Vertical_Jump, Bench_Press_Reps), position, body measurements, and school to predict **Drafted** (values closer to **1** indicate drafted; values closer to **0** indicate not drafted).



Let’s take on a practical prediction task and experience the excitement of **sports × data science!**

##Task

Using the available data—such as players’ athletic test results, physical measurements, and position information—predict whether each player will be selected in the NFL Draft.



In this competition, the **“Drafted”** column is the target variable, and all other columns are the features. A **“Drafted”** value closer to **1** indicates that the player **was drafted**, while a value closer to **0** indicates that the player **was not drafted**.

## Data

In data science competitions, you are typically provided with **training data** and **test data**. In this competition, the **training dataset is** `train.csv` and the **test dataset is** `test.csv`. The two datasets differ as follows:

- **Training data**: Used to train your machine learning model.

- **Test data**: You submit predictions for this dataset, and your score is evaluated based on those predictions.  



The variables included in the dataset are as follows:  



Variables |Definition

---|---

Id |A unique ID for each player

Year |The year the record corresponds to

Age |Player age

School |School name

Height |Height

Weight |Weight

Sprint_40yd |40-yard dash time

Vertical_Jump |Vertical jump reach

Bench_Press_Reps |Number of bench press repetitions

Broad_Jump |Broad jump distance

Agility_3cone |3-cone drill time

Shuttle |20-yard shuttle time

Player_Type |Broad role category

Position_Type |Position type

Position |Specific position

Drafted |Whether the player was drafted

## How to Get Started

---

### Data

Once you unzip the `competition.zip` file, you should see the following files inside `competition` folder:

* `README.ipynb`: This notebook

* `baseline.ipynb`: Tutorial notebook to get started on the competition

* `input` folder

    * `train.csv`: Data to **train** your own machine learning model

        * `Drafted` column is the target variable

            * `1` means "drafted"

            * `0` means "not drafted"

        * All other columns are explanatory variables

    * `test.csv`: Data to **evaluate** your trained model. You will be competing to achieve higher prediction accuracy on this data.

    * `sample_submission.csv`: Example of the CSV file to submit



### First Steps

Open the `baseline.ipynb` and run all cells. This will create a new file, `output/submission.csv`. Download the file to your PC, then upload on Omnicampus. You should then be able to see your score on the leaderboard.



### How to Improve Your Model

Here are some tips to get a higher ranking on the competition:

- [ ] **Step 1: Understand the data using visualizations**

- [ ] **Step 2: Preprocess the data**

    - Decide what preprocessing is needed based on your findings from Step 1

    - The tutorial only uses 5 features to create the model, so try adding more features

- [ ] **Step 3: Improve your model**

    - Optimize the hyperparameters of your model

    - Explore different models



We will also share some techniques you can use in lectures and office hours, so stay tuned!

## Evaluation Metric

In this competition, submissions are evaluated using **AUC**—[the Area Under the ROC Curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)—computed between the predicted probabilities for the test data and the ground-truth labels. The goal is to achieve the **highest AUC score** possible.

## Submission/Scoring/Leaderboard

Please submit your predictions via **Omnicampus**. Your submission must be a CSV file in the format described below.



Id|Drafted

---|---

2781|0.5

2782|0.5

2783|0.5

…|…

3474|0.5

3475|0.5

3476|0.5



Please follow the format in **sample_submission.csv**. Submissions not adhering to this format will receive a score of -1, so please check your file format if you encounter this issue.



The number of submissions is unlimited. However, scoring results may not be immediately reflected. When checking your results, please ensure that the scoring timestamp has been updated.



During the competition period, scoring will be conducted on a subset of the test data. This approach helps prevent "leaderboard overfitting." Based on these interim results, the leaderboard on Omnicampus will be updated during the competition. This leaderboard, reflecting scores based on a subset of the test data, is referred to as the **Public Leaderboard**.



In contrast, after the competition ends, final scoring will be performed on the entire test data. The final rankings will be determined based on this comprehensive evaluation. The leaderboard generated from this final scoring is referred to as the **Private Leaderboard**, in contrast to the Public Leaderboard.



Final rankings will be determined based on the **last submitted file**.



Participants ranked high on the Private Leaderboard will be requested to submit code that runs on Google Colab. This is to verify reproducibility before confirming the final rankings. We appreciate your cooperation in this matter.

## Rules

- **Prohibition of External Data Usage**  



No external data may be used at any stage of the analysis. You must rely solely on the provided datasets (input/train.csv and input/test.csv).



- **Prohibition of Hand-Labeling**  



Creating predictions manually instead of using a model is referred to as Hand-Labeling, and it is prohibited in most data science competitions. This rule also applies to this competition, prohibiting Hand-Labeling for all or part of the test data. **Making manual decisions for part of the predictions** based on rules or specific conditions derived from EDA (Exploratory Data Analysis) also falls under Hand-Labeling. All predictions must be generated by a model, and manual predictions are not permitted. Data processing must be based on reproducible methods, and the submitted predictions must be **automatically generated** by a model that can also be applied to other data with similar characteristics.



- **Ensuring Reproducibility**  

  

Ensure reproducibility of your predictions as much as possible. To achieve this, it is essential to **set seed values for random number generation**.



The phrase "as much as possible" is used because there are situations where reproducibility cannot be fully guaranteed. For example, recent updates to the PyTorch deep learning framework have caused overall precision to decrease. In such cases, reproducing predictions made with an earlier version would require downgrading the framework. However, for this competition, such measures are not required to ensure reproducibility.





- **Permission for Private Sharing**  



In data science competitions, private information sharing is typically strictly regulated from a fairness perspective. In most cases, information sharing within a team is only permitted when the team formation is declared through official channels. Personal information sharing outside the team, referred to as **Private Sharing**, is strictly prohibited.

However, since this competition is positioned as a tutorial for beginners, the Private Sharing prohibition will not be applied. If you have experienced individuals nearby, you are encouraged to actively seek their advice, and you may also exchange information and discuss with other participants online. When engaging in online discussions with other participants, please try to conduct these interactions in public forums rather than private channels, ensuring that all participants can share insights.



- **Citing Original Sources (Reference Code)**  



This competition has numerous high-quality and informative notebooks reported on the internet. Exploring such excellent approaches and deciphering code is also a form of learning, so please feel free to reference them. There is absolutely no problem with referencing others' code.

From an educational standpoint, GCI distinguishes between one's own work and citations. Therefore, when you quote code, please explicitly indicate the original source. For top-ranking participants in this competition, code disclosure is required. If it is discovered during this disclosure that the original source was not cited, and the code is clearly from another source, there is a possibility that the prize may be revoked. Therefore, it is recommended to keep a record of the notebooks you referenced to track which codes you have used.

