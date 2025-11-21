import pandas as pd

# =====================================================
# 1. LOAD LEGIT (TRANCOLIST)
# =====================================================
tranco = pd.read_csv(
    "dataset/legit/tranco_list.csv",
    usecols=[0],          # First column contains domain
    names=["url"],        # Rename to "url"
    header=None
)

# Convert domains → full URLs (so features like https, slash_count work)
tranco["url"] = "https://" + tranco["url"].astype(str)
tranco["label"] = 0   # legit


# =====================================================
# 2. LOAD OPENPHISH
# (Your file is just plain URLs one per line)
# =====================================================
openphish = pd.read_csv(
    "dataset/phishing/openphish.csv",
    names=["url"],       # The file contains just URLs
    header=None
)
openphish["label"] = 1


# =====================================================
# 3. LOAD URLHAUS
# (Your dataset has many columns — URL is column index 2)
# =====================================================
urlhaus = pd.read_csv("dataset/phishing/urlhaus.csv")

# We need only the URL column → column `"url"` or index 2
if "url" in urlhaus.columns:
    urlhaus = urlhaus[["url"]]
else:
    urlhaus = urlhaus.iloc[:, [2]]   # fallback for column index 2

urlhaus.columns = ["url"]
urlhaus["label"] = 1


# =====================================================
# 4. COMBINE ALL
# =====================================================
df = pd.concat([tranco, openphish, urlhaus], ignore_index=True)

# Remove duplicates
df = df.drop_duplicates(subset=["url"])

# Remove missing/empty
df = df.dropna(subset=["url"])

# Save master CSV
df.to_csv("MASTER_URL_DATASET.csv", index=False)

print("MASTER_URL_DATASET.csv created successfully!")
print("Total rows:", df.shape)
print(df.head())
