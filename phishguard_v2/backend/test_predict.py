from model_loader import predict_url

urls = [
    "https://google.com",
    "http://paypal-login-verification-secure-update.com",
    "https://openai.com",
    "http://free-gift-card-claim-now.xyz"
]

for url in urls:
    prob, score = predict_url(url)
    print(f"{url} → {prob:.4f} → {score}")
