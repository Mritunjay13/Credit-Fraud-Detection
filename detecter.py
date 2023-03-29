import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import processor
import Analysis
import PyPDF2
import pathlib

# Main Web Design
st.sidebar.title("Loan Fraud Detection")
user_file = st.sidebar.file_uploader("Upload_file", type=['csv', 'xlsx', 'pdf'], accept_multiple_files=False)
if user_file is not None:
    data = pd.read_csv(user_file)
    df = processor.preprocess(data)
    st.title(':red[Loan Fraud Detection Analysis]')
    v1 = st.title('Loan Data')
    v2 = st.dataframe(df)
    total_memeber = Analysis.totalmember(df)
    st.subheader("Total Members: {}".format(total_memeber))


    # Bivariate Analysis on NAME_CONTRACT_STATUS and AMT_CREDIT
    st.title('Current Status and Total Payment of loan')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax = plt.gca()
    ax.plot(df['loan_status'], df['total_pymnt'], 'o', c='red', alpha=0.1)
    ax.set_xlabel('Current Status of Members')
    ax.set_ylabel('Total amount of Pyment')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # Display those member whose current status is fully paid
    st.title('Fully Paid Loan Amount Members')
    fully_paid = Analysis.fullypaid(df)
    st.dataframe(fully_paid)
    total_memeber = Analysis.totalmember(fully_paid)
    st.subheader("Total Members: {}".format(total_memeber))

    # univariate analysis on contract status Approved
    st.header('Univariate Analysis on current status fully paid')

    tab1, tab2, tab3, tab4= st.tabs(["Purpose", "Term", "Grade", "Home_Ownership"])

    with tab1:
        st.header("Type of Loan")
        plt.figure(figsize=(18, 25))
        # subplot 1: loan type
        plt.subplot(4, 2, 1)
        my_plot = sns.countplot(y='purpose', data=fully_paid)
        my_plot.set_xticklabels(my_plot.get_xticklabels(), rotation=90)
        plt.title("TYPES OF LOAN", size=20)
 
        st.pyplot()

    with tab2:
        st.header("Loan Term")
        # subplot 2: Term
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 2)
        sns.countplot(x='term', data=fully_paid)
        plt.title("Term of Months", size=20)

        st.pyplot()

    with tab3:
        st.header("Grade")
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 3)
        sns.countplot(x='grade', data=fully_paid)
        plt.title("Grade of User", size=20)
        
        st.pyplot()
    with tab4:
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 4)
        sns.countplot(x='home_ownership', data=fully_paid)
        plt.title("Home Ownership", size=20)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    # Display those member whose current status is Charged Off
    st.title('Charged Off Members Details')
    charge_off = Analysis.chargedoff(df)
    st.dataframe(charge_off)
    total_memeber = Analysis.totalmember(charge_off)
    st.subheader("Total Members: {}".format(total_memeber))

    # univariate analysis on contract status Approved
    st.header('Univariate Analysis on current status of Charged Off')
    tab1, tab2, tab3, tab4= st.tabs(["Pupose", "Term", "Grade", "Home_Ownership"])

    with tab1:
        st.header("Type of Loan")
        plt.figure(figsize=(18, 25))
        # subplot 1: loan type
        plt.subplot(4, 2, 1)
        my_plot = sns.countplot(y='purpose',data=charge_off)
        my_plot.set_xticklabels(my_plot.get_xticklabels(), rotation=90)
        plt.title("TYPES OF LOAN", size=20)
        st.pyplot()

    with tab2:
        st.header("Term of Months")
        # subplot 2: Term
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 2)
        sns.countplot(x='term', data=charge_off)
        plt.title("Term of Months", size=20)
        st.pyplot()

    with tab3:
        st.header("An owl")
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 3)
        sns.countplot(x='grade', palette='gist_heat_r', data=charge_off)
        plt.title("Grade of User", size=20)
        st.pyplot()
    with tab4:
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 4)
        sns.countplot(x='home_ownership', data=charge_off)
        plt.title("Home Ownership", size=20)
        st.pyplot()


    # Display those member whose current status is Current
    st.title('Current Status Members Details')
    current = Analysis.current_u(df)
    st.dataframe(current)
    total_memeber = Analysis.totalmember(current)
    st.subheader("Total Members: {}".format(total_memeber))

    # univariate analysis on contract status Approved
    st.header('Univariate Analysis on current status of current Members')
    tab1, tab2, tab3, tab4= st.tabs(["Pupose", "Term", "Grade", "Home_Ownership"])

    with tab1:
        st.header("Type of Loan")
        plt.figure(figsize=(18, 25))
        # subplot 1: loan type
        plt.subplot(4, 2, 1)
        my_plot = sns.countplot(y='purpose', data=current)
        my_plot.set_xticklabels(my_plot.get_xticklabels(), rotation=90)
        plt.title("TYPES OF LOAN", size=20)
        st.pyplot()

    with tab2:
        st.header("Term of Months")
        # subplot 2: Term
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 2)
        sns.countplot(x='term', data=current)
        plt.title("Term of Months", size=20)
        
        st.pyplot()

    with tab3:
        st.header("Grade of user")
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 3)
        sns.countplot(x='grade', data=current)
        plt.title("Grade of User", size=20)
        st.pyplot()
    with tab4:
        st.header("Home Ownership")
        plt.figure(figsize=(18, 25))
        plt.subplot(4, 2, 4)
        sns.countplot(x='home_ownership', data=current)
        plt.title("Home Ownership", size=20)

        st.pyplot()



    st.title('Type of loan and Total Payment')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax = plt.gca()
    ax.plot(df['total_pymnt'],df['purpose'], 'o', c='blue', alpha=0.1)
    ax.set_xlabel('Type of Loan')
    ax.set_ylabel('Total ammount of Payment')
    plt.xticks(rotation=90)

    st.pyplot(fig)

