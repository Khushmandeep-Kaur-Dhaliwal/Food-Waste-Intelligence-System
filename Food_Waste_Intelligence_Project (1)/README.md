# Food Waste Intelligence System

A beginner-friendly BCA Data Science project that explores product-level food loss and waste records by country, food group and supply-chain stage.

## Features
- Public dataset download from Zenodo
- Data cleaning and preprocessing
- Exploratory data analysis
- Unit-aware comparisons
- Interactive Plotly charts
- Streamlit web dashboard
- Search, filters and CSV export
- Data-driven observations and limitations

## Dataset
WASTEWISE, *Database of product-level food loss and waste per supply chain stage*, Zenodo (2025).
- Record: https://zenodo.org/records/17588514
- DOI: https://doi.org/10.5281/zenodo.17588514
- The source readme reports 484 records and 29 variables, with European geographic coverage.
- Licence stated in the readme: CC BY-NC-SA.

Please provide attribution to the dataset creators, do not use the dataset commercially, and follow the share-alike terms. Check the Zenodo record for the latest licence and version details before submission or redistribution.

## Run in Google Colab
1. Upload and open `Food_Waste_Intelligence.ipynb` in Google Colab.
2. Run the notebook cells from top to bottom.
3. It downloads the public Excel dataset, cleans it, creates charts and exports `data/food_waste_clean.csv`.
4. Download the generated project folder or CSV and place it in this repository's `data/` folder.

## Run the dashboard locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Ensure `data/food_waste_clean.csv` exists before launching the dashboard.

## Important limitations
- The source combines measurements from different studies, time periods and methods.
- Quantities with different units must not be added together. The app filters to one unit before showing totals.
- The data has European scope and should not be described as actual measurements from a local Indian restaurant or college canteen.
- This project is an educational exploratory analytics tool, not a certified waste audit or a live monitoring system.

## Suggested team roles
1. Dataset research, downloading and cleaning.
2. Exploratory analysis and statistical summaries.
3. Dashboard layout, filters and charts.
4. Integration, testing, documentation and presentation.

## Suggested GitHub repository description
Food Waste Intelligence System – a Python Data Science project that analyses public food-loss and food-waste records using Pandas, Plotly and Streamlit.
