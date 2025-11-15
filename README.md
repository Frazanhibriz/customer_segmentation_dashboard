<h1 align="center">📊 Customer Segmentation Dashboard</h1>

<p align="center">
Interactive Streamlit dashboard visualizing customer behavior and K-Means segmentation results.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=flat-square&logo=streamlit" />
  <img src="https://img.shields.io/badge/Machine%20Learning-KMeans-blue?style=flat-square&logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Status-Live-success?style=flat-square" />
</p>

---

## 🚀 Overview
This dashboard provides an interactive interface to explore **customer segments** generated using a K-Means clustering model.

It helps visualize:
- Cluster proportions  
- Behavioral differences across segments  
- Booking patterns  
- Cancellations & engagement  
- Key feature distributions  

---

## ✨ Features
- 📌 Cluster Distribution (Pie & Bar Charts)  
- 🔥 Behavioral Heatmap (Feature Comparison)  
- 🔍 Cluster Explorer (Drill-down View)  
- 🌙 Modern Dark UI  
- 📈 Plotly Interactive Visualizations  

---

## 📁 Project Structure

customer_segmentation_dashboard/
│── app.py
│── requirements.txt
│── data/
│ └── user_features_with_clusters.csv
│── README.md

---

This dashboard is built using the clustering results from the main analysis project.

Full modelling workflow, notebooks, and analytical documentation:  
👉 **Customer Segmentation & Behavioral Analysis**  
https://github.com/Frazanhibriz/hotel_booking_user_segmentation

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

---
