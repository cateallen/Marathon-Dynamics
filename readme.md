### Marathon Dynamics
A data visualization project analyzing marathon race data from around the world, focusing on performance trends, environmental factors, and runner demographics.

### Project Overview
This project visualizes marathon race data from different events worldwide, uncovering insights into race times, weather conditions, course elevation, and runner demographics. By leveraging global marathon data, we aim to understand how different factors impact race performance, showcasing trends and dynamics unique to each marathon.

### Key visualizations include:

Race Performance vs. Elevation: How course difficulty affects marathon times.
Weather Effects on Race Times: Heatmaps of performance under various weather conditions.
Global Performance Comparison: Race times across countries and regions.
Pacing Strategies: Visualize split times and pacing of elite runners.

### Table of Contents
- Installation
- Usage
- Data Sources
- Features
- Contributing
- License


### Installation
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x
pip (Python package installer)

## Steps
1. Clone the repository
git clone https://github.com/cateallen/Marathon-Dynamics.git
cd Marathon-Dynamics
2. Set up the virtual environmental
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run the project: You can now run the scripts in the src/ folder to generate visualizations.

### Usage
Once the project is set up, you can explore the marathon stats:

## For instance: Visualizing Performance vs. Elevation
1. Ensure your marathon dataset (e.g., marathon-race-data.csv) is in the data/ folder.
2. Run the visualization script
python src/visualization.py
3. This will generate visualizations showing the relationship between marathon finish times and course elevation.

## Customizing with Your Own Data
To visualize your own marathon data:
1. Place your dataset in the data/ folder.
2. Modify the script in src/visualization.py to load your file. Ensure your dataset has columns like Race, Country, FinishTime, ElevationChange, Temperature, etc.


### Data Sources
I used marathon data collected from various global sources. Here are some useful datasets to get started:

- World Athletics: Official records of elite marathon events.
- OpenRace: Public race result data.
- Strava: Running activity tracking platform.
- Feel free to add your own datasets from official marathon websites or APIs.

### Features
- Visualize Marathon Trends: Gain insights into how race performance correlates with environmental factors like elevation and weather.
- Global Comparison: See how marathon race times compare across countries and regions.
- Interactive Dashboards (Planned): Build interactive visualizations for deeper exploration of trends.
- Pacing Analysis (Planned): Visualize the pacing strategies of top marathoners, using split data.


### Contributing

Please feel free to make contributions! Here’s how you can do so:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request, and we’ll review your changes.
6. Feel free to contribute new datasets, improvements to visualizations, or new features!


### License
This project is licensed under the MIT License - see the LICENSE file for details.