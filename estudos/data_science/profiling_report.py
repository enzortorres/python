import pandas as pd
from ydata_profiling import ProfileReport

data = pd.read_csv("titanic_train.csv")

profile = ProfileReport(data, title="Pandas Profiling Report")

# > Salvando como arquivo HTML
profile.to_file("relatorio_titanic.html")