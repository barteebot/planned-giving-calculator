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

        # Add the projected community impact section with compounding
        projected_community_impact(donation_amount)

def calculate_bequest(donation_amount, tax_rate, selected_pillar):
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Bequest Results")
    st.write(f"Estimated Estate Tax Savings: **${tax_savings:,.2f}**")
    st.write("""
    **How It Works:**
    A charitable bequest is a gift made through your will or trust. It allows you to support causes you care about without affecting your financial situation during your lifetime.

    **Benefits:**
    - **Financial Impact:** Potential estate tax savings, reducing the taxable value of your estate.
    - **Community Impact:** Leaves a lasting legacy by supporting community projects aligned with your values.
    """)
    display_impact_story(selected_pillar)

def calculate_gift_annuity(donation_amount, donor_age, tax_rate, selected_pillar):
    annuity_rate = get_annuity_rate(donor_age)
    annual_income = donation_amount * annuity_rate
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Gift Annuity Results")
    st.write(f"Annual Income: **${annual_income:,.2f}**")
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("""
    **How It Works:**
    A charitable gift annuity is a contract where you make a donation and, in return, receive a fixed annual income for life.

    **Benefits:**
    - **Financial Impact:** Provides a reliable income stream and immediate tax deductions.
    - **Community Impact:** After your lifetime, the remaining funds support community projects.
    """)
    display_impact_story(selected_pillar)

def calculate_remainder_trust(donation_amount, donor_age, tax_rate, selected_pillar):
    annual_payout_rate = 0.04  # 4% payout rate
    annual_income = donation_amount * annual_payout_rate
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Remainder Trust Results")
    st.write(f"Annual Income: **${annual_income:,.2f}**")
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("""
    **How It Works:**
    A charitable remainder trust provides you or your beneficiaries with income for life or a term of years, after which the remaining assets go to charity.

    **Benefits:**
    - **Financial Impact:** Potential income stream, immediate tax benefits, and reduction of taxable estate.
    - **Community Impact:** Significant future gift to support community projects.
    """)
    display_impact_story(selected_pillar)

def calculate_donor_advised_fund(donation_amount, tax_rate, selected_pillar):
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Donor-Advised Fund Results")
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("""
    **How It Works:**
    A donor-advised fund allows you to make a charitable contribution, receive an immediate tax deduction, and recommend grants from the fund over time.

    **Benefits:**
    - **Financial Impact:** Immediate tax deductions and flexibility in charitable giving.
    - **Community Impact:** Ongoing support for community projects you care about.
    """)
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
    # Embed the video in the impact stories section
    st.video("https://www.youtube.com/watch?v=x5bKXFXBj_4")
    stories = {
        "Arts & Culture": """
        **Bringing Art to Life in Appalachian Ohio**

        *When Emily decided to support the Arts & Culture pillar, she couldn't have imagined the ripple effect her generosity would create...*
        """,
        "Community & Economic Development": """
        **Revitalizing Main Street**

        *John had always felt a deep connection to his hometown, but he noticed that the once-thriving Main Street had fallen into decline...*
        """,
        "Education": """
        **Opening Doors to Education**

        *Education had always been close to Sarah's heart. By supporting the Education pillar, she aimed to break down barriers for students who lacked resources...*
        """,
        "Environmental Stewardship": """
        **Protecting Natural Treasures**

        *Michael cherished the natural beauty of Appalachian Ohio's landscapes. His donation to the Environmental Stewardship pillar was dedicated to preserving these treasures for future generations...*
        """,
        "Health & Human Services": """
        **Caring for Community Health**

        *Lisa recognized the challenges faced by remote communities in accessing healthcare. By contributing to the Health & Human Services pillar, she enabled the launch of mobile health clinics...*
        """
    }
    st.write(stories.get(selected_pillar, "Impact story not available for this pillar."))

def projected_community_impact(donation_amount):
    st.header("Projected Community Impact with Compounding")

    st.write("""
    Assuming 100% of your gift goes into an endowment, an annual return of **8%**, and an annual payout of **4%** to community projects, here's how your donation could impact the community over time:
    """)

    years_list = [10, 25, 100]
    annual_return_rate = 0.08  # 8% annual return
    annual_payout_rate = 0.04  # 4% annual payout to community

    data = []
    for years in years_list:
        endowment_balance = donation_amount
        cumulative_community_investment = 0

        for year in range(1, years + 1):
            # Calculate interest earned
            interest_earned = endowment_balance * annual_return_rate

            # Update endowment balance with interest
            endowment_balance += interest_earned

            # Calculate annual community investment
            annual_community_investment = endowment_balance * annual_payout_rate

            # Update cumulative community investment
            cumulative_community_investment += annual_community_investment

            # Deduct payout from endowment balance
            endowment_balance -= annual_community_investment

        data.append({
            "Years": years,
            "Total Dollars Invested into Community": f"${cumulative_community_investment:,.2f}",
            "Endowment Balance After Period": f"${endowment_balance:,.2f}"
        })

    st.table(data)

if __name__ == "__main__":
    main()
