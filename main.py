import static_page_parsing
import json
import streamlit as st


def main():
    # load url and other parameters
    with open('website_urls.json', 'r') as f1, open('filtered_positions.json', 'r') as f2:
        websites = json.load(f1)
        filtered_position_list = json.load(f2)

    # Iterate all websites, send them to parsers according to their webpage types.
    results = static_page_parsing.parsing(websites)


    new_companies_filter = st.button("Show all positions")

    for company_positions in results:
        st.markdown(f"**[{company_positions['company_name']}]({company_positions['URL']})**:")
        if len(company_positions['position_list']) > 0:
            for position in company_positions['position_list']:
                if position.strip() not in filtered_position_list:
                    st.write(f"- {position}")
        else:
            st.write("No available jobs")
            print()



if __name__ == "__main__":
    main()