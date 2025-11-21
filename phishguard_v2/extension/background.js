function saveTabUrl(tabId) {
    chrome.tabs.get(tabId, (tab) => {
        if (tab && tab.url) {
            chrome.storage.local.set({ current_url: tab.url });
        }
    });
}

// When user switches tabs
chrome.tabs.onActivated.addListener((activeInfo) => {
    saveTabUrl(activeInfo.tabId);
});

// When URL changes in the current tab
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.url) {
        saveTabUrl(tabId);
    }
});
