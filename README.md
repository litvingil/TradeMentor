# TradeMentor

TradeMentor is an innovative fintech application designed to revolutionize the learning and engagement experience for novice traders. By integrating real-time trading with educational tools and AI-driven insights, TradeMentor empowers users to mimic professional trades while gaining a deep understanding of trading decisions and market dynamics.

## Key Features

- **Copy Trading with Real-Time Learning**: Follow and replicate the trades of seasoned traders and get real-time explanations and analyses of each trading decision.

- **Advanced Analytics**: Utilize a range of analytical tools, from traditional techniques like moving averages and RSI to advanced machine learning-driven time series models.

- **News and Social Media Insights**: Stay updated with real-time news and social media trends that affect market conditions and trading decisions.

- **Personalized Teaching Assistant**: Each user can interact with a personalized chatbot powered by Retrieval-Augmented Generation (RAG) technology, designed to adapt to individual learning paces and styles.

- **Integration and Compatibility**: Seamlessly integrates with existing platforms such as eToro or QuadCode, enhancing your trading experience without disrupting existing setups.

- **Community and Network Building**: Connect with traders who share similar interests, risk tolerance, and trading preferences through an AI-driven similarity search.

- **Interactive Learning Experience**: Contribute your own insights and learn actively within the TradeMentor community.

## Getting Started

Clone the repository to your local machine:

```bash
git clone https://github.com/litvingil/TradeMentor.git
cd TradeMentor
```

### Prerequisites

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the Application

To start the application, run the following command in your terminal:

```bash
python main_app.py
```

## Usage

- **Home_page.py**: The entry script that loads the home page of the application.
- **main_app.py**: The main script that handles the application logic.
- **utils.py**: Contains utility functions used across different modules.
- **RSI_test.py** and **SMA_test.py**: These scripts are responsible for testing and demonstrating the implementation of technical indicators (Relative Strength Index and Simple Moving Average, respectively) used in market analysis.
- **find_corr.py**: Analyzes and identifies correlations between different financial instruments, helping users to understand market relationships and diversify their trading strategies.
- **find_news.py** and **find_tweets.py**: These scripts gather real-time news and tweets related to specific stocks or market events, providing users with insights into how current events might influence market dynamics.
- **translate.py**: Used for translating news content from various languages.
- **create_rag_db.ipynb**: A Jupyter notebook that guides users through the process of setting up the Retrieval-Augmented Generation (RAG) database, crucial for powering the personalized teaching assistant feature.
- **gpt.py**: Integrates LLM generate predictive text and automated responses, which are essential for the chatbot's functionality in educating users about trading concepts.
- **Market_Timing_with_Moving_Averages.pdf** and **embeddings.csv**: These resources include detailed documentation on market timing techniques using moving averages and data embeddings used for machine learning models within the platform.

Additional scripts and notebooks like `create_rag_db.ipynb` for setting up the RAG database, and analytical scripts (`RSI_test.py`, `SMA_test.py`) are also included.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

- Nadav Rubinstein
- Gil Litvin

Project Link: [https://github.com/your-username/TradeMentor](https://github.com/your-username/TradeMentor)

## Acknowledgements

- **Mentors from the Hackathon**: Special thanks to all the mentors who provided invaluable guidance, insights, and support throughout the development of TradeMentor during the hackathon. Your expertise and encouragement have been pivotal to our project's success.

- [QuadCode](https://www.quadcode.com)
- We also extend our appreciation to all the community members and technical experts whose advice and feedback have helped shape TradeMentor into a robust educational tool for traders.
