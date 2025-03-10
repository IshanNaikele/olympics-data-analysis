# 🏅 Olympics Data Analysis Web Application

 

## 📊 Overview

This interactive web application provides comprehensive analytics and visualizations for historical Olympic Games data from 1896 to 2016. Using Streamlit's powerful interface, users can explore medal tallies, country performances, athlete statistics, and overall Olympic trends through intuitive dashboards and interactive charts.

## ✨ Features

### 🏆 Medal Tally Analysis
- **Country Rankings**: View and compare medal counts by nation
- **Time Filters**: Analyze performance for specific Olympic years
- **Country Filters**: Focus on individual countries' medal histories
- **Combined Filtering**: Examine specific country performance in particular years

### 📈 Overall Analysis
- **Key Statistics Dashboard**: Quick view of editions, hosts, sports, events, nations, and athletes
- **Participation Trends**: Visualize how Olympic participation has evolved over time
- **Event Growth**: Track the expansion of Olympic events across different games
- **Sport Distribution**: Explore heatmaps showing event distribution by sport over time
- **Athletic Excellence**: Identify the most successful athletes in Olympic history

### 🌍 Country-wise Analysis
- **National Performance**: Track medal counts for specific countries across all Olympics
- **Sport Specialization**: Visualize country strengths through sport-specific medal heatmaps
- **National Heroes**: Discover top-performing athletes from each country

### 🏃 Athlete-wise Analysis
- **Age Analysis**: Statistical distributions of medalist ages
- **Sport-Specific Patterns**: Compare age distributions across different Olympic sports
- **Gender Participation**: Analyze male vs. female participation trends throughout Olympic history

## 🚀 Installation

### Prerequisites
- Python 3.7+
- Required packages:
  - pandas
  - streamlit
  - plotly
  - matplotlib
  - seaborn

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd olympics-data-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare data files**
   - Download the dataset files:
     - `athlete_events.csv` - Main Olympics dataset
     - `noc_regions.csv` - National Olympic Committee region mappings
   - Place them in a folder named `Data` within your project directory

4. **Configure file paths**
   - Open `app.py` in your preferred editor
   - Update the file paths to match your directory structure:
     ```python
     data = pd.read_csv('path/to/your/Data/athlete_events.csv')
     region_data = pd.read_csv('path/to/your/Data/noc_regions.csv')
     ```

## 🖥️ Usage

1. **Launch the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the dashboard**
   - Open your web browser and navigate to `http://localhost:8501`
   - The application will load with the default view

3. **Navigate the interface**
   - Use the sidebar to switch between analysis sections:
     - Medal Tally
     - Overall Analysis
     - Country-wise Analysis
     - Athlete-wise Analysis
   - Apply filters and interact with visualizations in each section

## 📁 Project Structure

```
olympics-data-analysis/
│
├── app.py                  # Main Streamlit application file
├── preprocessor.py         # Data preprocessing and transformation
├── helper.py               # Analysis and visualization functions
├── requirements.txt        # Python dependencies
│
└── Data/                   # Data directory
    ├── athlete_events.csv  # Olympics events and athlete data
    └── noc_regions.csv     # NOC to region mapping
```

## 📊 Data Sources

This application utilizes a comprehensive Olympic Games dataset covering 120 years of Olympic history (1896-2016), including:

- Summer and Winter Olympic Games
- Detailed athlete information (name, age, height, weight)
- Event specifications and results
- Complete medal records

## 🤝 Contributing

Contributions to enhance this application are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

 

Developed with ❤️ by  Ishan Naikele
