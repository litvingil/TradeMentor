import pandas as pd
import numpy as np
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Define the categories for each question
stocks_experience = ['None', 'Less than 10', '10 to 20', 'More than 20']
crypto_experience = ['None', 'Less than 10', '10 to 20', 'More than 20']
leverage_experience = ['None', 'Less than 10', '10 to 20', 'More than 20']
invested_amount = ['1-500', '500-2000', 'More than 2000']
education = ['None', 'Work experience', 'Professional experience', 'Academic degree', 'Financial related field', 'Online trading courses']
interests = ['Stocks', 'Crypto', 'Currencies', 'Commodities', 'Indices']
hold_positions = ['Few seconds to 24 hours', 'Few weeks to several months', 'More than several months/years']
deposit_plan = ['Up to 20k', '20k-50k', '50k-200k', '200k-500k', '500k-1m', 'Above 1m']
risk_reward = ['5-5', '10-10', '20-20', '40-40', '80-80']

# Sample bios and investment strategies
bios = [
    "I have been trading stocks for over a decade.",
    "Crypto enthusiast with a focus on long-term investments.",
    "Professional trader with experience in commodities and currencies.",
    "New to trading but eager to learn and grow.",
    "Experienced in leveraging products for high-risk, high-reward trades.",
    "Seasoned investor with a diverse portfolio including stocks, bonds, and mutual funds.",
    "Tech-savvy trader specializing in tech stocks and emerging markets.",
    "Finance graduate with a passion for trading and market analysis.",
    "Part-time trader focusing on index funds and ETFs.",
    "Retired financial analyst now investing full-time in real estate and commodities.",
    "Day trader with a knack for spotting short-term opportunities.",
    "Long-term investor with a preference for dividend-paying stocks.",
    "Amateur trader with a background in data science and algorithmic trading.",
    "Forex trader with over 5 years of experience in the currency markets.",
    "Environmental enthusiast investing in renewable energy and green technology stocks.",
    "Healthcare professional investing in biotech and pharmaceutical stocks.",
    "Small business owner using profits to invest in various asset classes.",
    "Travel enthusiast investing in airline and tourism stocks.",
    "Experienced in trading futures and options, with a focus on risk management.",
    "Retired engineer with a portfolio centered on industrial and manufacturing stocks.",
    "Young professional exploring investments in startup equities and venture capital.",
    "Blockchain expert with a portfolio heavily weighted towards cryptocurrencies.",
    "Growth-oriented investor focusing on small-cap and mid-cap stocks.",
    "Investor with a keen interest in the automotive and electric vehicle sector.",
    "New investor learning the ropes with a diversified approach to minimize risk."
]

# Generate synthetic data
np.random.seed(42)  # For reproducibility
num_users = 1000

synthetic_data = {
    'Stocks_Experience': np.random.choice(stocks_experience, num_users),
    'Stocks_Invested_Amount': np.random.choice(invested_amount, num_users),
    'Crypto_Experience': np.random.choice(crypto_experience, num_users),
    'Crypto_Invested_Amount': np.random.choice(invested_amount, num_users),
    'Leverage_Experience': np.random.choice(leverage_experience, num_users),
    'Education': np.random.choice(education, num_users),
    'Interests': np.random.choice(interests, num_users),
    'Hold_Positions': np.random.choice(hold_positions, num_users),
    'Deposit_Plan': np.random.choice(deposit_plan, num_users),
    'Risk_Reward': np.random.choice(risk_reward, num_users),
    'Profit_Loss': np.random.normal(loc=0, scale=10, size=num_users),  # Normal distribution for profit/loss
    'Bio': np.random.choice(bios, num_users),
    'Portfolio': [f"Portfolio {i}" for i in range(num_users)]  # Dummy portfolio names
}

# Create a DataFrame
user_profiles = pd.DataFrame(synthetic_data)

# Example new user profile
new_user_profile = {
    'Stocks_Experience': '10 to 20',
    'Stocks_Invested_Amount': '500-2000',
    'Crypto_Experience': 'Less than 10',
    'Crypto_Invested_Amount': '1-500',
    'Leverage_Experience': 'None',
    'Education': 'Online trading courses',
    'Interests': 'Stocks',
    'Hold_Positions': 'Few weeks to several months',
    'Deposit_Plan': '20k-50k',
    'Risk_Reward': '10-10',
    'Bio': "I am new to trading and interested in stocks.",
}

# Define keys for matching
matching_keys = [
    'Interests',
    'Hold_Positions',
    'Deposit_Plan',
    'Risk_Reward'
]

# Function to calculate similarity score
def calculate_similarity(user, new_user, keys):
    score = 0
    for key in keys:
        if user[key] == new_user[key]:
            score += 1
    return score/len(matching_keys)

# Apply the function to all users and sort by similarity score
user_profiles['Similarity_Score'] = user_profiles.apply(calculate_similarity, new_user=new_user_profile, keys=matching_keys, axis=1)

# BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Function to get BERT embeddings for a given text
def get_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

# Get embeddings for the new user's Bio and Investment Strategy
new_user_bio_embedding = get_embeddings(new_user_profile['Bio'])

# Calculate cosine similarity for the free text fields
user_profiles['Bio_Embedding'] = user_profiles['Bio'].apply(lambda x: get_embeddings(x))

def cosine_sim(a, b):
    return (cosine_similarity(a.reshape(1, -1), b.reshape(1, -1)).item()+1)/2

user_profiles['Bio_Similarity'] = user_profiles['Bio_Embedding'].apply(lambda x: cosine_sim(x, new_user_bio_embedding))

# Combine the similarity scores
user_profiles['Total_Similarity'] = user_profiles['Similarity_Score'] + user_profiles['Bio_Similarity']

# Get top matches
top_matches = user_profiles.sort_values(by='Total_Similarity', ascending=False).head(5)

# Display the top matching profiles
print(top_matches[['Portfolio', 'Total_Similarity', 'Profit_Loss', 'Bio']])
