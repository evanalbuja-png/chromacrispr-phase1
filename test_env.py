import sys

print("Python:", sys.version)

# Core
import numpy as np
import pandas as pd
import sklearn
import xgboost
import shap
import optuna
import h5py

# Genomics
import pybedtools
import pysam
import cooler
import hic2cool
import pyBigWig

# deepTools import check
import deeptools

print("numpy:", np.__version__)
print("pandas:", pd.__version__)
print("scikit-learn:", sklearn.__version__)
print("xgboost:", xgboost.__version__)
print("shap:", shap.__version__)
print("optuna:", optuna.__version__)
print("h5py:", h5py.__version__)

print("cooler OK")
print("hic2cool OK")
print("pyBigWig OK")
print("pybedtools OK")
print("pysam OK")

print("\nENVIRONMENT OK - ChromaCRISPR Phase 1 ready")
