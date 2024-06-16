import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import utils
import gpt
import time

import streamlit as st

import find_corr
import find_news
import find_tweets

# # Initialize chat history
if "messages_long" not in st.session_state:
    st.session_state.messages_long = []

if "openai" not in st.session_state:
    st.session_state.openai = gpt.chatgpt()

if 'button' not in st.session_state:
    st.session_state.button = False

if 'button_name' not in st.session_state:
    st.session_state.button_name = 'choose action'

def add_figs(data):
    data_with_signals = utils.add_signal_columns(data)
    fig.add_scatter(x=data_with_signals.index, y=data_with_signals['short_mavg'], mode='lines', name='50-Day SMA', line=dict(color='red'))
    fig.add_scatter(x=data_with_signals.index, y=data_with_signals['long_mavg'], mode='lines', name='200-Day SMA', line=dict(color='blue'))

    # Add markers for Golden Cross
    golden_crosses = data_with_signals[data_with_signals['Golden Cross'] == False]
    fig.add_scatter(x=golden_crosses.index, y=golden_crosses['short_mavg'], mode='markers', name='Golden Cross',
                    marker=dict(color='green', size=10, symbol='triangle-up'))

    # Add markers for Death Cross
    death_crosses = data_with_signals[data_with_signals['Death Cross'] == True]
    fig.add_scatter(x=death_crosses.index, y=death_crosses['short_mavg'], mode='markers', name='Death Cross',
                    marker=dict(color='red', size=10, symbol='triangle-down'))

def stream_txt(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

data = utils.get_data()

# Create a line plot
fig = px.line(data, x=data.index, y='value', title='APPLE Stock Price (6 months)')

# Add axis labels (optional, as Plotly will use default labels from DataFrame if not specified)
fig.update_layout(xaxis_title='Date', yaxis_title='Value')


# # Data points to be added as markers
green_points, red_points = utils.get_points(data)

# Add green points
fig.add_trace(
    go.Scatter(
        x=green_points['date'],
        y=green_points['value'],
        mode='markers',
        marker=dict(color='green', size=10),
        name='Buy'
    )
)

# Add red points
fig.add_trace(
    go.Scatter(
        x=red_points['date'],
        y=red_points['value'],
        mode='markers',
        marker=dict(color='red', size=10),
        name='Sell'
    )
)
if st.session_state.button:
    add_figs(data)

from streamlit_plotly_events import plotly_events

selected_points = plotly_events(fig)
if selected_points:
    st.session_state.button_name = 'action selected - press to analyze'
    # st.write(selected_points)

def click_button():
    st.session_state.button = not st.session_state.button

st.button(st.session_state.button_name, on_click=click_button)

if st.session_state.button:
    
    # The message and nested widget will remain on the page

    st.markdown("# AI Analysis")
    st.markdown("## Stock Graph")
    stock_text = st.session_state.openai.get_stock_summary() 
    st.write_stream(stream_txt(stock_text))
    st.markdown('---')

    st.markdown("## News")
    news_text = st.session_state.openai.get_news_summary(news=utils.get_news(),main_company="Apple",date="10/06/2024", companies_string="Apple, Microsoft and Google")
    st.write_stream(stream_txt(news_text))
    st.markdown('---')
    
    st.markdown("## Social Media")
    feed_text = st.session_state.openai.get_feed_summary(feed=utils.get_feed(),main_company="Apple",date="10/06/2024")
    st.write_stream(stream_txt(feed_text))
    st.markdown('---')

    # all_text = stock_text + news_text + feed_text

    st.markdown("## Summary")
    summary = st.session_state.openai.call_gpt([{"role": "user", "content": f"""
## stock report:
{stock_text}

## news report:
{news_text}

## feed report:
{feed_text}

as an educator in fintech, the above is three reports - graph, news and social media about apple stock. after reading this reports a professional trader decided to invest.
summarise in short paragraph his decision and what made him make that decision
"""}])
    st.write_stream(stream_txt(summary))
    st.markdown('---')
    
else:
    st.markdown('---')

     
with st.sidebar:
    st.title("Echo Bot")
    messages = st.container(height=500)
    if prompt := st.chat_input("Ask me anything"):
        st.session_state.messages_long.append({"role": "user", "content": prompt})
        text = st.session_state.openai.rag_q(prompt)
        st.session_state.messages_long.append({"role": "assistant", "content": text})
        for message in st.session_state.messages_long:
                messages.chat_message(message["role"]).write(message["content"])
        # messages.chat_message("user").write(prompt)
        # messages.chat_message("assistant").write(f"Echo: {prompt}")
    # Display chat messages from history on app rerun
    # messages_container = st.container(height=500)
    # st.chat_input("Say something")
    # for message in st.session_state.messages:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])

# what is a moving average?