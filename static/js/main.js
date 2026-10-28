function openTab(tabId, button) {
    const tabs = document.querySelectorAll(".tab-content");
    const buttons = document.querySelectorAll(".tab-button");

    tabs.forEach(function(tab) {
        tab.classList.remove("active");
    });

    buttons.forEach(function(btn) {
        btn.classList.remove("active");
    });

    document.getElementById(tabId).classList.add("active");
    button.classList.add("active");
}