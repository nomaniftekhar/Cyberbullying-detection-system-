"""Root entry point for Streamlit Cloud. Main file path: streamlit_app.py"""
import os, sys, runpy

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
os.chdir(ROOT)
runpy.run_path(os.path.join(ROOT, "src", "ui", "app.py"), run_name="__main__")
