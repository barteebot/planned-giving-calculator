# planned_giving_calculator.py

import streamlit as st
import random

def main():
    st.title("Planned Giving Calculator")

    # Embed the introductory YouTube video at the top
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

def calculate_bequest(donation_amount, tax_rate, selected_pillar):
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Bequest Results")
    st.write(f"Estimated Estate Tax Savings: **${tax_savings:,.2f}**")
    st.write("Your bequest will leave a lasting legacy without affecting your current financial situation.")
    display_impact_story(selected_pillar, donation_amount)

def calculate_gift_annuity(donation_amount, donor_age, tax_rate, selected_pillar):
    annuity_rate = get_annuity_rate(donor_age)
    annual_income = donation_amount * annuity_rate
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Gift Annuity Results")
    st.write(f"Annual Income: **${annual_income:,.2f}**")
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("Receive guaranteed income for life while supporting a worthy cause.")
    display_impact_story(selected_pillar, donation_amount)

def calculate_remainder_trust(donation_amount, donor_age, tax_rate, selected_pillar):
    annual_payout_rate = 0.05  # Assuming a 5% payout rate
    annual_income = donation_amount * annual_payout_rate
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Charitable Remainder Trust Results")
    st.write(f"Annual Income: **${annual_income:,.2f}**")
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("Benefit from income payments and reduce your taxable estate.")
    display_impact_story(selected_pillar, donation_amount)

def calculate_donor_advised_fund(donation_amount, tax_rate, selected_pillar):
    tax_savings = donation_amount * (tax_rate / 100)
    st.subheader("Donor-Advised Fund Results")
    st.write(f"Immediate Tax Deduction: **${tax_savings:,.2f}**")
    st.write("Recommend grants to charities over time while receiving an immediate tax benefit.")
    display_impact_story(selected_pillar, donation_amount)

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

def display_impact_story(selected_pillar, donation_amount):
    st.header(f"Impact Story in {selected_pillar}")

    # Determine the donation amount range
    if donation_amount <= 10000:
        amount_range = "$0 - $10,000"
    elif 10000 < donation_amount <= 25000:
        amount_range = "$10,001 - $25,000"
    elif 25000 < donation_amount <= 50000:
        amount_range = "$25,001 - $50,000"
    elif 50000 < donation_amount <= 100000:
        amount_range = "$50,001 - $100,000"
    else:
        amount_range = "$100,001 and above"

    # Placeholder list of video URLs (since we can't access YouTube directly)
    # Replace these URLs with actual video URLs from the FAO YouTube channel
    video_urls = [
        "https://youtu.be/dQw4w9WgXcQ",
        "https://youtu.be/3GwjfUFyY6M",
        "https://youtu.be/lY2yjAdbvdQ",
        "https://youtu.be/2Vv-BfVoq4g",
        "https://youtu.be/9bZkp7q19f0"
    ]

    # Select a random video URL
    random_video = random.choice(video_urls)
    st.video(random_video)

    # Impact stories dictionary
    impact_stories = {
        ("Arts & Culture", "$0 - $10,000"): """
        **Nurturing Young Artists**

        *With a generous gift in this range, we were able to supply art materials to local schools. Students like Lily discovered their passion for painting, leading to local exhibitions that brought the community together.*
        """,
        ("Arts & Culture", "$10,001 - $25,000"): """
        **Community Mural Projects**

        *Your contribution can fund community mural projects, transforming public spaces into vibrant works of art. Residents take pride in their neighborhoods, fostering unity and cultural appreciation.*
        """,
        # ... (Continue this pattern for all combinations)
    }

    # Fetch the appropriate story
    story_key = (selected_pillar, amount_range)
    story = impact_stories.get(story_key, "Impact story not available for this selection.")

    st.write(story)

if __name__ == "__main__":
    main()
