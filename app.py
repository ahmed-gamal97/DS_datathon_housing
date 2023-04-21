import streamlit as st
import pandas as pd
from src.pd_functions import *

# Constants
RESULTS_PATH = 'data/results_housing_class.csv'

def main():
    participant_name = get_participant_name()

    if participant_name:
        uploaded_file = st.file_uploader("Choose a file")

        if uploaded_file:
            process_uploaded_file(uploaded_file, participant_name)
        else:
            st.warning('Please upload a file.')
    else:
        st.warning('Please enter a participant name.')

    display_leaderboard()

def get_participant_name():
    text_input_container = st.empty()
    participant_name = text_input_container.text_input(
        "Introduce participant name: ",
        key="text_input"
    )
    return participant_name

def process_uploaded_file(uploaded_file, participant_name):
    try:
        test = get_ready_test(RESULTS_PATH, uploaded_file)
        participant_results = get_accuracy(RESULTS_PATH, test)

        st.success('Dataframe uploaded successfully!')
        display_participant_results(participant_results)
        update_and_plot_submissions(participant_results, participant_name)
    except:
        st.error('The file has a wrong format, please, review it and load it again.')

def display_participant_results(participant_results):
    st.title('Participant results')
    st.dataframe(participant_results)

def update_and_plot_submissions(participant_results, participant_name):
    try:
        update_submissions(participant_results)
        plot_submissions(participant_name)
    except:
        participant_results.to_pickle('files_to_update/submissions.pkl')

def display_leaderboard():
    try:
        show_leaderboard()
    except:
        st.write("There is no submission.")

if __name__ == "__main__":
    main()
