import pandas as pd
import tldextract
import re
import pandas as pd
import numpy as np
# Load the original dataset
df = pd.read_csv("C:/Users/parin/phishguard_v2/master_dataset/MASTER_URL_DATASET.csv") # columns: url,label

def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_https'] = int(url.startswith("https"))
    features['special_char_count'] = len(re.findall(r'[^a-zA-Z0-9]', url))
    features['suspicious_keyword'] = int(any(k in url.lower() for k in ["login", "verify", "secure", "update", "account", "bank", "free", "gift", "claim"]))
    ext = tldextract.extract(url)
    features['subdomain_depth'] = len(ext.subdomain.split('.')) if ext.subdomain else 0
    # IP address instead of domain
    features['has_ip'] = int(bool(re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url)))
    return features

# Apply feature extraction
features_list = df['url'].apply(extract_features)
features_df = pd.DataFrame(list(features_list))
features_df['label'] = df['label']

# Save numeric dataset
features_df.to_csv("MASTER_URL_NUMERIC.csv", index=False)
print("✅ Numeric features dataset saved as MASTER_URL_NUMERIC.csv")

