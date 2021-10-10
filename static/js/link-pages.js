function linkPages() {
    const links = document.querySelectorAll("a");

    links.forEach((link, index) => {
        if (link.text.toLowerCase().includes("account")) {
            console.log("Account");
        }

        else if (link.textContent.toLowerCase().includes("person")) {
            if (link.textContent.toLowerCase().includes("list")) {
                link.href = "/person/"
            }
        }

        else if (link.textContent.toLowerCase().includes("office")) {
            console.log("Office");
        }

    });

}
