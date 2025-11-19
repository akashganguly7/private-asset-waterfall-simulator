import streamlit as st
import pandas as pd
from waterfall import return_capital, preferred_return, gp_catch_up, final_split, irr
import plotly.graph_objects as go

st.title("💧 Private Equity Waterfall Simulator")

st.sidebar.header("Input Parameters")
#add a legend of LP: Limited Partner and GP: General Partner to the sidebar
st.sidebar.markdown("LP: Limited Partner | GP: General Partner")
capital = st.sidebar.number_input("LP Capital Invested (€)", value=5000)
exit_value = st.sidebar.number_input("Exit Value (€)", value=10000)
years = st.sidebar.number_input("Years Invested", value=5)
hurdle = st.sidebar.slider("Preferred Return (Hurdle %)", 0.0, 0.20, 0.08)
carry = st.sidebar.slider("GP Carry %", 0.0, 0.40, 0.20)

if st.sidebar.button("Calculate Waterfall"):
    
    st.subheader("Waterfall Breakdown")
    
    total_profit = exit_value - capital

    # Step 1
    lp_capital_return, remaining = return_capital(capital, exit_value)

    # Step 2
    lp_pref, remaining = preferred_return(capital, years, hurdle, remaining)

    # Step 3
    gp_cu, remaining = gp_catch_up(capital, total_profit, carry, remaining, lp_pref, lp_capital_return)

    # Step 4
    lp_split, gp_split = final_split(remaining)

    results = {
        "Stage": ["LP Capital Return", "LP Preferred Return", "GP Catch-Up", "Final LP Split", "Final GP Split"],
        "LP (€)": [lp_capital_return, lp_pref, 0, lp_split, 0],
        "GP (€)": [0, 0, gp_cu, 0, gp_split]
    }

    df = pd.DataFrame(results)
    st.table(df)

    # Total amounts
    st.write("### Totals")
    st.write(f"**LP Total:** €{lp_capital_return + lp_pref + lp_split:.2f}")
    st.write(f"**GP Total:** €{gp_cu + gp_split:.2f}")


    fig = go.Figure(go.Waterfall(
        name="Waterfall",
        orientation="v",
        measure=["absolute", "relative", "relative", "relative", "relative"],
        x=["Capital Return", "Preferred Return", "Catch-Up", "LP Split", "GP Split"],
        y=[lp_capital_return, lp_pref, gp_cu, lp_split, gp_split]
    ))

    st.plotly_chart(fig)
