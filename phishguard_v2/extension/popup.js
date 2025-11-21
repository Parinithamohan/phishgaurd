chrome.storage.local.get("current_url", async (data) => {
    const url = data.current_url;

    document.getElementById("status").innerText = "Scanning URL...";
    
    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    });

    const result = await response.json();

    document.getElementById("label").innerText = result.label;
    document.getElementById("prob").innerText = "Probability: " + result.probability;
});
