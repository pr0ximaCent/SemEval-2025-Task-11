import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score
import os
import zipfile

LANG_CODES = ['amh', 'arq' 'hau', 'orm', 'som'] # Language definition
GOLD_FOLDER = 'Path_to_truth_folder_(not_file_path)' # Path_to_truth_folder_(not_file_path)
output_zip = 'Path_to_output_folder'

# Initialize the zip file
with zipfile.ZipFile(output_zip, 'w') as zipf:
    for lang in LANG_CODES:
        print(f"=== Evaluating for Language: {lang} ===")
        
        gold_path = os.path.join(GOLD_FOLDER, f"{lang}.csv")
        pred_path = f"Prediction_file_path_{lang}.csv"
        df_test_gold = pd.read_csv(gold_path)
        df_test_pred = pd.read_csv(pred_path)
        
        emotion_columns = ["anger", "disgust", "fear", "joy", "sadness", "surprise"] # Labels name
        
        gold_labels = df_test_gold[emotion_columns].values
        pred_labels = df_test_pred[emotion_columns].values
        
        precision_micro = precision_score(gold_labels, pred_labels, average='micro')
        recall_micro = recall_score(gold_labels, pred_labels, average='micro')
        f1_micro = f1_score(gold_labels, pred_labels, average='micro')
        
        precision_macro = precision_score(gold_labels, pred_labels, average='macro')
        recall_macro = recall_score(gold_labels, pred_labels, average='macro')
        f1_macro = f1_score(gold_labels, pred_labels, average='macro')
        
        subset_accuracy = np.mean((gold_labels == pred_labels).all(axis=1))
        
        print(
            f"{precision_macro * 100:.2f} & "
            f"{recall_macro * 100:.2f} & "
            f"{f1_macro * 100:.2f} & "
            f"{subset_accuracy * 100:.2f}"
        )

        report = classification_report(
            gold_labels,
            pred_labels,
            target_names=emotion_columns,
            zero_division=0
        )
        
        # Save the classification report to a text file and add to the zip file
        report_filename = f"classification_report_{lang}.txt"
        with open(report_filename, 'w') as report_file:
            report_file.write(report)
        zipf.write(report_filename)

        print("\nClassification Report (per label):\n", report)
        
        plt.rcParams.update({'font.size': 20})
        for i, label in enumerate(emotion_columns):
            cm = confusion_matrix(gold_labels[:, i], pred_labels[:, i])
            plt.figure(figsize=(6, 5))
            sns.heatmap(
                cm, 
                annot=True,       
                fmt='d',          
                cmap='Blues', 
                cbar=False
            )
            plt.title(f"Confusion Matrix for '{label}'")
            plt.xlabel("Predicted")
            plt.ylabel("True")
            plt.tight_layout()
            
            # Save confusion matrix plot as an image file and add to the zip file
            cm_filename = f"confusion_matrix_{lang}_{label}.png"
            plt.savefig(cm_filename)
            zipf.write(cm_filename)
            plt.close()
print(f"All files have been saved and zipped into {output_zip}")
