# planned_giving_calculator.py

import streamlit as st

def main():
    st.title("Planned Giving Calculator")
    st.write("""
    This calculator helps you understand the financial benefits of planned giving options with the Foundation for Appalachian Ohio.
    """)

    # Input Section
    st.header("Donor Information")
    donation_amount = st.number_input("Donation Amount ($)", min_value=1000, value=10000, step=1000)
    donor_age = st.number_input("Donor's Age", min_value=18, value=50, step=1)
    tax_rate = st.slider("Marginal Tax Rate (%)", min_value=0, max_value=50, value=30, step=1)

    st.header("Planned Giving Options")
    option = st.selectbox("Select a Planned Giving Option", [
        "Charitable Bequest",
        "Charitable Gift Annuity",
        "Charitable Remainder Trust",
        "Donor-Advised Fund"
    ])

    st.header("Areas of Impact")
    fao_pillars = [
        "Arts & Culture",
        "Community & Economic Development",
        "Education",
        "Environmental Stewardship",
        "Health & Human Services"
    ]
    selected_pillar = st.selectbox("Select an FAO Pillar to Support", fao_pillars)

    # Calculation and Output
    if st.button("Calculate Benefits"):
        if option == "Charitable Bequest":
            calculate_bequest(donation_amount, tax_rate, selected_pillar)
        elif option == "Charitable Gift Annuity":
            calculate_gift_annuity(donation_amount, donor_age, tax_rate, selected_pillar)
        elif option == "Charitable Remainder Trust":
            calculate_remainder_trust(donation_amount, donor_age, tax_rate, selected_pillar)
        elif option == "Donor-Advised Fund":
            calculate_donor_advised_fund(donation_amount, tax_rate, selected_pillar)

def calculate_bequest(donation_amount, tax_rate, selected_pillar):
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Bequest Results")
    st.write(f"Estimated Estate Tax Savings: **${tax_savings:,.2f}**")
    st.write("Your bequest will leave a lasting legacy without affecting your current financial situation.")
    display_impact_story(selected_pillar)

def calculate_gift_annuity(donation_amount, donor_age, tax_rate, selected_pillar):
    annuity_rate = get_annuity_rate(donor_age)
    annual_income = donation_amount * annuity_rate
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Gift Annuity Results")
    st.write(f"Annual Income: **${annual_income:,.2f}**")
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("Receive guaranteed income for life while supporting a worthy cause.")
    display_impact_story(selected_pillar)

def calculate_remainder_trust(donation_amount, donor_age, tax_rate, selected_pillar):
    annual_payout_rate = 0.05  # Assuming a 5% payout rate
    annual_income = donation_amount * annual_payout_rate
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Remainder Trust Results")
    st.write(f"Annual Income: **${annual_income:,.2f}**")
    st.write(f"Immediate Tax​⬤
