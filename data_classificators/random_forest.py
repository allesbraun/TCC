from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

#creating an instance of the RandomForestClassifier
rfc = RandomForestClassifier(random_state=42)
