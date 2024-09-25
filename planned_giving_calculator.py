# planned_giving_calculator.py

import streamlit as st

def main():
    # Remove the FAO Logo (as per your request)
    # st.image("path_to_logo.png", use_column_width=True)

    # Update the main title
    st.title("Foundation for Appalachian Ohio's Planned Giving Calculator")

    # Embed the introductory YouTube video below the title
    st.video("https://youtu.be/Wv35EUxq2Nc")

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

        # Add the corrected projected community impact section
        projected_community_impact(donation_amount)

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
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("Benefit from income payments and reduce your taxable estate.")
    display_impact_story(selected_pillar)

def calculate_donor_advised_fund(donation_amount, tax_rate, selected_pillar):
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Donor-Advised Fund Results")
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("Recommend grants to charities over time while receiving an immediate tax benefit.")
    display_impact_story(selected_pillar)

def get_annuity_rate(age):
    # Simplified annuity rate table based on age
    if age < 60:
        return 0.04
    elif age < 70:
        return 0.045
    elif age < 80:
        return 0.05
    else:
        return 0.055

def display_impact_story(selected_pillar):
    st.header(f"Impact Story in {selected_pillar}")
    stories = {
        "Arts & Culture": """
        **Bringing Art to Life in Appalachian Ohio**

        *When Emily decided to support the Arts & Culture pillar, she couldn't have imagined the ripple effect her generosity would create. Her donation funded a community theater program that brought together children from diverse backgrounds. Over the course of the program, these young individuals not only discovered their hidden talents but also learned the value of teamwork and self-expression.*

        *The community theater became a beacon of creativity in the region, hosting performances that attracted audiences from neighboring towns. Parents and teachers noticed a positive change in the children's confidence and academic performance. Emily's contribution didn't just support an arts program; it ignited a cultural renaissance that enriched the entire community.*

        *Inspired by the success, local businesses and artists collaborated to establish annual art festivals and workshops. Emily's initial act of kindness had blossomed into a sustained movement, proving that the arts truly have the power to transform lives.*
        """,
        # ... (Other pillars' stories)
    }
    st.write(stories.get(selected_pillar, "Impact story not available for this pillar."))

def projected_community_impact(donation_amount):
    st.header("Projected Community Impact")
    st.write("""
    Assuming 100% of your gift goes into an endowment, an annual return of 5%, and an annual payout of 5% to community projects, here's how your donation could impact the community over time:
    """)

    years_list = [10, 25, 100]
    payout_rate = 0.05  # 5% annual payout to community
    annual_payout = donation_amount * payout_rate

    # Calculate total dollars invested into the community
    data = []
    for years in years_list:
        total_invested = annual_payout * years
        data.append({
            "Years": years,
            "Total Dollars Invested into Community": f"${total_invested:,.2f}",
            "Annual Community Investment": f"${annual_payout:,.2f}",
            "Endowment Principal Remains": f"${donation_amount:,.2f}"
        })

    st.table(data)

if __name__ == "__main__":
    main()
