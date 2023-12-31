import streamlit as st

import logging

# Save to File
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(levelname)s %(asctime)s.%(msecs)03d -%(message)s")

# File 
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def main():
	st.title("Adding Logs To App")
	st.text("Track All Activities/Pages Visited For App")

	menu = ["Home","EDA","ML","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		logger.info("Home Section")
		
	elif choice == "EDA":
		st.subheader("EDA")
		logger.info("EDA Section")
		
	elif choice == "ML":
		st.subheader("ML")
		logger.info("ML Section")
		
	elif choice == "Analytics":
		st.subheader("Analytics")
		logger.info("Analytics Section")
		
	else:
		st.subheader("About")
		logger.info("About Section")

if __name__ == '__main__':
	main()
