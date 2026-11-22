import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Food Waste Intelligence", page_icon="♻️", layout="wide")

st.title("♻️ Food Waste Intelligence System")
st.caption("Explore product-level food loss and waste records by country, product and supply-chain stage.")

DATA_PATH = Path(__file__).parent / "data" / "food_waste_clean.csv"
if not DATA_PATH.exists():
    st.error("Dataset not found. Run the Google Colab notebook and place data/food_waste_clean.csv in this project's data folder.")
    st.stop()

df = pd.read_csv(DATA_PATH)
required = {"country", "product", "supply_chain_stage", "quantity", "unit", "food_group", "edible_fraction"}
missing = required - set(df.columns)
if missing:
    st.error(f"Dataset is missing required columns: {', '.join(sorted(missing))}")
    st.stop()

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df = df.dropna(subset=["quantity"])
df = df[df["quantity"] >= 0]

st.sidebar.header("Filters")
units = sorted(df["unit"].dropna().astype(str).unique())
selected_unit = st.sidebar.selectbox("Measurement unit", units)
view = df[df["unit"].astype(str) == selected_unit].copy()

def multi_filter(label, column):
    values = sorted(view[column].dropna().astype(str).unique())
    chosen = st.sidebar.multiselect(label, values, default=values)
    if chosen:
        return chosen
    return values

countries = multi_filter("Country", "country")
groups = multi_filter("Food group", "food_group")
stages = multi_filter("Supply-chain stage", "supply_chain_stage")

view = view[
    view["country"].astype(str).isin(countries) &
    view["food_group"].astype(str).isin(groups) &
    view["supply_chain_stage"].astype(str).isin(stages)
]

if view.empty:
    st.warning("No records match these filters. Select at least one value in each filter.")
    st.stop()

total = view["quantity"].sum()
average = view["quantity"].mean()
records = len(view)
country_count = view["country"].nunique()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Records in view", f"{records:,}")
c2.metric(f"Sum of reported quantities ({selected_unit})", f"{total:,.2f}")
c3.metric(f"Average per record ({selected_unit})", f"{average:,.2f}")
c4.metric("Countries represented", f"{country_count:,}")

st.info("Only records using the selected measurement unit are combined. The source includes different studies and methods; totals should be interpreted as reported records, not as a complete census.")

left, right = st.columns(2)
with left:
    by_group = view.groupby("food_group", as_index=False)["quantity"].sum().sort_values("quantity", ascending=False).head(15)
    st.plotly_chart(px.bar(by_group, x="food_group", y="quantity", title="Reported quantity by food group"), use_container_width=True)
with right:
    by_stage = view.groupby("supply_chain_stage", as_index=False)["quantity"].sum().sort_values("quantity", ascending=False)
    st.plotly_chart(px.bar(by_stage, x="supply_chain_stage", y="quantity", title="Reported quantity by supply-chain stage"), use_container_width=True)

left, right = st.columns(2)
with left:
    by_country = view.groupby("country", as_index=False)["quantity"].sum().sort_values("quantity", ascending=False).head(15)
    st.plotly_chart(px.bar(by_country, x="country", y="quantity", title="Top countries in the filtered records"), use_container_width=True)
with right:
    edible = view.groupby("edible_fraction", as_index=False)["quantity"].sum()
    st.plotly_chart(px.pie(edible, names="edible_fraction", values="quantity", title="Edible fraction categories"), use_container_width=True)

st.subheader("Explore the records")
search = st.text_input("Search product names")
table = view.copy()
if search:
    table = table[table["product"].astype(str).str.contains(search, case=False, na=False)]
st.dataframe(table, use_container_width=True, hide_index=True)

st.download_button(
    "Download filtered records as CSV",
    data=table.to_csv(index=False).encode("utf-8"),
    file_name="filtered_food_waste_records.csv",
    mime="text/csv"
)

st.subheader("Insights and possible actions")
top_group = view.groupby("food_group")["quantity"].sum().sort_values(ascending=False)
top_stage = view.groupby("supply_chain_stage")["quantity"].sum().sort_values(ascending=False)
if len(top_group):
    st.write(f"• The largest recorded food-group total in this view is **{top_group.index[0]}**.")
if len(top_stage):
    st.write(f"• The largest recorded supply-chain-stage total in this view is **{top_stage.index[0]}**.")
st.write("• Use the product and country filters to identify records that may deserve closer investigation.")
st.write("• For a real business waste audit, collect local measured quantities, dates, preparation volumes and disposal methods. This public research dataset cannot replace those operational records.")

with st.expander("About the dataset and limitations"):
    st.write("Source: WASTEWISE, Database of product-level food loss and waste per supply chain stage, Zenodo (2025).")
    st.write("Geographic scope: Europe. The source readme reports 484 cases and 29 variables.")
    st.write("The dataset combines information from existing studies. Collection methods, time periods and sample descriptions vary. Missing values and different measurement units are possible.")
    st.write("Licence stated in the source readme: CC BY-NC-SA. Provide attribution, do not use the dataset commercially, and follow the share-alike terms.")
    st.markdown("[Open the original dataset on Zenodo](https://zenodo.org/records/17588514)")
