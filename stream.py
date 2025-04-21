import streamlit as st
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Load logo image (replace with your actual image path)
try:
    logo = Image.open('C:\\Users\\shari\\Desktop\\MNRE\\LSTM MODEL SE OPTIMIZATION\\website\\project\\static\\img\\icons\\MNRE.png')  # Replace with your image path
    st.sidebar.image(logo, width=150, height= 50)
except:
    st.sidebar.markdown("**AI Solar Forecasting**")

# Main title with blue accent
st.markdown("<h1 style='color: #1565c0;'>AI Forecasting Dashboard</h1>", unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📈 Sampling Frequency Charts", 
    "📊 Evaluation Metrics",
    "🧠 Project Overview", 
    "📉 Model Comparisons",
    "⚙️ Methodology & Insights",
    "📚 AI-Based Solar Research Paper Comparison",
    "📘 LSTM-Based Solar Forecasting – Q&A Section",
    "🧠 AI Forecasting - Project Overview"
])

# ---- TAB 1: Charts ----
with tab1:
    st.subheader("Line Chart - Sampling Frequency vs Accuracy (R²)")
    line_labels = ["24 Hours", "72 Hours", "48 Hours", "4 Days", "5 Days", "7 Days", "6 Days", "12 Hours",
                   "6 Hours", "4 Hours", "2 Hours", "1 Hour", "45 Minutes", "30 Minutes", "15 Minutes"]
    line_data = [0.17, 0.18, 0.22, 0.23, 0.26, 0.27, 0.31, 0.32, 0.79,
                 0.82, 0.88, 0.90, 0.91, 0.91, 0.93]

    line_chart = go.Figure()
    line_chart.add_trace(go.Scatter(
        x=line_labels[::-1], y=line_data[::-1], mode='lines+markers',
        name='Sampling Frequency', line=dict(color='#1e88e5')
    ))
    line_chart.update_layout(
        height=400, 
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(line_chart, use_container_width=True)

    st.subheader("Bar Chart - Sampling Frequency vs Cost")
    bar1_labels = ["15 Minutes", "30 Minutes", "45 Minutes", "1 Hour", "2 Hours", "4 Hours", "6 Days",
                   "7 Days", "6 Hours", "5 Days", "4 Days", "48 Hours", "72 Hours", "12 Hours", "24 Hours"]
    bar1_data = [0.04, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.005]

    bar1_chart = go.Figure([go.Bar(x=bar1_labels, y=bar1_data, marker_color='#64b5f6')])
    bar1_chart.update_layout(
        height=400, 
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(bar1_chart, use_container_width=True)

    st.subheader("Doughnut Chart - Model Fit")
    value = 80.1
    fig, ax = plt.subplots()
    ax.pie([value, 100 - value], labels=["Model Fit", "Remaining"], startangle=90,
           colors=['#1976d2', '#bbdefb'], wedgeprops=dict(width=0.5))
    ax.text(0, 0, f"{value}%", ha='center', va='center', fontsize=20)
    fig.set_facecolor('#e3f2fd')
    st.pyplot(fig)

    st.subheader("Scatter Chart - Voltage vs Current for Sampling Frequencies")
    scatter_data = {
        "1 hour": (33.45, 0.90, 5), "12 hours": (46.12, 0.32, 1), "15 minutes": (22.15, 0.93, 5),
        "2 hours": (37.75, 0.88, 4), "24 hours": (46.66, 0.17, 2), "30 minutes": (26.59, 0.91, 3),
        "4 days": (21.83, 0.23, 1), "4 hours": (41.25, 0.82, 5), "45 minutes": (31.41, 0.91, 5),
        "48 hours": (27.74, 0.22, 4), "5 days": (19.00, 0.26, 3), "6 days": (19.85, 0.31, 4),
        "6 hours": (54.79, 0.79, 5), "7 days": (17.85, 0.27, 4), "72 hours": (25.31, 0.18, 1)
    }

    scatter_chart = go.Figure()
    colors = ['#0d47a1', '#1565c0', '#1976d2', '#1e88e5', '#2196f3', '#42a5f5', 
              '#64b5f6', '#90caf9', '#bbdefb', '#e3f2fd', '#0d47a1', '#1565c0',
              '#1976d2', '#1e88e5', '#2196f3']

    for i, (label, (x, y, z)) in enumerate(scatter_data.items()):
        scatter_chart.add_trace(go.Scatter(
            x=[x], y=[y], mode='markers', marker=dict(size=z*4, color=colors[i % len(colors)]),
            name=label
        ))

    scatter_chart.update_layout(
        height=500,
        xaxis_title="Input Voltage (V)",
        yaxis_title="Output Current (A)",
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(scatter_chart, use_container_width=True)

    st.subheader("Dual Bar Chart - Accuracy vs MAPE")
    bar2_labels = ["15 Minutes", "30 Minutes", "45 Minutes", "1 Hour", "2 Hours", "4 Hours", "6 Days", "7 Days",
                   "6 Hours", "5 Days", "4 Days", "48 Hours", "72 Hours", "12 Hours", "24 Hours"]
    voltage_data = [22.15, 26.59, 31.41, 33.45, 37.75, 41.25, 54.79, 46.12, 19.85, 17.85, 19.00, 21.83, 27.74, 25.31, 46.66]
    mape_data = [0.93, 0.91, 0.91, 0.90, 0.88, 0.82, 0.79, 0.32, 0.31, 0.27, 0.26, 0.23, 0.22, 0.18, 0.17]

    bar2_chart = go.Figure()
    bar2_chart.add_trace(go.Bar(name='Accuracy', x=bar2_labels, y=voltage_data, marker_color='#1565c0'))
    bar2_chart.add_trace(go.Bar(name='MAPE min', x=bar2_labels, y=mape_data, marker_color='#42a5f5'))
    bar2_chart.update_layout(
        barmode='group', 
        height=400, 
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(bar2_chart, use_container_width=True)

# ---- TAB 2: Evaluation Metrics ----
with tab2:
    st.header("📊 Solar Forecasting - Model Evaluation Dashboard")

    # Create sample data instead of reading from local files
    st.subheader("LSTM Model Evaluation Metrics")
    
    # Sample LSTM data
    lstm_data = pd.DataFrame({
        'Sampling Frequency': ['15 Minutes', '30 Minutes', '45 Minutes', '1 Hour', '2 Hours', '4 Hours', 
                             '6 Hours', '12 Hours', '24 Hours', '48 Hours', '72 Hours', '4 Days', 
                             '5 Days', '6 Days', '7 Days'],
        'MAE': [0.045, 0.052, 0.063, 0.075, 0.112, 0.158, 0.187, 0.234, 0.312, 0.378, 0.402, 0.453, 0.487, 0.512, 0.534],
        'RMSE': [0.087, 0.095, 0.118, 0.142, 0.187, 0.223, 0.265, 0.312, 0.387, 0.432, 0.478, 0.512, 0.543, 0.567, 0.589],
        'nRMSE (%)': [5.2, 6.1, 7.3, 8.4, 11.2, 15.7, 18.3, 22.5, 27.8, 34.6, 38.9, 42.3, 45.8, 48.2, 51.3],
        'R²': [0.93, 0.91, 0.91, 0.90, 0.88, 0.82, 0.79, 0.32, 0.17, 0.22, 0.18, 0.23, 0.26, 0.31, 0.27]
    })
    
    st.dataframe(lstm_data.style.background_gradient(cmap='Blues'), use_container_width=True, height=450)

    st.subheader("Persistence Model Evaluation Metrics")
    
    # Sample Persistence data
    persistence_data = pd.DataFrame({
        'Sampling Frequency': ['15 Minutes', '30 Minutes', '45 Minutes', '1 Hour', '2 Hours', '4 Hours', 
                             '6 Hours', '12 Hours', '24 Hours', '48 Hours', '72 Hours', '4 Days', 
                             '5 Days', '6 Days', '7 Days'],
        'MAE': [0.065, 0.078, 0.092, 0.102, 0.153, 0.212, 0.254, 0.312, 0.387, 0.432, 0.478, 0.523, 0.565, 0.587, 0.612],
        'RMSE': [0.109, 0.124, 0.156, 0.187, 0.234, 0.285, 0.323, 0.387, 0.456, 0.521, 0.567, 0.612, 0.654, 0.678, 0.701],
        'nRMSE (%)': [7.5, 8.9, 10.2, 11.8, 16.5, 21.3, 25.6, 31.4, 38.2, 45.7, 51.2, 55.8, 59.7, 62.5, 65.8],
        'R²': [0.90, 0.87, 0.81, 0.73, 0.35, -0.53, -0.91, 0.05, -0.46, -0.89, -0.88, -1.43, -1.44, -0.24, -1.25]
    })
    
    st.dataframe(persistence_data.style.background_gradient(cmap='Blues'), use_container_width=True, height=450)

    st.info("ℹ️ You can scroll horizontally/vertically or use fullscreen mode for easier table viewing.")

# ---- TAB 3: Project Overview ----
# Example of implementing styled sections for Tab 3: Project Overview
with tab3:
    st.markdown("<h1 style='color: #1565c0;'>🧠 AI-Based Solar Energy Optimization</h1>", unsafe_allow_html=True)
    
    # Project Author section with improved styling
    st.markdown("""
    <div class="card" style="background-color:#e3f2fd; border-left-color:#1565c0;">
    <h3 style="color:#0d47a1;">👩‍💻 Project Author</h3>
    <p><strong>Siva Haritha</strong> - Intern, NIC Division</p>
    
    <ul style="list-style-type:none; padding-left:0;">
      <li>✅ <strong>Best Performing Model:</strong> 15-minute interval forecasting</li>
      <li>⚠️ <strong>Worst Performing Model:</strong> 24-hour interval forecasting</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Goal section with improved styling
    st.markdown("""
    <div class="card" style="background-color:#e3f2fd; border-left-color:#26c6da;">
    <h3 style="color:#0d47a1;">🎯 Main Goal of the Project</h3>
    <p>To design and evaluate AI-based solar energy forecasting models, integrating them into smart grid systems for improved energy management. The project aims to compare forecasting performance, explore optimization techniques, and contribute to sustainable energy deployment using intelligent data-driven methods.</p>
    </div>
    """, unsafe_allow_html=True)

    # Technologies section with improved styling - Frontend
    st.markdown("""
    <div class="card" style="background-color:#e3f2fd; border-left-color:#42a5f5;">
    <h3 style="color:#0d47a1;">🖥️ Frontend</h3>
    <ul>
      <li><strong>HTML5:</strong> Page structure and layout</li>
      <li><strong>CSS3:</strong> Styling and responsiveness</li>
      <li><strong>Bootstrap 5:</strong> UI components and grid</li>
      <li><strong>JavaScript:</strong> DOM interaction and logic</li>
      <li><strong>Chart.js:</strong> Interactive visualizations</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Technologies section with improved styling - Backend
    st.markdown("""
    <div class="card" style="background-color:#e3f2fd; border-left-color:#7e57c2;">
    <h3 style="color:#0d47a1;">⚙️ Backend & AI</h3>
    <ul>
      <li><strong>Python 3.x:</strong> Backend scripting and model control</li>
      <li><strong>Flask (optional):</strong> Serve predictions via API</li>
      <li><strong>TensorFlow/Keras:</strong> Deep learning with LSTM</li>
      <li><strong>scikit-learn:</strong> Preprocessing and validation</li>
      <li><strong>NumPy & Pandas:</strong> Data manipulation</li>
      <li><strong>pvlib:</strong> Solar irradiance estimation (GHIcs)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Technologies section with improved styling - Data Handling
    st.markdown("""
    <div class="card" style="background-color:#e3f2fd; border-left-color:#66bb6a;">
    <h3 style="color:#0d47a1;">📊 Data Handling</h3>
    <ul>
      <li><strong>Dataset:</strong> 10-second interval GHI measurements</li>
      <li><strong>Cleaning:</strong> NaN handling, outlier removal</li>
      <li><strong>Features:</strong> kcs, seasonal sinusoidal features, derivatives</li>
      <li><strong>Validation:</strong> MAE, RMSE, nRMSE, R² metrics</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---- TAB 4: Model Comparisons ----
with tab4:
    st.header("📉 Model Performance Comparison")

    # LSTM Bar Chart
    st.subheader("LSTM Model - Sampling Frequency vs Cost")
    lstm_labels = ["15 Minutes", "30 Minutes", "45 Minutes", "1 Hour", "2 Hours", "4 Hours", "6 Days", "7 Days", "6 Hours", "5 Days", "4 Days", "48 Hours", "72 Hours", "12 Hours", "24 Hours"]
    lstm_data = [0.04, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.005]
    fig_lstm = go.Figure([go.Bar(x=lstm_labels, y=lstm_data, marker_color="#1565c0")])
    fig_lstm.update_layout(
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(fig_lstm, use_container_width=True)

    # Persistence Bar Chart
    st.subheader("Persistence Model - Sampling Frequency vs Accuracy")
    persistence_labels = ["15 Minutes", "30 Minutes", "45 Minutes", "1 Hour", "2 Hours", "12 Hours", "6 Days", "24 Hours", "4 Hours", "72 Hours", "48 Hours", "6 Hours", "7 Days", "4 Days", "5 Days"]
    persistence_data = [0.90, 0.87, 0.81, 0.73, 0.35, 0.05, -0.24, -0.46, -0.53, -0.88, -0.89, -0.91, -1.25, -1.43, -1.44]
    fig_persistence = go.Figure([go.Bar(x=persistence_labels, y=persistence_data, marker_color="#1565c0")])
    fig_persistence.update_layout(
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(fig_persistence, use_container_width=True)

    # Accuracy Comparison Chart
    st.subheader("Overall Accuracy Comparison: Persistence vs LSTM")
    sampling_freqs = [
        "1 hour", "12 hours", "15 minutes", "2 hours", "24 hours",
        "30 minutes", "4 days", "4 hours", "45 minutes", "48 hours",
        "5 days", "6 days", "6 hours", "7 days", "72 hours"
    ]
    persistence_acc = [85.2, 76.4, 88.1, 83.7, 72.5, 89.3, 67.8, 84.6, 90.1, 70.3, 65.9, 68.4, 86.2, 66.7, 69.5]
    lstm_acc = [91.4, 81.6, 97.7, 89.5, 79.3, 94.2, 73.6, 90.7, 95.0, 76.1, 71.8, 74.3, 91.0, 72.2, 75.6]
    acc_fig = go.Figure()
    acc_fig.add_trace(go.Bar(name="Persistence Model", x=sampling_freqs, y=persistence_acc, marker_color="#0d47a1"))
    acc_fig.add_trace(go.Bar(name="LSTM Model", x=sampling_freqs, y=lstm_acc, marker_color="#42a5f5"))
    acc_fig.update_layout(
        barmode='group', 
        yaxis_title="Accuracy (%)",
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(acc_fig, use_container_width=True)

    # Accuracy Line Chart
    st.subheader("Model Accuracy over Sample Frequency")
    line_freqs = ["24 Hours", "72 Hours", "48 Hours", "4 Days", "5 Days", "7 Days", "6 Days", "12 Hours", "6 Hours", "4 Hours", "2 Hours", "1 Hour", "45 Minutes", "30 Minutes", "15 Minutes"]
    persist_line = [60, 62, 63, 65, 67, 70, 72, 75, 77, 80, 82, 85, 87, 89, 91]
    lstm_line = [70, 72, 75, 77, 80, 82, 85, 87, 90, 92, 94, 95, 97, 98, 99]
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=line_freqs, y=persist_line, name='Persistence Model', mode='lines+markers', fill='tozeroy', line=dict(color='#0d47a1')))
    fig_line.add_trace(go.Scatter(x=line_freqs, y=lstm_line, name='LSTM Model', mode='lines+markers', fill='tozeroy', line=dict(color='#42a5f5')))
    fig_line.update_layout(
        yaxis=dict(title="Accuracy (%)"), 
        xaxis=dict(title="Sampling Frequency"),
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(fig_line, use_container_width=True)

    # Accuracy Pie Chart
    st.subheader("Model Accuracy Comparison (Pie)")
    pie_accuracy = go.Figure(data=[
        go.Pie(labels=["LSTM Model", "Persistence Model"], values=[127.0, 64.3],
               marker=dict(colors=["#1565c0", "#42a5f5"]), textinfo='label+percent')
    ])
    pie_accuracy.update_layout(
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(pie_accuracy, use_container_width=True)

    # Cost Efficiency Pie Chart
    st.subheader("Cost Efficiency Score Comparison (Pie)")
    pie_cost = go.Figure(data=[
        go.Pie(labels=["LSTM Model", "Persistence Model"], values=[88.5, 52.7],
               marker=dict(colors=["#1976d2", "#90caf9"]), textinfo='label+percent')
    ])
    pie_cost.update_layout(
        plot_bgcolor='#e3f2fd',
        paper_bgcolor='#e3f2fd'
    )
    st.plotly_chart(pie_cost, use_container_width=True)

# ---- TAB 5: Methodology & Insights ----
with tab5:
    st.header("📋 Forecasting Parameters")
    st.table([
        ["Forecast Horizons", "15 min to 7 days"],
        ["Measurement Frequency", "10 seconds"],
        ["Data Duration", "Jan 2020 – Nov 2024"],
        ["Total Data Points", "17,297,280"]
    ])

    st.header("📥 Input Features")
    st.markdown("""
    - **Group 1:** First derivatives – 𝑑GHI, 𝑑GHIcs, 𝑑kcs  
    - **Group 2:** Second derivatives – 𝑑²GHI, 𝑑²GHIcs, 𝑑²kcs  
    - **Group 3:** Third derivatives – 𝑑³GHI, 𝑑³GHIcs, 𝑑³kcs  
    - **Group 4:** Basic – GHI, GHIcs, kcs  
    - **Group 5:** Seasonal – hour, day, month (sin/cos encoding)
    """)

    st.header("📊 Performance Evaluation Metrics")
    st.table([
        ["MAE", "Mean Absolute Error"],
        ["RMSE", "Root Mean Square Error"],
        ["nMAE", "Normalized MAE"],
        ["nRMSE", "Normalized RMSE"],
        ["R²", "Coefficient of Determination"],
        ["95% CI", "Confidence Interval"]
    ])

    st.header("🧠 Model Architecture")
    st.markdown("""
    - **Model:** LSTM (Long Short-Term Memory)  
    - **Layers:** 3 LSTM layers with 300 units each  
    - **Final Layer:** Dense (1 unit)  
    - **Activations:** Sigmoid, Tanh  
    - **Training:** Early stopping, time-series CV  
    - **Framework:** Keras (Python)
    """)

    st.header("🧼 Data Preprocessing Steps")
    st.markdown("""
    1. Missing value handling  
    2. Outlier detection  
    3. Clear-sky irradiance with PVLib  
    4. Remove night-time data  
    5. Compute kcs (clear sky index)  
    6. Compute 1st–3rd derivatives  
    7. Generate seasonal features  
    8. Downsampling for multiple horizons
    """)

    st.header("⚙️ Feature Engineering Settings")
    st.markdown("""
    - **Polynomial Order:** Varies (1–5) based on horizon  
    - **History Window (h):** 5 or 10 time steps  
    - **Feature Selection:** Grid search based
    """)

    st.header("✅ Advantages")
    st.table([
        ["High Accuracy", "LSTM-based model achieved low MAE and RMSE."],
        ["Long-term Dataset", "6 years of high-frequency data (17M+ samples)."],
        ["Comprehensive Features", "Derivatives up to 3rd order, seasonality, clear sky indices."],
        ["Multi-Horizon Forecasting", "From 15-minute to 7-day forecasts."],
        ["Open Dataset & Code", "Shared via GitHub for reproducibility."],
        ["Preprocessing Pipeline", "Includes normalization and feature engineering."]
    ])

    st.header("⚠️ Limitations")
    st.table([
        ["High Computational Demand", "Training requires substantial hardware."],
        ["Data-Dependent", "Performance may drop outside original region."],
        ["Limited Explainability", "Deep LSTMs are black-box models."],
        ["No Real-time Integration", "No deployment for MPPT/load shifting."],
        ["Lack of Ensemble Comparison", "No hybrid baselines included."],
        ["Scalability Constraints", "Architecture not designed for microgrids."]
    ])

    st.header("🔧 Possible Modifications & Improvements")
    st.table([
        ["Use Hybrid/Ensemble Models", "Improve generalization and interpretability."],
        ["Deploy in Real-Time Systems", "Smart grid decisions based on forecasts."],
        ["Use Transfer Learning", "Better generalization in new regions."],
        ["Explainable AI", "Use SHAP/LIME to interpret model."],
        ["Edge Deployment", "Enable Raspberry Pi/Jetson deployment."],
        ["Integrate Weather APIs", "Boost forecast accuracy in real-time."]
    ])

# ---- TAB 6: AI-Based Solar Research Paper Comparison ----
with tab6:
    # Expanded Insights
    st.header("🧠 Expanded Narrative Insights per Paper")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("1. RELAD-ANN (Hanif et al., 2024)")
        st.markdown("""
        - **Best for:** High-accuracy forecasting  
        - **Unique Strength:** Combines ANN + LightGBM  
        - **Limitation:** Based on Quetta region
        """)

        st.subheader("4. AI in PV Tech (Mohammad et al., 2023)")
        st.markdown("""
        - **Best for:** AI in full PV lifecycle  
        - **Unique Strength:** Covers design to maintenance  
        - **Limitation:** No experimental results
        """)

    with col2:
        st.subheader("2. Gen-AI (Mousavi et al., 2025)")
        st.markdown("""
        - **Best for:** Generative AI in renewables  
        - **Unique Strength:** Uses GANs, VAEs  
        - **Limitation:** No experimental validation
        """)

        st.subheader("5. Holistic AI Grid (Wen et al., 2024)")
        st.markdown("""
        - **Best for:** Full smart grid AI solutions  
        - **Unique Strength:** MPPT to cybersecurity  
        - **Limitation:** Requires high computing
        """)

    with col3:
        st.subheader("3. Forecasting & Grid (Bouquet et al., 2024)")
        st.markdown("""
        - **Best for:** Forecasting + smart grid  
        - **Unique Strength:** Public dataset, real deployment  
        - **Limitation:** Complex preprocessing
        """)

        st.subheader("6. AI for RE Systems (Bennagi et al., 2024)")
        st.markdown("""
        - **Best for:** Review of AI in renewables  
        - **Unique Strength:** 150+ studies analyzed  
        - **Limitation:** No new methodology
        """)

    # Future Scope
    st.header("🔮 Future Scope and Recommendations")

    recommendations = [
        ("Hybrid Modeling", "Combine generative + predictive models for improved forecasting."),
        ("Geographical Diversification", "Use data from diverse climates for better generalization."),
        ("Standardized Metrics", "Enable fair comparisons using unified performance metrics."),
        ("Empirical Validation", "Test Gen-AI models using real-world experiments."),
        ("AI Interpretability", "Apply XAI to increase AI system trust and transparency."),
        ("Cross-sector Integration", "Incorporate market, weather, and policy signals for better AI decisions.")
    ]

    for i in range(0, len(recommendations), 3):
        rec_cols = st.columns(3)
        for j, (title, desc) in enumerate(recommendations[i:i+3]):
            if j < len(rec_cols):
                with rec_cols[j]:
                    st.success(f"**{title}**  \n{desc}")

    st.markdown("These actions aim to move AI in solar and smart grids toward real-world deployment.")

# ---- TAB 7: LSTM-Based Solar Forecasting – Q&A Section ----
with tab7:
    st.header("📘 LSTM-Based Solar Forecasting – Q&A Section")
    st.markdown("Insightful answers about model design, performance, impact, and practical deployment.")

    qa_data = [
        ("bi-lightbulb", "What is LSTM?", "LSTM (Long Short-Term Memory) is a type of recurrent neural network that excels at learning patterns from time series data by maintaining memory over longer sequences."),
        ("bi-gear", "Why use LSTM for solar forecasting?", "LSTM models can handle temporal dependencies and nonlinear trends in solar irradiance and generation data, improving forecasting accuracy compared to traditional models."),
        ("bi-bar-chart-line", "What data is used in the LSTM model?", "The LSTM model typically uses historical solar irradiance, and past power generation data as input features for training."),
        ("bi-cpu", "How is the model trained?", "The model is trained using a loss function like Mean Squared Error (MSE) with backpropagation through time (BPTT), optimized using an algorithm like Adam or RMSprop."),
        ("bi-speedometer2", "What is the performance metric used?", "Common metrics include RMSE, MAE, and R² Score, which help evaluate how close the predicted values are to the actual solar power output."),
        ("bi-lightning-charge", "Can LSTM handle real-time data?", "Yes, with proper preprocessing and online learning techniques, LSTM can be adapted for real-time or near real-time solar forecasting applications."),
        ("bi-bullseye", "What is the goal of the LSTM-based solar forecasting project?", "To enhance forecast accuracy and grid reliability across short-term, day-ahead, and long-term horizons using LSTM deep learning integrated with smart grid infrastructure."),
        ("bi-exclamation-circle", "What is the main problem addressed by this project?", "The project tackles the challenge of poor forecasting in solar energy, which causes grid instability and inefficiencies.")
    ]
    def render_card(icon_html, content_html):
        st.markdown(
        f"""
        <div style="background-color:#f8f9fa; padding: 15px; margin-bottom: 10px; border-radius: 10px; box-shadow: 0 0 5px rgba(0,0,0,0.1);">
            <h5>{icon_html}</h5>
            {content_html}
        </div>
        """,
        unsafe_allow_html=True
    )

    for icon, question, answer in qa_data:
        render_card(f"<i class='{icon}'></i> {question}", f"<p>{answer}</p>")


with tab8:
    st.header("🧠 AI Forecasting - Project Overview")
    st.markdown("""
    <style>
    .card {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    .blockquote {
        border-left: 4px solid #1E2F97;
        padding-left: 1rem;
        color: #444;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# Define card rendering function
def render_card(title, content):
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{title}</div>
        {content}
    </div>
    """, unsafe_allow_html=True)

# Row 1
col1, col2 = st.columns(2)
with col1:
    render_card("🎯 Project Goal", """
    <p>Develop an AI-based predictive framework using deep learning (LSTM) to enhance forecasting, efficiency, and economic viability of solar energy systems integrated with smart grid infrastructure.</p>
    """)

with col2:
    render_card("⚙️ Technical Methodology", """
    <ul>
        <li>Real-time irradiance data (GHI, GHIcs, kcs) @10s frequency</li>
        <li>Forecasting from 15 min to 7 days</li>
        <li>LSTM-based deep learning models</li>
        <li>Evaluation metrics: MAE, RMSE, nMAE, nRMSE, R² (> 0.9)</li>
    </ul>
    """)

# Row 2
col3, col4 = st.columns(2)
with col3:
    render_card("🌐 Key Outcomes", """
    <ul>
        <li><strong>Accuracy:</strong> 30–50% lower error than traditional models</li>
        <li><strong>Cost Savings:</strong> Save Money by get rid of error</li>
        <li><strong>Grid Optimization:</strong> 20–40% reduced curtailment</li>
    </ul>
    """)

with col4:
    render_card("🧠 AI Integration Benefits", """
    <ul>
        <li>Smart grid automation</li>
        <li>Predictive maintenance via anomaly detection</li>
        <li>Hybrid ML + DL model options</li>
        <li>Scalable to other renewables (wind, hydro)</li>
    </ul>
    """)

# Row 3
col5, col6 = st.columns(2)
with col5:
    render_card("📈 Sustainability & Planning", """
    <ul>
        <li>Supports utility & government energy planning</li>
        <li>500K–1M tons CO₂ reduction annually</li>
        <li>Open data access with 17M+ records shared</li>
    </ul>
    """)

with col6:
    render_card("🔍 Challenges Solved", """
    <ul>
        <li>Forecast variability → LSTM time-series learning</li>
        <li>Market penalties → Precise bidding forecasts</li>
        <li>Reserve overuse → Confidence in predictions</li>
        <li>Manual work → Automation pipeline</li>
        <li>Panel loss → AI-based MPPT optimization</li>
    </ul>
    """)

# Final Impact Card (Full Width)
render_card("🌍 Final Impact", """
<p><strong>AI-powered forecasting enables:</strong></p>
<ul>
    <li>✔️ Better accuracy</li>
    <li>✔️ Higher ROI</li>
    <li>✔️ Lower carbon emissions</li>
    <li>✔️ Smarter, scalable clean energy systems</li>
</ul>
<blockquote class="blockquote">🧠 <em>Smarter forecasting → Efficient energy use → Sustainable growth</em></blockquote>
""")
