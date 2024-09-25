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

        *When Emily decided to support the Arts & Culture pillar, she couldn't have imagined the ripple effect her generosity would create. Her donation funded a community theater program that brought together children from diverse backgrounds. Over the course of the program, these young individuals not only discovered their hidden talents but also learned the value of teamwork and self-expression.*

        *The community theater became a beacon of creativity in the region, hosting performances that attracted audiences from neighboring towns. Parents and teachers noticed a positive change in the children's confidence and academic performance. Emily's contribution didn't just support an arts program; it ignited a cultural renaissance that enriched the entire community.*

        *Inspired by the success, local businesses and artists collaborated to establish annual art festivals and workshops. Emily's initial act of kindness had blossomed into a sustained movement, proving that the arts truly have the power to transform lives.*
        """,
        "Community & Economic Development": """
        **Revitalizing Main Street**

        *John had always felt a deep connection to his hometown, but he noticed that the once-thriving Main Street had fallen into decline. Determined to make a difference, he directed his donation to the Community & Economic Development pillar. His funds were used to renovate historic buildings, creating attractive spaces for new businesses.*

        *The revitalization project breathed new life into the local economy. Small businesses began to flourish, offering unique products and services that drew visitors from afar. Job opportunities increased, reducing unemployment and fostering a sense of pride among residents.*

        *The transformation of Main Street became a model for neighboring communities. John's dedication not only rejuvenated a town but also set in motion a wave of economic growth throughout Appalachian Ohio. His legacy is seen in the bustling streets and the smiles of entrepreneurs who found their start because of his generosity.*
        """,
        "Education": """
        **Opening Doors to Education**

        *Education had always been close to Sarah's heart. By supporting the Education pillar, she aimed to break down barriers for students who lacked resources. Her donation established a scholarship fund for underprivileged youth, granting them access to higher education that was once beyond their reach.*

        *One of the scholarship recipients, Alex, became the first in his family to attend college. His academic achievements inspired his younger siblings and peers to pursue their own educational goals. The ripple effect extended to the community, where educational attainment began to rise collectively.*

        *Sarah's commitment didn't stop at scholarships. She also funded mentorship programs and educational workshops. Her holistic approach ensured that students not only had financial support but also the guidance needed to succeed. Sarah's impact is a testament to how investing in education can uplift entire communities.*
        """,
        "Environmental Stewardship": """
        **Protecting Natural Treasures**

        *Michael cherished the natural beauty of Appalachian Ohio's landscapes. His donation to the Environmental Stewardship pillar was dedicated to preserving these treasures for future generations. The funds were used to protect vital waterways and expand conservation areas.*

        *Through his support, initiatives were launched to restore habitats and promote biodiversity. Educational programs taught locals about sustainable practices, fostering a community that values and actively participates in environmental preservation.*

        *One notable project was the creation of a network of hiking trails that not only provided recreational opportunities but also boosted eco-tourism. Michael's passion for the environment resulted in tangible benefits for both nature and the local economy, ensuring that the region's natural beauty remains unspoiled.*
        """,
        "Health & Human Services": """
        **Caring for Community Health**

        *Lisa recognized the challenges faced by remote communities in accessing healthcare. By contributing to the Health & Human Services pillar, she enabled the launch of mobile health clinics that brought essential medical services directly to those in need.*

        *These clinics provided routine check-ups, vaccinations, and health education, significantly improving the well-being of residents. The convenience of local access reduced untreated illnesses and fostered a healthier population.*

        *Moreover, Lisa's support helped establish partnerships with larger healthcare providers, expanding the range of services available. Her commitment not only addressed immediate health concerns but also laid the groundwork for sustainable healthcare solutions in Appalachian Ohio.*
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
