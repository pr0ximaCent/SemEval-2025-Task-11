# **SemEval-2025 Task 11: Bridging the Gap in Text-Based Emotion Detection**

This repository contains our implementation for **SemEval-2025 Task 11**, focusing on **Emotion Detection** in text. The goal of this shared task is to detect and classify emotions from text-based data across different languages and intensities, with a focus on bridging the gap in emotion detection using NLP techniques.

- To cite our paper, please use following `bibtex` command.
``` bibtex
@inproceedings{paran-etal-2025-zero_shot,
  title = "{Zero_Shot at SemEval-2025 Task 11: Fine-Tuning Deep Learning and Transformer-based Models for Emotion Detection in Multi-label Classification, Intensity Estimation, and Cross-lingual Adaptation}",
  author = "Paran, Ashraful Islam and Aftahee, Sabik and Hossan, Md. Refaj and Hossain, Jawad and Hoque, Mohammed Moshiul",
  booktitle = "Proceedings of the 19th International Workshop on Semantic Evaluation (SemEval-2025)",
  month = jul,
  year = "2025",
  address = "Vienna, Austria",
  publisher = "Association for Computational Linguistics"
}
```
## **Task Overview**

Text-based emotion detection has become increasingly important for a wide range of applications, from sentiment analysis to human-computer interaction. This task challenges participants to classify emotions in text using three distinct tracks:

### **Tracks**

- **Track A: Multi-label Emotion Detection**  [Link](https://www.codabench.org/competitions/3863/)  
  For a given text snippet, predict the perceived emotion(s) of the speaker from the following categories:  
  - joy, sadness, fear, anger, surprise, disgust.  
  In some languages (e.g., English), disgust may not be considered.  
  **Objective**: Label the text snippet with 1 (emotion present) or 0 (emotion not present) for each emotion.

- **Track B: Emotion Intensity**  [Link](https://www.codabench.org/competitions/4891/)  
  Given a text snippet and a target emotion, predict the intensity of the emotion.  
  **Objective**: For each perceived emotion, assign an intensity score from the following ordinal classes:  
  - 0: No emotion  
  - 1: Low degree of emotion  
  - 2: Moderate degree of emotion  
  - 3: High degree of emotion

- **Track C: Cross-lingual Emotion Detection**  [Link](https://www.codabench.org/competitions/4892/)  
  Given a labeled training dataset in one language, predict the perceived emotion labels for a new text instance in a different target language.  
  **Objective**: Detect emotions in texts from different languages using a model trained in one language.


### **Key Details**

- **Data Sources**: Text snippets in multiple languages (including English and others).  
- **Evaluation Metric**: Macro F1 Score for multi-label classification (Track A and B), Cross-lingual F1 Score for Track C.  
- **Dataset**: Training datasets with emotion labels for Tracks A and B. Track C requires participants to adapt to a new language without a provided training dataset.
  
For dataset access and participation details, visit the **Participate** page [here](https://github.com/emotion-analysis-project/SemEval2025-Task11/).

## **Repository Structure**

```
├── Track A/
│   ├── Figures_(XLM-R)
│   ├── Notebooks/
|   |      ├── ML_Models_Pipeline
|   |      ├── DL_Models_Pipeline
│   ├── Reports_(XLM-R)
|   ├── Utilites/
|   |      ├── Error_Finder.py
|   |      ├── Prediction_Checker.py
├── Track B/
│   ├── Figures_(XLM-R)
│   ├── Notebooks/
|   |      ├── ML_Models_Pipeline
|   |      ├── DL_Models_Pipeline
│   ├── Reports_(XLM-R)
|   ├── Utilites/
|   |      ├── Error_Finder.py
|   |      ├── Prediction_Checker.py
├── Track C/
│   ├── Figures_(BiLSTM+CNN)
│   ├── Notebooks/
|   |      ├── ML_Models_Pipeline
|   |      ├── DL_Models_Pipeline
│   ├── Reports_(BiLSTM+CNN)
|   ├── Utilites/
|   |      ├── Error_Finder.py
|   |      ├── Prediction_Checker.py
├── requirements.txt          # Required Python libraries
├── README.md                 # Project documentation
```
